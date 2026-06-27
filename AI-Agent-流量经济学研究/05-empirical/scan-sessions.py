#!/usr/bin/env python3
"""
扫描本地 Claude Code 会话日志，提取每次 API 调用的 token 计量。

数据来源：~/.claude/projects/*/<session-uuid>.jsonl
研究目的：构造真实的 input:output token 分布，量化 Agent 流量上下行比例。

字段口径（参见 https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching）：
  - input_tokens                      非缓存的新输入 token
  - cache_creation_input_tokens       本轮写入 cache 的输入 token
  - cache_read_input_tokens           命中 cache 的输入 token（仍需在请求体里发送）
  - output_tokens                     模型输出 token

约定：
  上传 token  = input_tokens + cache_creation + cache_read
  下载 token  = output_tokens
  上下行比例  = 上传 / 下载

注意：
  - 本指标统计的是 token 数，而非字节数。token→字节转换需另算放大系数（UTF-8/JSON/HTTP2/TLS）。
  - cache_read 在 Anthropic API 中虽计费打折，但客户端仍需提交完整 prompt，故计入上行。
  - 不区分 sidechain（Agent tool 中创建的子代理），全部计入。
"""
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

PROJECTS_ROOT = Path("/Users/roger/.claude/projects")
OUT_PATH = Path("/Users/roger/Work/Blog/AI-Agent-流量经济学研究/05-empirical/scan-result.jsonl")
SUMMARY_PATH = Path("/Users/roger/Work/Blog/AI-Agent-流量经济学研究/05-empirical/scan-summary.md")


def iter_assistant_records():
    for jsonl in PROJECTS_ROOT.rglob("*.jsonl"):
        project = jsonl.parent.name
        session = jsonl.stem
        try:
            with jsonl.open() as f:
                for line in f:
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if rec.get("type") != "assistant":
                        continue
                    msg = rec.get("message")
                    if not isinstance(msg, dict):
                        continue
                    usage = msg.get("usage")
                    if not isinstance(usage, dict):
                        continue
                    yield {
                        "project": project,
                        "session": session,
                        "timestamp": rec.get("timestamp"),
                        "model": msg.get("model"),
                        "input_tokens": usage.get("input_tokens", 0) or 0,
                        "cache_creation": usage.get("cache_creation_input_tokens", 0) or 0,
                        "cache_read": usage.get("cache_read_input_tokens", 0) or 0,
                        "output_tokens": usage.get("output_tokens", 0) or 0,
                        "is_sidechain": rec.get("isSidechain", False),
                    }
        except OSError:
            continue


def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    by_project = defaultdict(lambda: {"calls": 0, "up": 0, "down": 0, "cache_read": 0, "cache_create": 0, "new_input": 0})
    by_model = defaultdict(lambda: {"calls": 0, "up": 0, "down": 0})
    totals = {"calls": 0, "up": 0, "down": 0, "cache_read": 0, "cache_create": 0, "new_input": 0}
    ratios = []
    with OUT_PATH.open("w") as fout:
        for r in iter_assistant_records():
            up = r["input_tokens"] + r["cache_creation"] + r["cache_read"]
            down = r["output_tokens"]
            if up == 0 and down == 0:
                continue
            fout.write(json.dumps({**r, "up": up, "down": down}, ensure_ascii=False) + "\n")

            totals["calls"] += 1
            totals["up"] += up
            totals["down"] += down
            totals["cache_read"] += r["cache_read"]
            totals["cache_create"] += r["cache_creation"]
            totals["new_input"] += r["input_tokens"]

            p = by_project[r["project"]]
            p["calls"] += 1
            p["up"] += up
            p["down"] += down
            p["cache_read"] += r["cache_read"]
            p["cache_create"] += r["cache_creation"]
            p["new_input"] += r["input_tokens"]

            m = by_model[r["model"] or "unknown"]
            m["calls"] += 1
            m["up"] += up
            m["down"] += down

            if down > 0:
                ratios.append(up / down)

    ratios.sort()
    n = len(ratios)
    def pct(p):
        if not ratios:
            return None
        idx = max(0, min(n - 1, int(p * n)))
        return ratios[idx]

    # 写 Markdown summary
    lines = []
    lines.append("# 本地 Claude Code 会话 token 分布扫描 — 实测结果\n")
    lines.append(f"扫描会话条数：**{totals['calls']:,}**（来自 {len(by_project)} 个项目目录）\n")
    lines.append("## 总量\n")
    lines.append(f"- 上传 token 总计：{totals['up']:,}")
    lines.append(f"- 下载 token 总计：{totals['down']:,}")
    if totals['down'] > 0:
        lines.append(f"- **总体 上行/下行 token 比例：{totals['up']/totals['down']:.2f} : 1**")
    lines.append("")
    lines.append(f"### 上行 token 的组成")
    if totals['up'] > 0:
        lines.append(f"- 新增（未缓存）输入：{totals['new_input']:,} ({totals['new_input']/totals['up']*100:.1f}%)")
        lines.append(f"- 缓存写入：{totals['cache_create']:,} ({totals['cache_create']/totals['up']*100:.1f}%)")
        lines.append(f"- 缓存读取：{totals['cache_read']:,} ({totals['cache_read']/totals['up']*100:.1f}%)")
    lines.append("")
    lines.append("## 单次调用上下行比例分位数\n")
    lines.append("| 分位 | up/down |")
    lines.append("|---|---|")
    for p in [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]:
        v = pct(p)
        lines.append(f"| p{int(p*100)} | {v:.2f} |" if v else f"| p{int(p*100)} | n/a |")
    lines.append("")
    lines.append("## 按模型聚合\n")
    lines.append("| 模型 | 调用数 | 上行总 | 下行总 | 比例 |")
    lines.append("|---|---|---|---|---|")
    for m, s in sorted(by_model.items(), key=lambda x: -x[1]['calls']):
        ratio = s['up']/s['down'] if s['down'] else 0
        lines.append(f"| {m} | {s['calls']:,} | {s['up']:,} | {s['down']:,} | {ratio:.2f} |")
    lines.append("")
    lines.append("## 按项目类型聚合（Top 15）\n")
    lines.append("| 项目目录 | 调用数 | 上行总 | 下行总 | 比例 |")
    lines.append("|---|---|---|---|---|")
    for p, s in sorted(by_project.items(), key=lambda x: -x[1]['calls'])[:15]:
        ratio = s['up']/s['down'] if s['down'] else 0
        lines.append(f"| `{p}` | {s['calls']:,} | {s['up']:,} | {s['down']:,} | {ratio:.2f} |")
    lines.append("")
    SUMMARY_PATH.write_text("\n".join(lines))
    print(f"wrote {OUT_PATH} ({totals['calls']:,} records)")
    print(f"wrote {SUMMARY_PATH}")
    print(f"总体 up/down = {totals['up']/totals['down']:.2f}" if totals['down'] else "no output tokens")


if __name__ == "__main__":
    main()
