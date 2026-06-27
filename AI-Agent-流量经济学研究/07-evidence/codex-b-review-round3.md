# Codex-B 三审审稿

## A. H6 升级后的一致性

- `05-empirical/5A-本地实测.md:29,110`：仍写 cache_read 字节判断是 L4、须抓包验证，和 `:61,115,161` 的 L2 已解决冲突。高｜建议：删“开放假设/H6 留存”，改“cache_read 是否提交已升 L2；token→wire bytes 放大仍 L4”。
- `08-conclusion/08-conclusion.md:14,123`、`INDEX.md:44`：仍称 H6 留存/抓包协议已就绪。高｜建议：改“未抓包的是网络字节比与编码层放大，不是 H6 本身”。
- `07-evidence/07-evidence.md:218`、`08-conclusion/08-conclusion.md:99`：仍用“6 个开放假设/六项假设”。中｜建议：统一为“H1-H5 五项待验证 + H6 一项已解决”。
- `07-evidence/07-evidence.md:157`：“文档明示必须完整提交”略强，H6 文献正文承认无逐字 must contain full prompt。低｜建议：改“prefix hash 机制 + SDK schema 支持该推断”。

## B. Part 2 / Part 3 首次审稿

- `02-bgp-settlement/02-bgp-settlement.md:49`：把 5-50 Tbps L4 情景上界写成“目前量级”，与 Part 6/8 冲突。高｜建议：改“在 5-50 Tbps 情景上界下仍未必触发”，或删除。
- `02-bgp-settlement/02-bgp-settlement.md:200-202`：称 sum 口径“合约采用比例不高”、AI Agent“同时具备”两条件，缺公开合同/ASN 实测。高｜建议：降 L4，沿用 Part 8“可能具备，本研究没有结论”。
- `02-bgp-settlement/02-bgp-settlement.md:115`：2Africa 仍写“2025 Q4 预计投产”，已过期。中｜建议：更新为“核心系统已完成/分支状态待核”或发布前重核。
- `02-bgp-settlement/02-bgp-settlement.md:202`：“韩国公平贡献费立法”易误读为已立法。中｜建议：改“网络使用费法案/政策争议”。
- `03-cloud-pricing/03-公有云定价.md:187`：Part 2 说近年数据缺失，却用 `$0.5/Mbps·月` 比较。高｜建议：删数字。
- `03-cloud-pricing/03-公有云定价.md:146`：挑战者存在“间接证明商业溢价”逻辑过强。中｜建议：改“支持商业溢价可能存在，不能证明比例”。
- `03-cloud-pricing/03-公有云定价.md:154-162,222`：中国云“完全跟随出向阶梯”过强。中｜建议：改“入向免费类似；出向按带宽/流量/线路多模式，需中国站价目复核”。
- `03-cloud-pricing/03-公有云定价.md:97-99`：Data Act 日期不精确，“反垄断议题”偏强。低｜建议：补 2024-01-11 生效、2025-09-12 适用、2027-01-12 禁止 switching charges；改“竞争/锁定议题”。

## C. Codex-A2 数据整合一致性

- AS37963 / AS132203 / AS136907 / AS55990：正文只在 Part 4 使用，注册名与 A2 笔记一致。无｜建议：若 Part 2/6 后续引用，复用 Part 4 表格口径。
- `04-china-structure/04-中国结算结构.md:178-180`、`INDEX.md:48`：中国移动 164 Tbps / 330 POP 一致，但 Part 2/6 未吸收。低｜建议：Part 2 海缆表后或 Part 6 中国运营商段补交叉引用。
- `04-china-structure/04-中国结算结构.md:174`：移动云 RMB 100.4B 只在 Part 4 出现，Part 6/8 未用。低｜建议：若支撑“运营商既是云方又是网络方”，Part 6 加该数并标天翼云/联通云待补。

## D. 跨文档矩阵验证

- 162:1：Part 1/5A/7/8/INDEX 数值一致，均限定 usage token；问题仅在 8/INDEX 把“未抓包”误挂到 H6。中｜建议：按 A 节修。
- 96.1% cache_read：数值一致。`07-evidence.md:217` 的“cache 重传”可能被误读成 L1 抓包。低｜建议：改“96.1% usage token 计入 cache_read；字节未削减为 L2 文献证据”。
- 中国移动 164 Tbps：Part 4 与 INDEX 一致；Part 2/6 缺引用。低｜建议：按 C 节补。

## E. 发布门槛判定

当前版未达“内部研究报告 v1.0 对外引用”门槛。必须修复：A 节高/中项；B 节 5-50 Tbps、AI Agent 同时具备两条件、TeleGeography `$0.5/Mbps·月`、中国云“完全跟随”。

修复后引用规范：L1 只引 48,633 次 Claude Code usage token 实测、162:1、96.1%；L2 可引 H6 文献证据、云价目、Data Act、历史案例、中国移动年报；L3 只作背景；H1-H5、全球量级、拐点年份、监管路径、结算重写不得作事实。H6 可写“L2 协议/SDK 证据支持 Anthropic prompt caching 不削减HTTP request body”，不能写“已抓包实测”。

**发布判定：修复后可发布。**
