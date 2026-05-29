---
title: 边界与反思 — 后半部分（GCP / Azure 为什么学不来）
series: 深度拆解 AWS 架构和内部计费机制
part: 3b
author: Codex 初稿
date: 2026-05-26
---

前半部分讨论了 AWS 这套内部市场化机制在生成式 AI 时代的张力。后半部分要问另一个问题：如果「归属收入（Attributed Revenue）+ 内部转移定价（Transfer Pricing）」能把 PaaS 与 IaaS 的利益绑在一起，为什么 GCP 和 Azure 没有照搬？

答案不是「不会算账」。更可能是：这套机制依赖的组织前提，不是财务系统上线后才出现的，而是产品架构、团队边界、销售权力和客户度量长期共同塑造的结果。

## GCP：共享基础设施很强，但平台化不是同一件事

Google 的优势从来不是基础设施不够强。Google Cloud 官方介绍 Colossus 时明确说，同一套底层存储基础设施同时支撑 Google Cloud 和 YouTube、Drive、Gmail 等 Google 产品；同文还把 Colossus、Spanner、Borg 列为 Google Cloud 存储服务的核心构件，并说明 Borg 对 Kubernetes 的设计和发展有持续影响。[^1] 这是一种典型的「One Google」路径：先为 Google 自己的大规模业务构建统一底座，再把其中一部分能力产品化给外部客户。

问题在于，「内部共享底座」和「外部可购买的平台原语」不是同一个工程目标。Steve Yegge 在 2011 年那篇实名 Google+ 长文里，把 Amazon 和 Google 做了很尖锐的对比：他认为 Amazon 在 2002 年前后被强制要求所有团队通过服务接口通信，接口从一开始就要能外部化；而 Google 的问题是更像产品公司，不够像平台公司。[^2] 这篇文章不是 AWS 官方史料，也带有强烈个人判断，但它的价值在于：作者同时有 Amazon 和 Google 工作经历，并且把「内部 API 边界」和「外部平台能力」之间的关系讲得很清楚。

Kubernetes 是一个更温和、更正面的例子。Google Cloud 官方说 Kubernetes 是 Borg 的开源衍生物，目标之一是把应用放在任何 Kubernetes 实现上运行，包括云厂商提供的实现或客户自己运行的实现。[^3] 后来 Google 又在 Kubernetes 1.11 的官方博客中强调，把 cloud provider 相关代码从 Kubernetes core 中拆出，以提高可插拔性和多云可移植性。[^4] 这些都是平台化努力，但也说明一个事实：把 Google 内部已经成熟的能力外部化，需要重新设计接口、治理和生态边界。

Anthos 进一步体现了这种路径。Google Cloud 官方把 Anthos 描述为基于 Kubernetes Resource Model、面向混合云和多云的一致应用平台，可运行在 Google Cloud、AWS 和 Azure 上。[^5] The Register 对 Anthos 的报道也把它概括为 Google Cloud Next 2019 上的跨云管理平台，强调「write once, run anywhere」的诉求。[^6] 这不是坏产品路线，但它和 AWS 的服务原语路线不同：GCP 更倾向于提供一个一致的控制面和抽象层，而 AWS 更愿意让大量独立服务以各自 API 暴露，再用客户实际消费来证明服务边界是否成立。

公开质疑也集中在这里。The Register 在 2020 年报道 Istio 和 Knative 是否捐给基金会时，指出 Kubernetes 已在 2015 年捐给 CNCF，但 Knative 当时没有立即进入基金会，引发社区对 Google 控制权的担忧。[^7] 这类争议不能证明 GCP 内部财务激励怎样运作，但能说明：当平台既是公司战略资产，又要成为开放生态基础设施时，接口归属、控制权和商业化节奏会天然拉扯。

这一节对本系列问题的意义是：如果 PaaS 团队建立在高度共享、内部优先的基础设施之上，它未必天然拥有像外部客户一样「购买」底层 IaaS 原语的关系。没有这种买卖边界，Attributed Revenue 就很难自动变成团队之间的利益结算语言。

## Azure：ACR 是消费收入指标，不是可公开证明的工程分账机制

Azure 讨论里最容易出错的是 ACR。这里必须先拆开两个缩写：Azure Container Registry 是容器镜像仓库服务，Microsoft Learn 明确定义它用于存储和分发容器镜像及 OCI artifact；[^8] 本节讨论的 ACR 是 Azure Consumed Revenue，即 Azure 消耗收入，二者不是一回事。

Microsoft Learn 对 Azure Consumed Revenue 的定义很具体：ACR 是客户消费 Azure 服务的货币价值，计算方式是「计量资源数量 × 客户支付的单位价格」；它可以按 subscription、enrollment、resource 或 billing meter 聚合，且不等同于 billed revenue，因为预付承诺、Reserved Instance 等场景下，客户预付金额和实际消费金额可能不同。[^9] 这说明 Azure 的北极星之一确实是「客户实际用了多少 Azure」，而不是只看合同签了多少。

这和 Satya Nadella 在《Hit Refresh》里讲的文化转向是一致的。HarperCollins 对该书的介绍把核心主题概括为 Microsoft 的转型、同理心和重新发现公司使命；Nadella 在书中反复把 empathy 和理解客户未被表达的需求放在领导力和产品判断中心。[^10] 因此，把 Azure 的消费收入指标理解为「从 license / booking 转向 customer usage」是有公开来源支持的。

但这里必须停住。公开资料能证明 Microsoft 有 ACR 定义，也能证明合作伙伴体系里存在围绕 ACR 的归因和激励。例如 Partner Reported Azure Consumed Revenue 页面说明，PRACR 用于让 Microsoft field incentives 与最终客户 Azure consumption 对齐，以减少 SaaS 解决方案的渠道冲突。[^11] 这仍然是 partner / field-facing 机制，不是 Microsoft 内部 Sales 与 Engineering 之间如何分配 ACR 的财务规则。本文未找到可靠公开来源支持「微软销售代表与工程团队围绕 ACR 互相博弈」「工程团队 KPI 直接按 ACR 分账」这类说法，因此不采用这些断言。

Azure 与 AWS 的差异更稳妥的写法是：Azure 公开可见的 ACR 体系首先服务于客户消费、合作伙伴、销售协同和云业务管理；AWS 公开可见的 Partner Revenue Measurement 也能基于实际 AWS consumption 衡量 partner solutions 驱动的 attributed revenue，但 AWS 文档只证明 partner-facing 归因能力，不证明 AWS 内部 PaaS/IaaS 团队的 P&L 结算细节。[^12] 如果要比较两家公司内部工程激励，公开资料不足以支撑精确机制对照。

这一节的意义是：不能因为 Azure 有 ACR，就把它等同于 AWS 式内部市场。消费收入指标可以对齐客户成功，也可以服务销售和伙伴生态；但它是否能让 PaaS 团队像客户一样向 IaaS 团队付账，公开资料没有给出答案。

## 为什么难以复制

AWS 机制之所以难复制，不是因为别家公司不知道「按用量算钱」。公开资料能看到几个前提同时存在：第一，Yegge 所描述的 Amazon 服务接口强制令，把内部协作推向可外部化 API；[^2] 第二，AWS 官方对 two-pizza team 和 single-threaded ownership 的解释，强调小团队对单一服务、客户和全生命周期负责；[^13] 第三，AWS PRM 这类 partner-facing 系统至少证明 AWS 有能力基于实际服务消费做自动化归因。[^12]

但这些公开资料也给出边界：AWS 官方 two-pizza 文章自己承认，小团队机制可能带来重复建设和孤岛问题，需要治理结构处理。[^13] Google 的反例说明，强大的共享基础设施不等于天然形成可结算的服务市场。Azure 的反例说明，客户消费指标不等于工程组织内部自动分账。

所以评估一家云厂商或一家大型企业能否做出好用的 PaaS，不应只看它有没有「平台战略」或「消费收入指标」。更关键的问题是：PaaS 团队是否能以清晰的 API、清晰的成本、清晰的客户归因，像真实客户一样选择和约束底层 IaaS；IaaS 团队是否因为 PaaS 的成功而自动受益，而不是只在预算会和组织会上被要求配合。

如果这个关系不存在，PaaS 就很容易退回两种状态：在 GCP 式共享底座里，产品化要不断和内部基础设施边界谈判；在 Azure 式销售协同里，消费增长可以被很好地度量，但未必自然翻译成工程团队之间的内部市场价格。AWS 的特殊性恰恰在于，它把技术边界、团队边界和收入归因尽早绑在了一起。这个组合不是一个财务插件，而是一整套组织操作系统。

## 参考资料

[^1]: [Tier 1] Colossus under the hood: a peek into Google’s scalable storage system — Dean Hildebrand, Denis Serenyi / Google Cloud Blog — 2021-04-20 — https://cloud.google.com/blog/products/storage-data-transfer/a-peek-behind-colossus-googles-file-system

[^2]: [Tier 2] Stevey's Google Platforms Rant — Steve Yegge — 2011-10-12 — https://gist.github.com/chitchcock/1281611

[^3]: [Tier 1] How Kubernetes takes container workload portability to the next level — Alex Barrett / Google Cloud Blog — 2016-05-09 — https://cloud.google.com/blog/products/gcp/how-kubernetes-takes-container-workload-portability-to-the-next-level/

[^4]: [Tier 1] Kubernetes 1.11: a look from inside Google — Craig Box / Google Cloud Blog — 2018-07-02 — https://cloud.google.com/blog/products/gcp/kubernetes-1-11-a-look-from-inside-google

[^5]: [Tier 1] Anthos, a modern application platform for enterprises — Veer Muchandi / Google Cloud Blog — 2021-06-03 — https://cloud.google.com/blog/products/application-modernization/anthos-modern-application-platform-enterprises

[^6]: [Tier 2] Google Cloud flashes flower power in bid to realize 'write once, run anywhere' dream — Thomas Claburn / The Register — 2019-04-09 — https://www.theregister.com/2019/04/09/gcp_anthos_keynote/

[^7]: [Tier 2] Google Cloud CEO says Istio will be handed to a foundation. The Reg: But what about..? Google: That will be all. — Tim Anderson / The Register — 2020-04-23 — https://www.theregister.com/off-prem/2020/04/23/google-cloud-ceo-says-istio-will-be-handed-to-a-foundation-the-reg-but-what-about-google-that-will-be-all/1368891

[^8]: [Tier 1] About registries, repositories, images, and artifacts — Microsoft Learn — 2026-03-25 — https://learn.microsoft.com/en-us/azure/container-registry/container-registry-concepts

[^9]: [Tier 1] How to use the Azure usage report — Microsoft Learn — 2025 — https://learn.microsoft.com/en-us/partner-center/insights/azure-usage-report

[^10]: [Tier 2] Hit Refresh: The Quest to Rediscover Microsoft's Soul and Imagine a Better Future for Everyone — Satya Nadella, Greg Shaw, Jill Tracie Nichols / Harper Business — 2017-09-26 — https://www.harperacademic.com/book/9780062652508/hit-refresh/

[^11]: [Tier 1] Partner Reported Azure Consumed Revenue — Microsoft Learn — 2026-04-29 — https://learn.microsoft.com/en-us/partner-center/referrals/partner-reported-azure-consumed-revenue

[^12]: [Tier 1] What is Partner Revenue Measurement? — AWS Documentation — 2026 — https://docs.aws.amazon.com/PRM/latest/aws-prm-onboarding-guide/what-is-service.html

[^13]: [Tier 1] Powering Innovation and Speed with Amazon’s Two-Pizza Teams — Daniel Slater / AWS Executive Insights — 2022 — https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/
