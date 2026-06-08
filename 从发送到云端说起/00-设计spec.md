# 设计 Spec：《从「发送到云端」说起 —— AI 产业四层棋局（中美对照）》

- 日期：2026-06-04
- 作者：roger
- 状态：已与用户对齐，待用户审阅本 spec

## 一、目标与定位

写一篇**深度产业分析长文**，以 Claude Code 里不起眼的「Send to cloud」按钮为切入口，逐步分析全行业趋势，覆盖 AI 产业栈的**四层**：

1. **芯片层**（算力硅）
2. **云计算层**（数据中心 / 云平台 / Agent 托管基础设施）
3. **LLM 层**（前沿模型提供商）
4. **Agent 入口 / 运行时层**（离用户最近的产品与编排层）

每一层都**同时列出美国与中国的代表性提供商**，讲清三类关系：

- **技术 / 供货关系**（谁给谁供芯片、跑在谁的云上、谁集成谁的模型）
- **投资 / 股权关系**（谁投了谁、金额、占股、长期承诺）
- **竞争关系**（供货方/投资方同时在产品层与被投/客户竞争的"三重身份"）

## 二、硬性要求

1. **来源核查标准：官方一手优先 + 逐条验活。**
   - 优先级：官方公告 / SEC 文件 / 一手财报 > 主流权威媒体（路透、彭博、FT、The Information 等）。
   - 所有引用在**正文内嵌可点击链接** `[锚文字](url)`，锚文字用中文。
   - **每个链接最终由 Claude 用 `curl`/WebFetch 验活**（HTTP 可访问、内容对得上）；验证失败的换源或显式标注。
2. **时效声明**：投资额、产能、份额等数字以 **2026-06-01 前后**公开信息为准，文末加复核声明。无官方出处的论断标注为"结构性推断"。
3. **广度精选 + 深度展开**：每层每国挑 5–8 家头部玩家（不铺长尾），但每家的关系与投资逐笔讲透。
4. **四层覆盖矩阵（必做）**：对每一家主要厂商，明确标出它**覆盖了四层中的哪几层**，并且**每一层都写出所用的具体产品名**（而非只打勾）。
   - 例：Google = 芯片(TPU) / 云(Google Cloud) / LLM(Gemini, DeepMind) / Agent(Jules、Vertex AI Agent Builder)。
   - 例：OpenAI = 芯片(—，仅传闻自研) / 云(—，无自有云) / LLM(GPT 系列) / Agent(ChatGPT、Codex)。
   - 例：Anthropic = 芯片(—) / 云(—) / LLM(Claude) / Agent(Claude Code、含 on the web)。
   - 矩阵以**表格**形式进入正文（中美各一张，或合并一张并标注国别），每个单元格填具体产品名或"—"。
   - 正文据此展开"全栈自有 vs 被夹在中间"的结构性判断（对标范文图 7）。

## 三、厂商清单（已确认）

### 芯片层
- 美国：Nvidia、AMD、Google TPU、AWS Trainium/Inferentia、Microsoft Maia、Broadcom、Marvell
- 中国：华为昇腾、寒武纪、壁仞、摩尔线程、燧原、阿里平头哥、百度昆仑芯

### 云计算层
- 美国：AWS、Azure、Google Cloud、Oracle、CoreWeave
- 中国：阿里云、华为云、腾讯云、火山引擎、百度智能云

### LLM 层
- 美国：OpenAI、Anthropic、Google DeepMind、Meta、xAI
- 中国：DeepSeek、阿里通义千问、智谱、月之暗面（Kimi）、MiniMax、字节豆包、百度文心

### Agent 入口 / 运行时层
- 美国：Claude Code（含 on the web）、OpenAI Codex、Google Jules、Cursor、GitHub Copilot、AWS Bedrock AgentCore、Azure AI Foundry Agent Service
- 中国：通义灵码、文心快码、Trae（字节）、CodeBuddy（腾讯）、各家 Agent 托管平台

> 用户已确认清单，本轮不强制纳入 SK Hynix/三星/台积电/Groq/Cerebras 等；如复核中发现关系网必须提及，可在正文以一句话带过并附链接。

### 四层覆盖矩阵骨架（子代理需逐格填具体产品名，"—"表示不覆盖）

**美国主要厂商：**

| 厂商 | 芯片 | 云 | LLM | Agent 入口/运行时 |
|---|---|---|---|---|
| Google/Alphabet | TPU | Google Cloud | Gemini (DeepMind) | Jules、Vertex AI Agent Builder、Gemini CLI |
| Amazon/AWS | Trainium / Inferentia | AWS | Nova | Bedrock AgentCore、Q Developer |
| Microsoft | Maia / Cobalt | Azure | MAI / Phi | Copilot、Foundry Agent Service |
| Nvidia | GPU (CUDA) | DGX Cloud | (—/Nemotron) | (—) |
| OpenAI | (—,传闻自研) | (—) | GPT 系列 | ChatGPT、Codex |
| Anthropic | (—) | (—) | Claude | Claude Code (含 on the web) |
| Meta | MTIA | (—) | Llama | (待核) |
| xAI | (—) | Colossus 自建 | Grok | (待核) |
| Oracle | (—) | OCI | (—) | (—) |

**中国主要厂商：**

| 厂商 | 芯片 | 云 | LLM | Agent 入口/运行时 |
|---|---|---|---|---|
| 阿里巴巴 | 平头哥(含光/PPU) | 阿里云 | 通义千问 | 通义灵码 |
| 华为 | 昇腾 | 华为云 | 盘古 | (待核) |
| 百度 | 昆仑芯 | 百度智能云 | 文心 | 文心快码/Comate |
| 腾讯 | (自研/投资待核) | 腾讯云 | 混元 | CodeBuddy |
| 字节跳动 | (自研待核) | 火山引擎 | 豆包 | Trae |

> 上表为骨架，括号/"待核"处由子代理联网核实并填具体产品名+链接；不覆盖的层填"—"。

## 四、文章结构

1. 引子：从「Send to cloud」按钮切入
2. 范式转变：云端异步执行是什么、为什么（解绑在场 → 调度 Agent 队列）
3. 四层框架的提出 + **四层覆盖矩阵**（中美各一张表，每格写具体产品）：芯片 → 云 → LLM → Agent 入口
4. 第一层 · 芯片（中美对照 + 关系 + 投资 + 管制背景）
5. 第二层 · 云（中美对照）
6. 第三层 · LLM（中美对照）
7. 第四层 · Agent 入口 / 运行时（中美对照）
8. 错综关系网：供货 × 持股 × 竞争的三角；中美各自的"杠铃"与"被夹在中间"判断；跨国交织（出口管制、自研替代）
9. 结语 + 一手追踪信号 + 事实时效声明
10. 附录（可选）：分层分国 厂商-关系-来源 对照表

配图沿用范文"图 N + 图注"形式，本轮只写图注、不画图。

## 五、委派工作流（方案 A：按国家分工 + 交叉复核）

```
Codex  ──> 美国侧四层（厂商 + 技术关系 + 投资关系 + 源链接）──┐
Gemini ──> 中国侧四层（同上）                              ──┤
                                                            │ 第一稿
              互换交叉复核（Gemini 审美国稿 / Codex 审中国稿）│
                                                            ▼
Claude（我）──> 逐条 curl/WebFetch 验活所有链接
            ──> 裁决两边分歧、补缺、统一术语与口径
            ──> 综合成最终深度报告（正文内嵌链接 + 图注 + 时效声明）
```

- 非交互调用：`codex exec "<prompt>"`、`gemini -p "<prompt>"`（均启用联网检索）。
- 每个委派任务把产出**写入本文件夹内的独立文件**，避免污染上下文：
  - `02-drafts/us-codex.md`（Codex 美国稿）
  - `02-drafts/cn-gemini.md`（Gemini 中国稿）
  - `03-reviews/us-reviewed-by-gemini.md`、`03-reviews/cn-reviewed-by-codex.md`
  - `04-final/最终文章.md`
- 委派指令中明确：要求逐条给官方一手链接、标注时效、区分事实与推断。
- 委派指令中明确：每家子代理必须产出本国的**四层覆盖矩阵**——对每个厂商逐层填写"覆盖/不覆盖"，覆盖的层写出**具体产品名**并附该产品的官方链接，不覆盖的填"—"。

## 六、风险与缓解

| 风险 | 缓解 |
|---|---|
| 子代理训练知识不覆盖 2026 年事件，可能编造链接/数字 | 强制要求联网检索；所有链接由我最终验活；2026 关键事件我亲自 WebSearch 复核 |
| 投资金额/产能口径混乱（多个口径混用） | 要求注明口径与日期；文末时效声明；分歧由我裁决 |
| 中文厂商英文资料稀疏 | Gemini 用中文检索官方源（公司公告、招股书、信通院等） |
| 上下文溢出 | 子代理产出落盘到独立文件，我按需 Read |

## 七、验收标准

- 四层 × 中美 全部覆盖，每家有技术关系与（如有）投资关系的明确陈述。
- 正文每条事实/数字有内嵌链接，且链接经验活可访问。
- 结构对标范文逻辑，深度报告体量（8000 字以上）。
- 文末有一手追踪信号与时效声明。
