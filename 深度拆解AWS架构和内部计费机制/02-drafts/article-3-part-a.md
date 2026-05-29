---
title: 边界与反思：计费副作用与 Bedrock 的容量张力
series: 深度拆解 AWS 架构和内部计费机制
part: 3a
author: Codex 初稿
date: 2026-05-26
---

## 机制的副作用：CloudWatch 与 Data Transfer

前两篇把 **归因收入（Attributed Revenue）** 和 **内部转移定价（Transfer Pricing）** 看成一种组织发明：它让平台团队不只是“成本中心”，而能把自己在客户价值链里的贡献计入账面。问题在于，同一套机制也可能把某些底层能力变成过于稳定的收费池。CloudWatch 和 Data Transfer 是最典型的两个公开可见入口。

CloudWatch 的副作用来自可观测性数据的自然膨胀。日志、指标、告警、查询都和生产系统规模一起增长，而且很多增长并不是“业务价值等比例增长”。Corey Quinn 在 2024 年讨论 CloudWatch Logs 时指出，CloudWatch Logs 账单刺痛客户的关键经常不是存储，而是日志摄入（ingest）费用；他同时用当时的公开价格对比了 Standard 与 Infrequent Access 两类日志的每 GB 摄入差异。[^1] AWS 自己在 2023 年 re:Invent 期间发布 CloudWatch Logs Infrequent Access，承认客户应用规模扩大后日志量随之增长，许多客户被迫在可观测性和成本之间做取舍；这个新日志类的摄入单价比 Standard 低 50%，但也去掉了部分高级能力。[^2]

这说明 AWS 并非没有降价或简化的动作。但动作的形态很重要：它不是把 CloudWatch Logs 的默认成本结构整体改掉，而是新增一个能力较少的日志类，让客户自己迁移、自己判断功能取舍。对于工程团队来说，这通常意味着更多治理工作：区分哪些日志要实时告警，哪些只做事后取证；设置保留期；改 IaC 模板；教育服务团队不要把 debug 级别日志永久打到 Standard。CloudWatch 团队提供了更便宜的出口，但没有消除“日志越多，CloudWatch 账面越好看”的基本张力。

Data Transfer 的问题更直接。AWS 官方的 Global Network FAQ 把数据传输收费分成三类：出互联网（DTO）、跨可用区（DTAZ）和跨 Region（DTIR）；其中跨 AZ 数据传输覆盖 EC2、RDS、Redshift、DAX、ElastiCache、跨 AZ ENI 等场景。[^3] AWS 定价白皮书也把 outbound data transfer 列为 AWS 成本的三个基本驱动之一，并说明出站流量会按聚合后的 outbound data transfer rate 出现在月度账单中。[^4] 这类收费对架构设计影响很大：同样是“高可用”，一个服务是否跨 AZ chatty、是否通过 NAT Gateway 访问同 Region 服务、是否跨 Region 做同步复制，都会把可靠性设计翻译成网络账单。

Corey Quinn 对 Data Transfer 的批评持续多年。2021 年他在分析 Cloudflare R2 时，用 1 TB 对象被访问 1000 次的例子说明 AWS egress 如何迅速成为对象存储总成本里的主导项，并把 Cloudflare R2 的零 egress 当成对 AWS 定价结构的直接挑战。[^5] 2022 年，他又专门做实验验证 AWS 所谓 ingress free 是否真的免费，结论是 S3 场景下 AWS 基本符合承诺，但他仍把 AWS Data Transfer 定价称为复杂到需要画图理解。[^6] 这些文章不是 AWS 官方事实来源，但它们反映了长期客户侧 FinOps 语境：Data Transfer 的痛点不只是贵，而是难预测、难解释、难和服务边界对应。

AWS 近年的官方回应也侧面确认了压力。2024 年 3 月，AWS 宣布当客户要把数据迁出 AWS 时，可申请免除出互联网数据传输费；公告同时强调，超过 90% 客户已经不会产生 AWS 出互联网传输费用，因为 AWS 每月提供 100 GB 从 Region 到互联网的免费额度，并提供每月 1 TB CloudFront 免费出站流量。[^7] 这是一项重要变化，但它的边界也很清楚：它主要解决“迁出 AWS”的 switching cost，而不是日常业务 egress、跨 AZ 或跨 Region 架构成本。

因此，CloudWatch 和 Data Transfer 是机制失效的两个公开样本。它们并不能证明某个团队在内部会议上如何计算 P&L；这部分未找到公开来源支持。但从外部账单形态看，当某个内部服务的收入与客户规模、日志量、网络流量深度绑定时，团队天然更容易优化“可配置的折扣选项”，而不是主动拆掉高收入的默认收费路径。这反过来印证了归因收入机制的真实力量：它能激励团队把平台能力产品化，也可能激励团队维护一个对客户不够友好的收入结构。

## Bedrock 与 GPU 容量的内部计费张力

生成式 AI 让这套机制进入更稀缺的资源环境。Amazon Bedrock 是 AWS 在模型调用层的托管入口：客户不必自己训练基础模型，而是通过 Bedrock 选择 Anthropic、Meta、Mistral、Amazon 等模型，按 on-demand、batch、provisioned throughput 等方式付费。AWS Bedrock 定价页明确按模型提供商、模型、Region、输入 token、输出 token、batch 折扣、provisioned throughput 等维度收费。[^8] 在 Andy Jassy 的 2024 年 Q1 财报电话会中，AWS 也把生成式 AI 栈分成三层：底层是自建模型客户使用的 NVIDIA compute instances、Trainium 和 Inferentia；中间层则是希望使用现有 LLM 并做定制、部署生产级应用的 Bedrock。[^9]

这意味着 Bedrock 是 PaaS 层入口，但它消耗的是同一类稀缺底层资源：GPU、Trainium、Inferentia、数据中心、电力和网络。AWS 官方 EC2 页面把 P5/P5e/P5en 描述为面向深度学习和 HPC 的最高性能 GPU 实例，P5 使用 NVIDIA H100，P5e/P5en 使用 NVIDIA H200，最多 8 张 GPU。[^10] AWS Trainium 官方页面则强调 Trainium 是为大规模 AI 训练与推理设计的自研加速器，Trainium1 驱动 EC2 Trn1，Trainium2 相比第一代最高 4 倍性能，并宣称 Trn2 相比 GPU-based EC2 P5e/P5en 有 30% 到 40% 的 price performance 优势。[^11] 2023 年 re:Invent Adam Selipsky 主旨演讲也把 Bedrock、Trainium2、NVIDIA 合作放在同一个生成式 AI 叙事里：AWS 既卖托管模型入口，也卖底层训练和推理基础设施。[^12]

张力来自容量稀缺。The Information 在 2023 年 4 月的具名报道中写到，AI 服务器芯片需求激增导致 AWS、Microsoft、Google、Oracle 等云厂商限制客户可用容量，一些客户报告等待数月才能租到硬件；报道还提到，有客户在 AWS 和 Google Cloud 上花了数周仍未拿到 AI server，部分 AWS 新客户被建议改用 Amazon 自研 Trainium。[^13] 这篇报道早于 Bedrock GA，但它描述的是同一个约束：客户想直接租 GPU 做训练或推理，云厂商同时要把稀缺加速器分配给裸 EC2、托管训练、托管推理和更高阶的 AI 服务。

Jassy 在 2024 年 Q1 电话会的说法进一步把这个约束公开化。他说 AWS 已经有 multi-billion dollar revenue run rate 的 AI 动能；底层方面，AWS 有广泛的 NVIDIA compute instances，同时 Trainium 和 Inferentia 因相对替代方案的 price performance 而需求很高；更大批量 Trainium2 会在 2024 年下半年和 2025 年初到来。[^9] 同一通电话里，Brian Olsavsky 说明 Amazon 预计 2024 年资本开支会同比显著增加，主要由支持 AWS 增长、包括生成式 AI 的基础设施 CapEx 驱动。[^14]

如果把它放回内部核算框架，冲突就很清楚：一块 H100/H200 或一组 Trainium 容量，可以作为 EC2 GPU 实例直接卖给客户，也可以被 Bedrock 包装成 token、模型单元或 provisioned throughput。前者收入归因更接近 IaaS，客户可见的是实例小时、网络和存储；后者收入归因更接近 PaaS，客户购买的是模型能力、低延迟、Guardrails、RAG、Agents、Fine-Tuning 和企业集成。Bedrock 做得越好，越可能把底层容量“向上消化”，让客户不再直接管理 GPU；但在 GPU 极度紧张时，EC2 团队也有理由认为，直接把 GPU 卖给愿意长期承诺的大客户，同样能带来明确收入和利用率。

公开材料没有披露 AWS 内部如何在 Bedrock、EC2 GPU、Trainium/Inferentia 团队之间分摊毛利，也没有披露 Bedrock 不同模型实际运行在哪类加速器上；这些点未找到公开来源支持。因此这里不能把“内部争抢 GPU”写成已证实事实。更稳妥的说法是：AWS 官方和具名报道共同证明了三件事。第一，Bedrock 是 AWS 生成式 AI 的中间层产品入口。第二，EC2 GPU 与 Trainium/Inferentia 是同一生成式 AI 栈的底层稀缺能力。第三，2023 到 2024 年，AI 加速器容量和 CapEx 是 AWS 对外承认的核心约束。由此可以推导，归因收入机制在 AI 时代会遇到比 CloudWatch 和 Data Transfer 更尖锐的资源分配问题：高阶服务越成功，越需要吞掉底层最稀缺的硬件；底层团队越能直接变现，越会要求内部转移价格准确反映机会成本。

这对本系列的本质问题很关键。PaaS 团队要有动力做出好产品，不能只靠“把 IaaS 包一层再加价”；它必须在内部拿到足够合理的容量价格，同时让底层团队相信，容量被 PaaS 消化后产生的是更高客户生命周期价值，而不是账面收入从一个团队挪到另一个团队。Bedrock 是这套机制在生成式 AI 时代的新考题。

## 参考资料

[^1]: [Tier 2] A Nuanced Logging Optimization Point — Corey Quinn / Last Week in AWS — 2024-02-12 — https://www.lastweekinaws.com/newsletter/a-nuanced-logging-optimization-point/

[^2]: [Tier 1] New Amazon CloudWatch log class for infrequent access logs at a reduced price — Marcia Villalba / AWS News Blog — 2023-11-26 — https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-log-class-for-infrequent-access-logs-at-a-reduced-price/

[^3]: [Tier 1] AWS Global Network FAQs — Amazon Web Services — 2026-05-28 accessed — https://aws.amazon.com/about-aws/global-infrastructure/global-network/faqs/

[^4]: [Tier 1] Key principles - How AWS Pricing Works — Amazon Web Services Docs — 2026-05-28 accessed — https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/key-principles.html

[^5]: [Tier 2] The Compelling Economics of Cloudflare R2 — Corey Quinn / Last Week in AWS — 2021-10-06 — https://www.lastweekinaws.com/blog/the-compelling-economics-of-cloudflare-r2/

[^6]: [Tier 2] AWS Data Transfer Charges: Ingress Actually Is Free — Corey Quinn / Last Week in AWS — 2022-10-12 — https://www.lastweekinaws.com/blog/aws-data-transfer-charges-ingress-actually-is-free/

[^7]: [Tier 1] Free data transfer out to internet when moving out of AWS — Sébastien Stormacq / AWS News Blog — 2024-03-05 — https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/

[^8]: [Tier 1] Amazon Bedrock pricing — Amazon Web Services — 2026-05-28 accessed — https://aws.amazon.com/bedrock/pricing/

[^9]: [Tier 1] Q1 2024 Amazon Earnings Call Transcript — Amazon Investor Relations — 2024-04-30 — https://s2.q4cdn.com/299287126/files/doc_financials/2024/q1/Q124-Amazon-Transcript-FINAL.pdf

[^10]: [Tier 1] Amazon EC2 Accelerated Computing Instances — Amazon Web Services — 2026-05-28 accessed — https://aws.amazon.com/ec2/instance-types/accelerated-computing/

[^11]: [Tier 1] AWS Trainium — Amazon Web Services — 2026-05-28 accessed — https://aws.amazon.com/ai/machine-learning/trainium/

[^12]: [Tier 1] AWS re:Invent 2023 - CEO Keynote with Adam Selipsky — AWS Events / YouTube — 2023-11-28 — https://www.youtube.com/watch?v=PMfn9_nTDbM

[^13]: [Tier 2] AI Developers Stymied by Server Shortage at AWS, Microsoft, Google — Aaron Holmes and Anissa Gardizy / The Information — 2023-04-07 — https://www.theinformation.com/articles/ai-developers-stymied-by-server-shortage-at-aws-microsoft-google/

[^14]: [Tier 1] Q1 2024 Amazon Earnings Call Transcript, capital expenditures remarks — Amazon Investor Relations — 2024-04-30 — https://s2.q4cdn.com/299287126/files/doc_financials/2024/q1/Q124-Amazon-Transcript-FINAL.pdf
