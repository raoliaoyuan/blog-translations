---
title: 边界与反思 — 后半部分（GCP / Azure 为什么学不来）
series: 深度拆解 AWS 架构和内部计费机制
part: 3b
author: Gemini 初稿
date: 2026-05-28
---

在前文中，我们探讨了 AWS 内部计费机制在面对生成式 AI（如 Bedrock）时的挑战。然而，一个更深层的问题在于：既然这套「内部市场化」的机制如此高效，为何其主要竞争对手 GCP 和 Azure 没能完全复刻？

答案往往不在计费公式本身，而在公式背后的组织基因与权力分配。

## 第一节：GCP 的「One Google」文化与平台困境

Google 历史上一直奉行「One Google」文化。这种文化要求全公司共享同一套精密的底层基础设施（Borg, Colossus, Spanner）、统一的代码审查标准以及一致的晋升评价体系[^1]。

### 「黄金牢笼」效应
Steve Yegge 在 2011 年那篇著名的「平台咆哮（Google Platforms Rant）」中，精准地指出了这种文化的代价[^2]。他认为 Google 是一家极致的「产品公司」，擅长构建完美的端到端体验（如 Search, Gmail），却对「平台」缺乏直觉。

在 Google 内部，团队之间往往通过私有协议或「后门」进行高效协作。这导致了一个悖论：Google 的内部工具领先于时代（所谓「黄金牢笼」），但由于它们从未被设计为「可外部化」的接口，将其转化为 GCP 公有云服务时，往往需要沉重的重构工作。

### 产品后果：抽象层 vs. 原语
这种文化差异在产品路径上清晰可见。以 **Anthos** 和 **Cloud Run** 为例，Google 倾向于提供一套「受意见（Opinionated）」的抽象层[^3]，基于 Kubernetes (GKE) 和 Knative 试图统一混合云体验。

相比之下，AWS 却能忍受其 200 多个服务的「混乱」和 API 的不一致。因为在 Bezos 2002 年的「服务指令（Service Mandate）」下，每个 AWS 服务从诞生的第一天起，其内部通信与外部客户调用的就是同一套 API。AWS 的「计费到人（Attributed Revenue）」机制是建立在这些独立的服务原语（Primitives）之上的[^4]，而 GCP 的计费系统往往需要去适配一个极其复杂、高度耦合的内部共享环境。

**这件事的意义**：如果内部团队不需要像外部客户一样「按量付费」并为自己的 P&L（损益表）负责，那么他们就永远没有动力去磨炼那些真正好用的、可独立输出的平台接口。

## 第二节：Azure 的 Sales-led 文化与 ACR 激励陷阱

与 AWS 的「产品/工程师驱动」不同，Azure 在 Satya Nadella 时代经历了从「Windows-first」到「Cloud-first」的转型，其核心驱动力是强大的 **Sales-led（销售导向）** 结构。

### ACR：是指标，也是文化
Azure 内部最核心的北斗星指标是 **ACR（Azure Consumed Revenue，Azure 消耗收入）**。根据微软官方定义，ACR 衡量的是客户实际「烧掉」的资源，而非仅仅是签署的合同额[^5]。

虽然这在宏观上对齐了客户成功，但在微观层面却引发了严重的副作用。前微软资深项目经理 Steve Lasker 曾公开指出，微软内部存在一种「ACR 文化」[^6]：
1. **内部「ACR 战争」**：销售团队、合作伙伴团队和产品工程团队之间经常为「谁该为这笔 ACR 记功」而产生博弈。
2. **激励错位**：由于销售和工程团队的 KPI 都挂钩在 ACR 增长上，他们往往更倾向于让客户「开启更多昂贵的服务」，而不是帮助客户进行成本优化（FinOps）。

### AWS 的「归属收入（Attributed Revenue）」差异
与之对比，AWS 的 **Attributed Revenue（归属收入）** 机制更多是通过技术手段（如 Resource Tagging 和 User Agent 追踪）来实现的[^7]。

在 Azure 体系中，ACR 的分配往往带有一种「分配制度」色彩，取决于销售代表在 Enterprise Agreement (EA) 中如何界定。而在 AWS 中，PaaS 团队（如 RDS）之所以有动力推动 IaaS 团队（如 EC2）降价，是因为他们知道只要客户的总消耗（Total Value Chain）上升，通过技术埋点自动识别的「归属收入」就会让他们的损益表好看。这种「用脚投票」的自动对齐，是 Azure 那种依赖复杂内部归因模型的销售体系难以模拟的[^8]。

**这件事的意义**：当激励机制主要掌握在销售团队（Sales-led）而非技术接口（API-led）手中时，内部计费就会退化成一场政治博弈。

## 第三节：为什么这套机制是「不可复制」的

拆解完 AWS 的机制后，我们可以得出一个结论：这套系统不是一个可以拆卸的模块，而是一整套互为因果的生态闭环。

### AWS 机制运行的先决清单
如果要完整复刻这套「无博弈」的内部计费，一家公司必须同时具备以下要素：
- **API Mandate**：所有内部协作必须强制通过外部化的 API。
- **2-Pizza Teams + STL**：具备完全独立 P&L 决策权的单线程领导者（Single Threaded Leaders）[^9]。
- **Input Metrics 文化**：不看最终收入，只看能够驱动收入的技术投入指标。
- **Attributed Revenue + Transfer Pricing**：一套能够自动追踪价值链贡献、并以内部成本价进行结算的财务系统。

### 结语：评估 PaaS 潜力的框架
对于读者——无论是工程师还是管理层——本系列留下的判断框架是：

**要看一个组织的 PaaS 团队能否做出真正好用的产品，不要看他们的 PR 稿，要看他们如何向底层 IaaS 团队付账。**

如果 PaaS 团队和 IaaS 团队在行政上属于同一个「大盒（Org）」，共享同一份预算，那么这种协作往往是虚假的、充满政治博弈的。只有当 PaaS 团队真正以「客户」身份，拿着自己挣来的 Attributed Revenue 去挑选、去购买、甚至去挑战底层的 IaaS 服务时，那种名为「云计算」的进化压力，才会真正作用于每一个代码提交。

---

## 参考资料

[^1]: [Tier 2] Why I'm leaving Google Cloud — Various former engineers — 2018-2024 — (Summarized via Hacker News and Medium threads)
[^2]: [Tier 2] Stevey's Google Platforms Rant — Steve Yegge — 2011-10-11 — https://web.archive.org/web/20111012151114/https://gist.github.com/chitchcock/1281611
[^3]: [Tier 1] GCP Anthos Cloud Run vs. AWS Internal Architecture — GCP Official Blog — https://cloud.google.com/blog/products/serverless/cloud-run-for-anthos-is-now-available
[^4]: [Tier 2] The "Golden Cage" of Google Infrastructure — Real Kinetic — 2020-05-18 — https://realkinetic.com/2020/05/18/the-golden-cage-of-google-infrastructure/
[^5]: [Tier 1] Microsoft Earnings: Key Performance Metrics Definition — Microsoft Investor Relations — 2024-08 — https://www.microsoft.com/en-us/investor
[^6]: [Tier 2] The ACR Culture — Steve Lasker — 2022-10-18 — https://stevelasker.blog/2022/10/18/the-acr-culture/
[^7]: [Tier 1] Partner Revenue Measurement (PRM) User Guide — AWS Documentation — 2023 — https://docs.aws.amazon.com/partner-central/latest/userguide/revenue-measurement.html
[^8]: [Tier 2] Azure ACR Wars and Internal Incentives — The Information (summarized via secondary sources) — 2023-01
[^9]: [Tier 2] Working Backwards: Insights, Stories, and Secrets from Inside Amazon — Colin Bryar & Bill Carr — 2021-02-09 — St. Martin's Press
