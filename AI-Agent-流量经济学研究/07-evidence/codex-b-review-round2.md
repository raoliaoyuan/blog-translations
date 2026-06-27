# Codex-B 二轮审稿

## 已到位

- usage token / 网络字节在 5A、scan-summary、Part 8 已基本分离；162:1 与 96.1% 限定为 Anthropic usage token，字节层改入 H6。
- “业界系统性低估 5–16 倍”已降为 H5；H5 主体合理，强调同口径扩样。
- Bedrock/direct/Azure/Vertex 已分写；“0.3%–3% 全球占比”撤回；2026–2028 改为“数年/动态跟踪”。
- “强制本地化”大多改为“鼓励/引导”；AI crawler 与 LLM API 已分口径；Part 4 对 AS、直联点、价差已加 caveat。

## 未到位 / 部分到位

- `01-framework:73`：“HTTP 请求体仍需携带完整提示内容……故字节层面的上行成本未减少。”仍把 H6 写成事实。建议改：“若 cache_read 仍需完整提交 prompt，则字节层上行成本可能未减少；待抓包。”
- `01-framework:76`：“Anthropic……主要 region 集中在 us-west-2、us-east-1、eu-central-1；OpenAI……主要在 us-east、us-west；Google……集中在 us-central1。”仍过细且未证。建议用 Part 6 口径：direct API region/ASN 不公开，多云多区域，关键仅保留“中国大陆无公开 region”。
- `07-evidence:98`：“OpenAI（AS54321）”仍残留，与 Part 6 冲突。建议删除具体 AS，改“待 DNS/traceroute/RPKI/PeeringDB 实测”。
- `04-china-structure:99`：“受跨境出向百倍价差的影响”又把不同口径合并。建议改“受跨境按量高溢价、专线高价与配额约束影响”。
- H6 已加入，但 `07-evidence:218,222`、`08-conclusion:96,128`仍写“五项/H1–H5/5 个”。建议统一为“六项/H1–H6”。
- H5 主文合理，但 `07-evidence:72`、`08-conclusion:104`仍以“系统性低估”命名。建议改“是否低估/是否不适用 Agent workload”。

## 新引入风险

- `06-stakeholder-impact:58`：“1995 年以来家宽体验侧第一次出现的方向反转”缺证且过强；建议改“可能成为少见的上行体验瓶颈”。
- `08-conclusion:7` 称“三条已确证结论（L1+L2）”，但 `08:29` 的集中度、不可绕开性仍需实测。建议改“已确证事实与结构性推断”。
- `08-conclusion:120`“强烈信号”偏外宣；建议改“值得跟踪的信号”。
- `06:108` 与 `06:167` 相差 1000×；结论中不宜把 5–50 Tbps 写成“当前量级”，只能写“情景上界”。

## 可发布判断

当前版比上一轮收敛，可内部流转；但不建议作为“可对外引用”的研究报告发布。发布前至少修掉 Part 1 的 H6 事实化、Part 7 的 AS54321、H1–H6 计数不一致，以及 Part 6/8 强结论。修复后，对外引用限于 L1/L2；H1–H6 必须作为开放假设。
