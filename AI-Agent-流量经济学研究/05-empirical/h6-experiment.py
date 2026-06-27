#!/usr/bin/env python3
"""
H6 实验：测量 Anthropic API 在 cache_read 场景下的 HTTP 请求体字节数。

研究目的：区分 prompt caching 的两种可能实现
  情景 A: cache_read 时 HTTP body 仍含完整 prompt（仅服务端 prefill 优化）
  情景 B: cache_read 时 HTTP body 只发 cache key/reference（同时削减字节与计费）

参考：05-empirical/H6-抓包协议.md
依赖：pip install anthropic httpx
环境变量：ANTHROPIC_API_KEY 必需

输出：
  h6-results.jsonl 原始记录
  控制台打印组 1/2/3 平均字节数与组 3/组 2 字节比
"""
import os
import json
import time
from pathlib import Path

try:
    import httpx
    import anthropic
except ImportError:
    raise SystemExit("缺少依赖。请：pip install anthropic httpx")

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    raise SystemExit("ANTHROPIC_API_KEY 未设置。请：export ANTHROPIC_API_KEY=sk-ant-...")

HERE = Path(__file__).parent
LONG_PROMPT_PATH = HERE / "h6-test-prompt.txt"
RESULTS_PATH = HERE / "h6-results.jsonl"

if LONG_PROMPT_PATH.exists():
    LONG_PROMPT = LONG_PROMPT_PATH.read_text()
    print(f"使用本地 prompt 文件：{LONG_PROMPT_PATH}（{len(LONG_PROMPT)} 字符）")
else:
    LONG_PROMPT = ("这是一段用于验证 Anthropic prompt caching 字节行为的固定测试文本。" * 200)
    print(f"使用内置 prompt（{len(LONG_PROMPT)} 字符，约 {len(LONG_PROMPT)//4} token）")


class ByteLogger(httpx.Client):
    last_request_body_bytes = 0
    last_request_headers_bytes = 0

    def send(self, request, *args, **kwargs):
        body = request.content or b""
        ByteLogger.last_request_body_bytes = len(body)
        ByteLogger.last_request_headers_bytes = sum(
            len(k) + len(v) + 4 for k, v in request.headers.items()
        )
        return super().send(request, *args, **kwargs)


client = anthropic.Anthropic(api_key=API_KEY, http_client=ByteLogger())
results = []


def run_once(label, with_cache, model="claude-sonnet-4-6"):
    content_block = {"type": "text", "text": LONG_PROMPT}
    if with_cache:
        content_block["cache_control"] = {"type": "ephemeral"}
    messages = [{"role": "user", "content": [
        content_block,
        {"type": "text", "text": "请用一句话回复 ok。"}
    ]}]
    try:
        resp = client.messages.create(
            model=model,
            max_tokens=64,
            messages=messages,
        )
    except Exception as e:
        print(f"[ERR] {label}: {e}")
        return None

    body_bytes = ByteLogger.last_request_body_bytes
    headers_bytes = ByteLogger.last_request_headers_bytes
    usage = resp.usage.model_dump() if hasattr(resp.usage, "model_dump") else dict(resp.usage)
    record = {
        "label": label,
        "with_cache": with_cache,
        "model": model,
        "request_body_bytes": body_bytes,
        "request_headers_bytes": headers_bytes,
        "input_tokens": usage.get("input_tokens", 0),
        "cache_creation_input_tokens": usage.get("cache_creation_input_tokens", 0),
        "cache_read_input_tokens": usage.get("cache_read_input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
    }
    results.append(record)
    print(json.dumps(record, ensure_ascii=False))
    return record


def main():
    # 组 1：不启用 cache
    print("\n=== 组 1: 不启用 cache_control ===")
    for i in range(5):
        run_once(f"group1-no-cache-{i}", with_cache=False)
        time.sleep(1)

    # 组 2 + 3：启用 cache，首次创建 + 紧接命中
    print("\n=== 组 2+3: cache 创建 + 命中 ===")
    for i in range(5):
        run_once(f"group2-cache-creation-{i}", with_cache=True)
        time.sleep(2)
        run_once(f"group3-cache-read-{i}", with_cache=True)
        time.sleep(1)

    # 落盘
    with RESULTS_PATH.open("w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"\n已写入 {RESULTS_PATH} （{len(results)} 条记录）")

    # 分析
    def avg(records, key):
        vals = [r[key] for r in records if r]
        return sum(vals) / len(vals) if vals else 0

    g1 = [r for r in results if r["label"].startswith("group1")]
    g2 = [r for r in results if r["label"].startswith("group2")]
    g3 = [r for r in results if r["label"].startswith("group3")]

    print("\n=== 字节统计 ===")
    print(f"组 1 (no cache)          avg body bytes: {avg(g1, 'request_body_bytes'):.0f}")
    print(f"组 2 (cache_creation)    avg body bytes: {avg(g2, 'request_body_bytes'):.0f}")
    print(f"组 3 (cache_read)        avg body bytes: {avg(g3, 'request_body_bytes'):.0f}")

    if g2 and g3 and avg(g2, "request_body_bytes") > 0:
        ratio = avg(g3, "request_body_bytes") / avg(g2, "request_body_bytes")
        print(f"\n组 3 / 组 2 字节比：{ratio:.4f}")
        if ratio > 0.95:
            print("→ 情景 A 确证：cache_read 时 HTTP body 仍含完整 prompt")
            print("  报告 5A.4 '未削减字节' 论断成立")
        elif ratio < 0.05:
            print("→ 情景 B 确证：cache_read 时 HTTP body 显著缩小")
            print("  报告 5A.4 '未削减字节' 论断需撤回")
        else:
            print(f"→ 混合：cache_read 削减约 {(1-ratio)*100:.1f}% 字节")
            print("  报告需增加新假设，重新量化")

    # 验证 cache_read 是否真的触发
    g3_cache_read_count = sum(1 for r in g3 if r["cache_read_input_tokens"] > 0)
    print(f"\n组 3 中实际触发 cache_read 的次数：{g3_cache_read_count}/{len(g3)}")
    if g3_cache_read_count < len(g3):
        print("⚠️  部分组 3 调用未触发 cache_read，结果可能受污染")


if __name__ == "__main__":
    main()
