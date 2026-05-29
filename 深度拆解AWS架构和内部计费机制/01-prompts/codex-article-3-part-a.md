<以下内容请先在上下文中加载 _shared-header.md 的所有约束，然后执行下面的具体任务>

# 任务：撰写第 3 篇《边界与反思》— 前半部分（计费副作用与 Bedrock 案例）

## 第 3 篇的整体定位

前两篇讲完机制和组织底座，第 3 篇要回答两个问题：(1) 这套机制什么时候失效？(2) 别家云厂商为什么学不来？本任务负责前半（约 2000 中文字），后半（GCP/Azure 对比）由 Gemini 完成。整合时由 Claude 缝合。

## 你负责的两节

### 第 1 节：机制的副作用 — CloudWatch / Data Transfer 计费投诉

- 多年来 AWS 客户最痛的两个账单类目：CloudWatch（指标 / 日志爆炸式增长）和 Data Transfer（跨 AZ / 跨 Region / Egress）
- 引用：Corey Quinn《Last Week in AWS》多篇文章（至少 2 篇不同主题，2019-2024）
- 论点：当一个内部服务（CloudWatch、网络）的 attributed revenue 模型被设计得过于"激进"，结果就是它的团队没动力主动降价 / 简化定价，因为账面收入太可观
- 引用一个 Werner Vogels 或 AWS 官方对 Data Transfer 定价的公开回应（如有 — 找近几年的官方表态，例如 2024 Data Transfer 出口免费政策调整公告）
- 这反过来印证机制本身的存在 — 当机制把利润绑死在某团队上，它就有动力维护现状

### 第 2 节：Bedrock 与 GPU 容量的内部计费张力

- Bedrock 是 AWS 在生成式 AI 时代的 PaaS 入口，跑在 EC2 GPU 实例 + Trainium / Inferentia 上
- 引用：2023 re:Invent Adam Selipsky 主旨演讲（AWS 官方 YouTube）+ Bedrock 定价页 + AWS Trainium 产品页
- 引用：The Information 或 Bloomberg 关于 2023-2024 AWS GPU 容量挤压的报道
- 论点：当外部 GPU 容量极度紧张时，Bedrock 团队和直接卖 EC2 GPU 实例的团队之间的内部利润分配会出现张力 — 高阶服务"消化"了 GPU 容量，但客户也可能宁愿直接租裸 GPU
- 找一段公开材料证明这种张力（如 Andy Jassy 财报电话会上对 Bedrock 与 EC2 GPU 关系的表述 — Amazon SEC 10-Q earnings call transcript）

## 必须包含的源（至少）

- Corey Quinn《Last Week in AWS》两篇不同主题文章（Tier 2）
- AWS 官方对 CloudWatch 或 Data Transfer 定价的近年表态（Tier 1，例如 2024 Egress 免费政策博客）
- 2023 re:Invent Adam Selipsky 主旨演讲 YouTube 链接（Tier 1）
- AWS Bedrock 官方定价页（Tier 1）
- AWS Trainium 产品页（Tier 1）
- The Information 或 Bloomberg 关于 AWS GPU 容量的署名报道一篇（Tier 2）
- Amazon Q1-Q3 2024 财报电话会议转录或 SEC 文件中关于 Bedrock 的表述（Tier 1）

## 字数

约 2000 中文字。

## 输出格式

完整 Markdown 片段（含 YAML front matter `part: 3a`）+ 自己的参考资料表。Claude 整合时会合并到第 3 篇统一参考资料表。

## 提交

直接输出最终 Markdown，不要解释性前后文。
