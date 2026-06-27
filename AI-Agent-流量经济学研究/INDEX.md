# AI Agent 流量经济学研究 — 索引

> **报告版本：v1.2.1（已定版）**
> **定版日期：2026-06-27（v1.2.1 应用 Codex-B Part 9 专项审稿修订）**
> 形态：内部研究报告（图表数据密集，每节挂数据源链接，留可复核接口）
> 中国 / 海外内容比例：约 1:1
> 实测：单用户低样本（48,633 次 API 调用）
> 假设：H1–H5 开放、H6 已 L2 解决
> 审稿：Codex-B 三轮对抗审稿全部应用，三审判定"修复后可发布"
> 作者：Claude（主线）+ Codex-A/A2/A3/A4（数据考古）+ Codex-B（对抗审稿）

## 引用规范（v1.1）

按 Codex-B 三审建议：

| 等级 | 可引内容 |
|---|---|
| **L1 可引** | 48,633 次 Claude Code usage token 实测、162:1、96.1% |
| **L2 可引** | H6 文献证据、AWS/GCP/Azure 云价目、EU Data Act、5 例历史结算危机、中国移动 2024 年报、AMS-IX/DE-CIX/HKIX 公开峰值、Cloudflare AI bot 占比、arXiv 三篇 |
| **L3 只作背景** | DPI 厂商行业共识、行业评论 |
| **不可作事实** | H1–H5 任何条目、全球量级具体数字、拐点年份、监管路径预测、结算重写时间表 |
| **H6 特殊措辞** | 可写"L2 协议/SDK 证据支持 Anthropic prompt caching 不削减 HTTP request body"，**不可**写"已抓包实测" |

## 文档结构

| 部分 | 文件 | 状态 | 角色 |
|---|---|---|---|
| 目录草案 v0.4 | [00-目录草案.md](00-目录草案.md) | 已确认 | Claude + Codex |
| Part 1 问题重定位 | [01-framework/01-问题重定位.md](01-framework/01-问题重定位.md) | ✅ 完成 | Claude |
| Part 2 国际 BGP 结算（资料笔记） | [02-bgp-settlement/codex-a-research-notes.md](02-bgp-settlement/codex-a-research-notes.md) | ✅ Codex-A 完成 | Codex-A |
| Part 2 国际 BGP 结算（正文） | [02-bgp-settlement/02-bgp-settlement.md](02-bgp-settlement/02-bgp-settlement.md) | ✅ 完成（合稿） | Claude |
| Part 3 公有云出向定价史（笔记） | [03-cloud-pricing/codex-a-cloud-pricing-notes.md](03-cloud-pricing/codex-a-cloud-pricing-notes.md) | ✅ Codex-A 完成 | Codex-A |
| Part 3 公有云出向定价史（正文） | [03-cloud-pricing/03-公有云定价.md](03-cloud-pricing/03-公有云定价.md) | ✅ 完成（合稿） | Claude |
| Part 4 中国互联网结算结构（正文） | [04-china-structure/04-中国结算结构.md](04-china-structure/04-中国结算结构.md) | ✅ 完成（含 Codex-A2 数据） | Claude |
| Part 4 Codex-A2 数据笔记 | [04-china-structure/codex-a2-china-data.md](04-china-structure/codex-a2-china-data.md) | ✅ 完成 | Codex-A2 |
| Part 5A 本地实测 | [05-empirical/5A-本地实测.md](05-empirical/5A-本地实测.md) | ✅ 完成 | Claude |
| Part 5B / 5C 公开观测 + 假设区 | [05-empirical/5B-公开观测.md](05-empirical/5B-公开观测.md) | ✅ 完成（含 Codex-A4 数据） | Claude + Codex-A4 |
| Part 5B Codex-A4 数据笔记 | [05-empirical/codex-a4-public-observation.md](05-empirical/codex-a4-public-observation.md) | ✅ 完成 | Codex-A4 |
| Part 6 三类利益方影响 | [06-stakeholder-impact/06-stakeholder-impact.md](06-stakeholder-impact/06-stakeholder-impact.md) | ✅ 完成 | Claude |
| Part 7 证据强度评级 | [07-evidence/07-evidence.md](07-evidence/07-evidence.md) | ✅ 完成 | Claude |
| Part 8 结论 | [08-conclusion/08-conclusion.md](08-conclusion/08-conclusion.md) | ✅ 完成 | Claude |
| **Part 9 利益方当前动作（2025-2026）** | [09-stakeholder-actions/09-利益方当前动作.md](09-stakeholder-actions/09-利益方当前动作.md) | ✅ 完成（v1.2 新增） | Claude + Codex-A5 |
| Part 9 Codex-A5 数据笔记 | [09-stakeholder-actions/codex-a5-stakeholder-actions.md](09-stakeholder-actions/codex-a5-stakeholder-actions.md) | ✅ 完成 | Codex-A5 |
| Part 9 Codex-B 专项审稿 | [07-evidence/codex-b-review-part9.md](07-evidence/codex-b-review-part9.md) | ✅ 完成（已应用） | Codex-B |
| **博客可发布版** | [博客版本-AI-Agent流量经济学.md](博客版本-AI-Agent流量经济学.md) | ✅ 完成 — **面向企业 IT + 公有云厂** + 11 张 PNG 配图 | Claude |
| 博客配图 | [博客图表/](博客图表/)（11 SVG 源文件 + 11 PNG 144 DPI） | ✅ 完成（PNG 用于发布，SVG 用于二次编辑） | Claude |
| Codex-B 对抗审稿 | [07-evidence/codex-b-review.md](07-evidence/codex-b-review.md) | ✅ 完成 | Codex-B |
| Codex-B 修订日志 | [07-evidence/codex-b-revision-log.md](07-evidence/codex-b-revision-log.md) | ✅ 应用 Tier 1+2（含一/二/三轮） | Claude |
| Codex-B 二轮审稿 | [07-evidence/codex-b-review-round2.md](07-evidence/codex-b-review-round2.md) | ✅ 完成（已应用） | Codex-B |
| Codex-B 三轮审稿（发布前） | [07-evidence/codex-b-review-round3.md](07-evidence/codex-b-review-round3.md) | ✅ 完成（已应用） | Codex-B |
| H6 抓包协议（已降为可选 L1 升级路径） | [05-empirical/H6-抓包协议.md](05-empirical/H6-抓包协议.md) | ✅ 完成（H6 已通过文献证据法解决至 L2，本协议非必需） | Claude |
| H6 实验脚本（已降为可选 L1 升级路径） | [05-empirical/h6-experiment.py](05-empirical/h6-experiment.py) | ✅ 完成（H6 已 L2 闭环，本脚本非必需） | Claude |
| **H6 文献证据法（核心）** | [05-empirical/H6-文献证据.md](05-empirical/H6-文献证据.md) | ✅ 完成 — **H6 已解决，判情景 A，L2 确证** | Codex-A3 |

## 实测数据

- 扫描脚本：[`05-empirical/scan-sessions.py`](05-empirical/scan-sessions.py)
- 实测结果：[`05-empirical/scan-summary.md`](05-empirical/scan-summary.md)
- 原始记录：[`05-empirical/scan-result.jsonl`](05-empirical/scan-result.jsonl)（48,633 行）

## 关键发现摘要（已经 Codex-B 两轮审稿修订）

1. **本地实测 L1**（已完成）：
   - 单用户、48,633 次 API 调用、横跨 15 项目目录
   - 上行 / 下行 **usage token** 比 = **162 : 1**（总体加权）
   - 上行 usage token 中 **96.1%** 计入 prompt cache_read 字段
   - **注**：以上为 Anthropic API usage token 计量；网络字节比未抓包，留 H6

2. **结构性论断 L2-L3**（已挂源）：
   - 现有三套结算体系（公有云入向免费 / 国际 BGP 对等 / 中国行政互联）建立在"下行驱动"前提之上
   - 中国移动 2024 国际传输带宽 **164 Tbps、330 POP**（[年报](https://www.chinamobileltd.com/en/ir/reports/ar2024.pdf)）
   - EU Data Act 已是首次以法律形式监管 egress fee（[2023/2854](https://data.europa.eu/eli/reg/2023/2854/oj)，2024-01-11 生效 / 2027-01-12 禁止 switching charges）
   - AMS-IX 2026 daily peak in/out **13.308/13.281 Tb/s 几乎完美对称**（差异 0.2%）——构成 H1 弱反证
   - Cloudflare 2024-06 top 1M 站点 **38.73% 被 AI bot 访问**，AI bot 流量 2025 年占 HTML requests 4.2%
   - arXiv 三篇相关论文（[2504.10688](https://arxiv.org/abs/2504.10688)、[2510.11269](https://arxiv.org/abs/2510.11269)、[2509.06515](https://arxiv.org/abs/2509.06515)）

3. **假设 H1–H6 进展**：
   - H1：BGP 层流量方向反转 — 待验证
   - H2：公有云入向免费可持续性拐点 — 待验证
   - H3：95th percentile 在 AI workload 下的失真程度 — 待验证
   - H4：中国监管路径偏向"算力本地化（鼓励/引导）" — 待验证
   - H5：业界 10:1–30:1 估算是否仍适用于 Agent workload — 待验证
   - ~~H6：Anthropic prompt caching 是否削减客户端→服务端字节~~ — **已通过文献证据法解决：判情景 A，L2 确证 prompt caching 不削减字节**（[H6-文献证据](05-empirical/H6-文献证据.md)）

## 角色分工记录（最终）

| 角色 | 承担 | 状态 |
|---|---|---|
| Claude（主线） | 框架、实测、合稿、一致性校验、Part 1–8 主稿撰写 | ✅ 完成 |
| Codex-A（数据考古） | Part 2 国际 BGP 资料、Part 3 公有云定价资料 | ✅ 完成 |
| Codex-A2（中国数据） | Part 4 中国数据补充 | ✅ 完成（关键数据已挂；MIIT/CAICT/联通待续） |
| Codex-A3（H6 文献证据） | H6 假设的文档与 SDK 源码证据 | ✅ 完成（H6 升 L2） |
| Codex-A4（公开观测） | Part 5B Cloudflare/IXP/Sandvine/学术论文 | ✅ 完成 |
| Codex-B（对抗审稿） | 一/二/三轮审稿 | ✅ 完成（三轮全部应用修订） |

## Codex-B 审稿结论（三轮）

- **一轮**：发现 H6 事实化、AS54321、占全球 0.3%-3%、强制本地化、token/字节混用等高严重度问题
- **二轮**：判定"可内部流转"，发现 H1-H6 计数不一致、Part 1 H6 残留等中等问题
- **三轮（发布前）**：判定 **修复后可发布**，关键修复项已全部应用

> 三轮判定原文："修复后引用规范：L1 只引 48,633 次 Claude Code usage token 实测、162:1、96.1%；L2 可引 H6 文献证据、云价目、Data Act、历史案例、中国移动年报；L3 只作背景；H1-H5、全球量级、拐点年份、监管路径、结算重写不得作事实。H6 可写'L2 协议/SDK 证据支持 Anthropic prompt caching 不削减HTTP request body'，不能写'已抓包实测'。"

三轮全部修订已应用（详见 [修订日志](07-evidence/codex-b-revision-log.md)）。

## 版本历史

| 版本 | 日期 | 状态 | 主要变化 |
|---|---|---|---|
| v1.0 | 2026-06-27 | 三审应用完成，标"可对外引用" | Part 1–8 全部完成，Codex-B 三轮审稿全部应用，H6 升 L2 |
| v1.1 | 2026-06-27 | 完成 | 新增 Part 5B 公开观测（Codex-A4 数据），Part 5 闭环 |
| v1.2 | 2026-06-27 | 完成 | 新增 Part 9 利益方当前动作 2025-2026（Codex-A5 数据 + Claude 自审） |
| **v1.2.1** | **2026-06-27** | **已定版** | **应用 Codex-B Part 9 专项审稿修订（含关键修订：发现 DE-CIX AI-IX 产品，更新"IXP 无 AI 专项"论断）** |

## 定版声明

**AI Agent 流量经济学研究 v1.2.1 已定版**。所有正文文档（Part 1–9 + 5A + 5B + H6 文献证据）均挂载可追溯的公开数据源；所有可能被引用的论断均按 L1–L4 四级评级标注；H1–H5 五项开放假设各自给出验证方法与反证条件；H6 通过文献证据法 L2 解决；三轮对抗审稿 + Part 9 专项审稿 + Claude 自审全部应用。可作为内部研究报告对外引用（按上述引用规范）。

## Part 9 关键更新（v1.2.1 修订）

Codex-B Part 9 专项审稿发现关键事实遗漏：**DE-CIX AI-IX** 是 [DE-CIX 官网](https://www.de-cix.net/en/services/ai-ix) 公开的 AI 流量专用 IXP 产品——这修订了原稿"IXP 完全无 AI 专项产品"的强论断。准确判断变为：

> **AI 专项 IXP 产品开始出现，但密度极低**——DE-CIX AI-IX 是本研究找到的唯一显性案例，其他 IXP（AMS-IX、LINX、HKIX、Equinix）仍以通用容量扩张为主。

## Part 9 核心论断（v1.2 新增）

> 在公开层面（12 个月 2025-06 至 2026-06）**没有任何利益方推出"AI 流量费"新计费项**，但全部公开动作落到**四层**——容量价格、跨云私网、协议降本、底层路由。**动作密度排名**：OpenAI/Stargate > Google/GCP > Anthropic > 美国/EU 监管 > AWS > Azure > 中国侧 > IXP/ISP。**最少公开动作的是 ISP/IXP**——可能是承载者未感知、流量绕开公网、或内部动作未公开，无法定论。
>
> 关键数据点：AWS ML Capacity Blocks 6 月内复合涨 ~38%（GPU 容量价不是 egress 价）；OpenAI Stargate 7GW、$400B 三年 + Oracle $300B 五年；Anthropic 与 Google 100 万 TPU、1GW+；Google Blue-Raman 海缆 218 Tbps（可扩至 400 Tbps）；中国 ~2 万亿元算力网格规划目标 2028 单一计算网格。
