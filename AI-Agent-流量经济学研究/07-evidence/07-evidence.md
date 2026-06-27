# 第七部分　证据强度评级与开放问题

> 内部研究报告 · 草稿 v0.1
>
> 本部分是研究的"诚实账本"：把全文论断逐条按证据强度评级，明示哪些可信、哪些仍是推断，并列出长期跟踪指标与复现方法。

## 7.1 四级证据强度评级体系

| 级别 | 标记 | 定义 | 在报告中如何呈现 |
|---|---|---|---|
| L1 | **【已实测】** | 本研究自行采集并可复现的数据 | 直接挂脚本与原始数据 |
| L2 | **【已发布数据】** | 官方/学术/行业机构公开发表的可追溯数据 | 挂 URL，附年份与原数值 |
| L3 | **【行业共识】** | 多源一致但无单一权威统计来源 | 多源交叉引用，注明"共识" |
| L4 | **【推断 / 假设】** | 由 L1–L3 外推，或基于结构性逻辑推理 | 显式标"假设"，留至 7.3 开放问题 |

**评级使用原则**：

- 报告中任何"AI Agent 流量正在/将会/已经..."的陈述句，必须挂载相应级别。
- L4 论断**不允许**伪装为 L1–L3，必须显式承认推断成分。
- L3 与 L4 的论断需要在结论与对策中被独立列出"如果不成立，将如何"的反事实分析。

## 7.2 全文核心论断的证据强度评级

按章节顺序列出本研究所有可能被引用的核心论断及其评级：

### 来自 Part 1（问题重定位）

| 论断 | 证据强度 | 依据 |
|---|---|---|
| AI Agent 客户的真实流量结构是大量上行 + 少量下行 | L1 | 本研究实测 48,633 调用 |
| 三套结算体系建立在"下行驱动"假设上 | L3 | 公有云定价范式、BGP peering ratio 概念 |
| AI Agent 触发的是结算模型问题而非带宽容量问题 | L4 | 由 L1+L3 推断 |

### 来自 Part 2（国际 BGP 结算）

| 论断 | 证据强度 | 依据 |
|---|---|---|
| 95th percentile 算法的工程定义 | L2 | [DrPeering](https://drpeering.net/white-papers/Internet-Service-Providers-And-Peering.html)、[Burstable billing](https://en.wikipedia.org/wiki/Burstable_billing) |
| 95th 三种 in/out 口径（max / 分别算 / sum） | L2 | 同上，附 InterNAP、TW Telecom、HopOne 样本 |
| Tier 1 / Tier 2 定义 | L2 | 维基百科条目 |
| PeeringDB 无 Tier1/Tier2 原生字段，需 CAIDA AS Rank 二次分类 | L2 | [PeeringDB Docs](https://docs.peeringdb.com/) |
| 历史结算危机 5 例（Comcast/BitTorrent、Level3/Netflix、Cogent/Verizon、Free/YouTube、SK Broadband/Netflix） | L2 | FCC 文件、Reuters、Wired、ARCEP 公告（详见 Codex-A 笔记） |
| BEREC 2017 报告认定生态可自适应 | L2 | [BEREC IP Interconnection Report](https://www.berec.europa.eu/en/document-categories/berec/reports/berec-report-on-ip-interconnection-practices-in-the-context-of-net-neutrality) |
| AI 时代 transit 价格出现拐点 | **L4** | 公开价格曲线尚未证实，Codex-A 明确承认 |
| 海缆容量数据（2Africa 180Tbps、MAREA 200Tbps 等） | L2 | 各项目官方公告 |

### 来自 Part 3（公有云定价）

> Codex-A 待补，本评级待 Part 3 完成后填充

### 来自 Part 4（中国结算）

| 论断 | 证据强度 | 依据 |
|---|---|---|
| 三大运营商互联结构与南北互联历史 | L2 | 工信部历年文件、公开报道 |
| BGP 多线 vs 单线带宽溢价 4–8× | L3 | 公开 IDC 报价单与运营商集采公告，难单一定价 |
| 跨境带宽配额管制存在 | L2 | 监管文件 |
| 跨境出向价差 5–10× 量级 | L3 | 各云价目页对照（待 Part 3 Codex-A 完成验证） |
| 国内公有云入向同样免费 | L2 | 各厂官方价目页 |
| 中国监管路径与欧盟"公平贡献费"不同 | **L4** | 结构性推断，无既成事实 |
| 推理算力本地化是政策最可能回应路径 | **L4** | 由"东数西算"政策外推 |

### 来自 Part 5（实测）

| 论断 | 证据强度 | 依据 |
|---|---|---|
| 编码型 Agent 实测 **usage token** 上下行比 162 : 1（总体）、386 : 1（中位数） | **L1** | [scan-summary.md](../05-empirical/scan-summary.md) |
| 上行 usage token 中 96.1% 计入 prompt cache_read 字段 | **L1** | 同上 |
| 小模型/流水线节点角色比例更极端（Haiku 281:1） | L1 | 同上 |
| cache_read 字节仍需客户端→服务端完整提交 HTTP body | **L2** | [H6-文献证据](../05-empirical/H6-文献证据.md) — 官方文档 + SDK 源码 |
| token 比 ≈ 字节比 | **L4** | 未实测（已从 L3 降级） |
| 业界估算（10:1–30:1）是否适用于 Agent workload | **L4** | 口径不同不可直接对比，已从 L3 降级，移入 H5 |
| 单用户样本不能外推到所有 workload | L1（限制声明） | 自承样本局限 |

### 来自 Part 6（利益方影响）

| 论断 | 证据强度 | 依据 |
|---|---|---|
| 家宽上行从"用不到"变"经常满载" | L4 | 由 L1 实测 + 家宽零售套餐结构推断 |
| 企业出口带宽采购模型需重估 | L4 | 由 L1 实测外推到团队规模 |
| 全球 Agent 日上行总量 50–500 PB | L4 | 由 L1 + 用户数公开估算外推 |
| ~~当前 AI 流量占全球互联网 0.3%–3%~~ **论断撤回** | — | 分子分母口径不一致（input token 估算 vs 全网双向带宽），经 Codex-B 审稿不构成有效比较 |
| 公有云入向免费的财务可持续性面临拐点 | L4 | 推断 |
| IXP 流量结构反转 | L4 | 推断（公开数据未确认） |
| 中国三大运营商既是网络方又是云方的角色重叠是结构性优势 | L3 | 行业共识 |

## 7.3 开放假设清单（保留供后续验证）

按 Part 1.5 与用户决策，本研究保留以下假设作为"待数据验证"留存，不在结论中下断言：

### 假设 H1：BGP 层流量方向反转

> 当 AI Agent 流量足够大时，全球 IXP 与对等链路上将出现"用户 ISP → 推理服务商"方向占主导的流量结构反转。

**验证方法**：

- 跟踪 DE-CIX Frankfurt、AMS-IX、HKIX 等大型 IXP 公开 ASN 级流量曲线
- 跟踪 OpenAI、Anthropic、Google AI 推理服务 ASN 的对等关系变化（**注**：具体 ASN 须通过 DNS / traceroute / RPKI / PeeringDB 对推理 API 域名实测得出，本研究尚未建立这一映射）
- 跟踪 PeeringDB 中推理服务商网络的 traffic ratio 字段（自报字段）

**反证条件**：若上述指标持续显示"内容方→用户方"主导（如视频、CDN 流量增长仍快于 AI 上行），则假设不成立。

### 假设 H2：公有云入向免费可持续性拐点

> 当 AI Agent 类客户在公有云总流量中占比超过某阈值（推测 10%–20%），入向免费策略将面临财务调整，可能出现"AI 流量专项定价"。

**验证方法**：

- 跟踪 AWS / GCP / Azure / 阿里云的价目页历史变化，特别留意是否新增 inbound 计费维度
- 跟踪云厂财报中"网络费用"与"网络收入"细分（如有披露）
- 跟踪推理服务商财报中"基础设施成本"占比

**反证条件**：若 5 年内三大公有云未推出 AI 流量专项定价，且推理服务商内部成本结构稳定，则假设不成立。

### 假设 H3：95th percentile 计费在 AI workload 下失真

> AI Agent 流量的"持续吞吐 + 上下行不对称"特征，会让 95th percentile 计费在某些链路上产生显著失真——上行峰值与下行峰值不再同步。

**验证方法**：

- 采集 ISP 公开的链路利用率曲线（如有）
- 对自有出口的企业进行 1 分钟粒度抓包，按 in/out 分别算 95th
- 与 BGP4/CMTS 设备的 SNMP 历史数据对比

**反证条件**：若实测上行与下行 95th 差异 < 30%，则失真不显著。

### 假设 H4：中国监管路径偏向"算力本地化"

> 在 AI Agent 跨境上行流量持续增长的压力下，中国监管层更可能通过"东数西算""算力网络"等工程，**鼓励并引导**推理算力境内部署（强度可能逐步抬升，但不一定走到"强制"），而非引入"公平贡献费"类机制。

**验证方法**：

- 跟踪工信部、网信办、发改委关于算力网络的政策文件
- 跟踪三大运营商云业务（移动云、天翼云、联通云）AI 推理收入占比
- 跟踪国内推理服务商（DeepSeek、智谱、月之暗面、阿里通义、字节豆包）region 部署变化

**反证条件**：若监管层公开讨论或落地某种"内容方向 ISP 付费"机制，假设不成立。

### 假设 H5：业界 10:1–30:1 估算是否仍适用于 Agent workload

> a16z、SemiAnalysis 等公开估算的 input:output 比例（10:1–30:1）多来自 chatbot 时代假设，**可能**对 Agent workload 显著低估，但单一数字直除不构成"系统性低估 X 倍"的结论——业界估算的 token 口径（是否包含 cache_read、是否按 usage token / 网络字节）未明示。

**单用户单工具样本已观察到差异**（L1），但同口径扩样需要：

- 跨用户（10+ 用户）、跨 workload（编码、浏览器、RAG、多模态）的同口径 usage token 数据
- 跨厂商（OpenAI、Google、本地推理）的对照
- **重点**：拿到业界估算原作者的口径定义（是否包含 cache_read），否则无法做 apples-to-apples 对比

### 假设 H6：Anthropic prompt caching 是否削减客户端上行字节 — **已解决 → L2 确证**

> 报告核心论断之一"96.1% 上行 usage token 是 prompt cache_read"在 token 层 L1 已确认。本节探讨"这一现象在网络字节层面意味着什么"。

**判定**：**情景 A 成立**——cache_read 场景下客户端仍需要完整提交 prompt 内容；prompt caching **不削减**客户端→服务端 HTTP 字节。

**证据来源**（详见 [H6-文献证据.md](../05-empirical/H6-文献证据.md)）：

1. **L2 官方文档**：[Anthropic Prompt Caching 文档](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching) "How automatic prefix checking works" 描述服务端通过 cumulative prefix hashing 识别 cache 匹配——该机制要求客户端将相关 prefix 提交到服务端才能完成 hash（文档未逐字写"必须发送 full prompt"，但 hash 机制 + Messages API 无状态语义共同支持此推断）
2. **L2 SDK 源码**：[anthropic-sdk-python messages.create](https://github.com/anthropics/anthropic-sdk-python/blob/main/src/anthropic/resources/messages/messages.py) 完整 JSON 序列化整个 messages / system / tools 数组，无任何"cache hit 时省略字段"的优化分支
3. **L2 协议层**：`cache_control` schema 只有 `type: "ephemeral"` + `ttl` 两字段，无 cache key / reference 语义
4. **反例验证**：OpenAI 的 [`previous_response_id`](https://developers.openai.com/api/docs/guides/conversation-state) 是真正字节削减的对照，但 Anthropic 当前未提供等价协议

**结论**：H6 不需要抓包实测即可在 L2 级别确证。[mitmproxy 抓包脚本](../05-empirical/h6-experiment.py) 仍保留为可选升级路径（L2 → L1），但不再是必需。

## 7.4 长期跟踪指标清单

如果团队/读者要持续跟踪本研究主题，建议定期采集以下指标：

| 指标类别 | 具体指标 | 数据源 | 更新频率 |
|---|---|---|---|
| 流量观测 | Cloudflare Radar **AI crawler / verified bot** 流量占比（**注意口径**：是 web crawler 和浏览器型 user-action bot，**不是 LLM API 调用本身的字节**——这两者不能混用） | [radar.cloudflare.com/traffic/verified-bots](https://radar.cloudflare.com/traffic/verified-bots)、[Year in Review 2025](https://blog.cloudflare.com/radar-2025-year-in-review/) | 实时 |
| IXP 统计 | DE-CIX / AMS-IX / HKIX 峰值流量与方向 | 各 IXP 公开页 | 月 |
| 海缆容量 | TeleGeography Submarine Cable Map 新增项目 | [submarinecablemap.com](https://www.submarinecablemap.com/) | 季 |
| 公有云价目 | AWS / GCP / Azure / 阿里云出向价格 | 各官方价目页 | 月（自动监测） |
| 中国监管 | 工信部通信业统计公报（月度 / 年度） | [miit.gov.cn 运行监测 通信业](https://www.miit.gov.cn/gxsj/tjfx/txy/) **栏目首页，需 Codex-A2 抓最近一期具体 PDF 链接** | 月 |
| 中国白皮书 | 信通院云计算 / 数据中心 / 算力网络白皮书 | [caict.ac.cn](http://www.caict.ac.cn/) **首页，需 Codex-A2 定位最新白皮书 PDF** | 年 |
| 运营商财报 | 三大运营商 ICT/云/IDC 业务收入 | A股/港股年报 | 半年 |
| 推理服务商 | OpenAI / Anthropic 公开容量信息 | 官方公告、Bedrock/Vertex region 列表 | 不定 |
| BGP 拓扑 | RouteViews / RIPE RIS / CAIDA AS Rank | 各源 | 实时/日 |
| 终端测量 | M-Lab NDT、RIPE Atlas、APNIC Labs | 各源 | 实时/月 |
| 政策动向 | BEREC、欧盟、FCC、工信部公开咨询 | 各机构网站 | 不定 |

## 7.5 复现本研究的最小数据采集方法

任何团队要在自有环境复现本研究的核心实测，需要以下最小数据集：

### 7.5.1 单用户层级（与本研究 Part 5A 一致）

- 从 `~/.claude/projects/` 或同等的本地会话日志中提取 token usage
- 运行 [scan-sessions.py](../05-empirical/scan-sessions.py)（约 10 行修改即可适配 OpenAI Codex、Cursor、其他工具的本地日志）
- 输出每模型、每项目、每分位的上下行比例
- **最小样本**：1000 次以上 API 调用即可得到稳定分布

### 7.5.2 团队层级

- 部署透明 HTTPS 代理（mitmproxy + 内部 CA）作为 LLM API 出口
- 按用户、按项目、按 workload 标签记录 HTTP 请求/响应字节
- 采样粒度 1 分钟
- 输出每用户 / 每天的上行字节、下行字节、调用次数
- **建议样本**：100+ 用户 × 30+ 天

### 7.5.3 网络出口层级

- 边界路由器 SNMP / NetFlow / IPFIX 采集
- 按目标 ASN（OpenAI、Anthropic、Google AI）分别统计上下行
- 输出每 5 分钟粒度的 in/out 带宽时间序列
- 用于 95th percentile 失真验证

### 7.5.4 公开数据采集

- Cloudflare Radar API 抓取 AI crawler / verified bot 类别月度趋势（口径限定：crawler，不是 LLM API）
- PeeringDB API 抓取重点 ASN 的对等关系变化
- RouteViews / RIPE RIS 抓取 BGP 前缀公告变化

## 7.6 本部分小结

- 研究全文论断按四级评级（已实测 / 已发布 / 共识 / 推断）严格区分
- 核心已实测发现：**编码型 Agent 上行 / 下行 usage token 比 162:1，96.1% 上行 usage token 计入 cache_read；其字节仍走 HTTP body 已 L2 文献证据确证**
- 假设格局：**H1–H5 五项待验证 + H6 一项已解决**（H6 通过文献证据法升 L2）。逐项给出验证方法与反证条件
- 长期跟踪指标 11 类，覆盖流量、容量、定价、监管、技术拓扑
- 复现方法分单用户、团队、网络出口、公开数据四级，最小样本明示

**研究的诚实底线**：本研究不冒充已经知道答案。**H6 已通过文献证据法升级至 L2 已确证**（详见 [H6-文献证据.md](../05-empirical/H6-文献证据.md)）；H1–H5 仍承认目前公开数据不足以下确定结论。后续验证工作应优先围绕剩余 5 个假设的数据采集展开。

---

**下一节衔接**：Part 8 给出基于已确证部分的结论，把开放假设留作"风险与机会"清单。
