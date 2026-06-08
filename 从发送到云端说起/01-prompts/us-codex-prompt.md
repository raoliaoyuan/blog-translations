你是一名 AI 产业研究员。请联网检索，产出一份关于【美国侧】AI 产业四层格局的结构化研究稿，用中文写作，保存为 Markdown。

## 输出位置
把最终结果写入文件：02-drafts/us-codex.md（相对当前工作目录）。只写这一个文件。

## 分析框架：四层
芯片 → 云计算 → LLM → Agent 入口/运行时。

## 必须覆盖的美国厂商
- 芯片：Nvidia、AMD、Google TPU、AWS Trainium/Inferentia、Microsoft Maia、Broadcom、Marvell
- 云：AWS、Azure、Google Cloud、Oracle、CoreWeave
- LLM：OpenAI、Anthropic、Google DeepMind、Meta、xAI
- Agent 入口/运行时：Claude Code（含 on the web）、OpenAI Codex、Google Jules、Cursor、GitHub Copilot、AWS Bedrock AgentCore、Azure AI Foundry Agent Service

## 三类关系（每家都要讲）
1. 技术/供货关系：谁给谁供芯片、跑在谁的云、谁集成谁的模型。
2. 投资/股权关系：谁投了谁、金额、占股比例、长期承诺（如 Amazon 对 Anthropic 投资、Microsoft 对 OpenAI、Nvidia 的各项投资等）。
3. 竞争关系：供货方/投资方同时在产品层与被投或客户竞争的"三重身份"。

## 必做：四层覆盖矩阵
产出一张 Markdown 表格，行=主要厂商（Google、Amazon/AWS、Microsoft、Nvidia、OpenAI、Anthropic、Meta、xAI、Oracle 等），列=芯片/云/LLM/Agent 四层。
- 每个单元格：若覆盖该层，填【具体产品名】（不是打勾），例如 Google 芯片格填 "TPU"；不覆盖填 "—"。
- 每个产品名后附该产品的官方链接。
示例：Google = 芯片(TPU) / 云(Google Cloud) / LLM(Gemini, DeepMind) / Agent(Jules、Vertex AI Agent Builder)。OpenAI = 芯片(—) / 云(—) / LLM(GPT) / Agent(ChatGPT、Codex)。

## 硬性要求（务必遵守）
1. 来源：官方一手优先（公司公告/SEC 文件/官网/财报）> 主流权威媒体（Reuters/Bloomberg/FT/The Information）。每一条事实、数字、关系都要在正文内嵌可点击链接：[中文锚文字](url)。不要列"参考文献"集中堆在文末，要内嵌。
2. 链接必须是真实、可访问的 URL。不确定的链接宁可不写，不要编造 URL。
3. 时效：投资额、产能、份额等数字标注口径与日期，以 2026-06-01 前后公开信息为准。不同口径（如 Oracle 采购的不同金额说法）不要混用，分别注明。
4. 区分事实与推断：无官方出处的判断显式标注为"（结构性推断）"。
5. 写作语气克制，技术术语首次出现用"中文（English）"。

## 结构建议
1. 四层覆盖矩阵（表格）
2. 第一层·芯片（逐家：技术关系+投资关系+竞争+出口管制背景）
3. 第二层·云
4. 第三层·LLM
5. 第四层·Agent 入口/运行时
6. 美国侧关系网小结：供货×持股×竞争三角，谁全栈自有、谁被夹在中间。

请现在开始联网检索并写文件。
