---
title: 组织与文化底座：AWS 内部机制的操作系统
series: 深度拆解 AWS 架构和内部计费机制
part: 2
author: Codex 初稿
date: 2026-05-26
---

上一篇讨论的是机制：如果一个云厂商既卖 EC2、S3、EBS 这样的基础设施服务，也卖 Lambda、EKS、SageMaker 这样的上层平台服务，那么它必须回答一个问题：客户到底是因为谁创造的价值而付费？外部世界里，AWS 已经把这种问题产品化成了非常细的计量、标签、账单、成本分摊和归因工具。但把这个外部事实进一步外推到 AWS 内部的归属收入（Attributed Revenue）、转移定价（Transfer Pricing）、团队 P&L 或 KPI 分配时，公开资料并不足以支撑具体结论。本文会保持这个边界：内部是否存在某种 attributed revenue 或 transfer pricing，可以作为基于组织和技术形态的合理推测；但任何具体比例、结算口径、团队 KPI 绑定方式，本文都不作断言，因为未找到公开来源支持。

真正值得研究的是另一个问题：为什么这种推测在 Amazon / AWS 身上看起来成立，而在许多公司身上会显得危险？答案不在某个会计公式，而在组织设计。Amazon 长期把服务接口、团队边界、客户语言、输入指标和决策终结机制做成一套管理系统。它不证明 AWS 内部一定怎样分钱，却解释了如果要在强独立核算文化里避免 PaaS 团队和 IaaS 团队互相博弈，组织需要先具备哪些前提。

## 1. API Mandate：把协作关系变成接口关系

Steve Yegge 在 2011 年的实名长文里转述了一个后来被频繁引用的 Amazon 内部转折点：大约 2002 年前后，Jeff Bezos 要求所有团队必须通过服务接口（Service Interface）暴露数据和功能，团队之间也必须通过这些接口通信；不得直接读别人的数据库、不得共享内存、不得走后门；接口还必须从一开始就考虑未来能否对外部开发者开放。Yegge 明确说明这是他的回忆和转述，不是 Amazon 官方发布的备忘录原文，但这份材料来自一位曾在 Amazon 工作约六年半的实名前员工，因此可作为可信二手来源使用。[^1]

这件事经常被讲成 AWS 技术架构的起点，但它同样是组织边界的起点。接口不是单纯的工程实现，它把“找隔壁团队帮忙”改写成“调用另一个服务”。一旦跨团队协作只能通过 API 发生，调用方、被调用方、请求量、错误率、延迟、配额和依赖关系都更容易被记录。换句话说，组织内部原本模糊的人情协作，被压缩成可观察、可限流、可审计的技术契约。

这并不等于“每一次内部 API 调用都是内部账单明细”。这样的说法需要 AWS 内部财务系统来源，本文没有找到公开来源支持。更谨慎的说法是：API mandate 为任何后续的成本归因或价值归因提供了必要的接口边界。没有清晰的服务边界，归因机制只能靠组织层级和项目归属猜测；有了接口边界，至少具备了把消耗和依赖映射到服务关系的基础。

Yegge 还提到，Amazon 在这种面向服务的改造过程中发现了许多副作用：调用链会让故障升级更复杂，内部团队可能像外部攻击者一样压垮你的服务，因此需要配额、限流、监控和服务发现等配套机制。[^1] 这点很重要。服务化不是把组织摩擦消灭，而是把摩擦显性化。对本文的核心问题来说，显性化是第一步：只有当跨团队消耗和依赖能被看见，才可能谈利益对齐。

## 2. Two-Pizza Team 和 STL：让“账”有责任主体

AWS Executive Insights 对二披萨团队（Two-Pizza Team）的解释很直接：团队规模小到两张披萨可以喂饱，理想情况下少于 10 人；但它同时强调，二披萨团队不是只关于人数，而是关于自治、责任和单线程聚焦。Amazon 和 AWS 的二披萨团队通常围绕一个具体产品、服务或客户群建立，拥有端到端生命周期责任，而不是把上线后的服务交给另一个运维组织。[^2]

同一篇 AWS 官方文章还把二披萨团队和单线程领导者（Single-Threaded Leader, STL）连在一起：团队要有单线程所有权，领导者的作用不是成为所有决策的审批瓶颈，而是提供战略方向、移除障碍，并在需要时用机制保持检查和治理。[^2] 另一篇 AWS Enterprise Strategy 文章把 STL 描述为对一个结果拥有单一聚焦和完整决策权的负责人，目的是减少传统矩阵组织中的责任扩散。[^3]

这对内部计费或 attributed revenue 的意义，不是“STL 一定对某张 P&L 负责”。这个具体说法没有公开来源支持。更可靠的结论是：如果一个组织希望把收入、成本、消耗或客户价值归因到某个服务，必须先有能承接这些信号的责任主体。二披萨团队和 STL 的价值在这里：它们把一个服务的路线图、客户体验、运营质量和权衡决策尽量收束到一个可识别的团队及其领导者身上。

Amazon 官方材料也承认这种结构不是没有代价。二披萨团队可能带来重复建设和孤岛化，需要治理结构决定何时合并重复努力，同时又不能压制团队自治。[^2] 这比“团队越小越好”的简单叙事更接近现实。强独立核算文化只有在责任边界足够清楚时才可能促进产品改进；如果边界过度碎片化，它也可能鼓励团队只优化自己的局部指标。

所以，本节的关键不是 Amazon 找到了神奇团队规模，而是它把“服务”作为技术边界，又把“团队”作为责任边界。只有当这两个边界大体重合时，内部核算才有可能不退化成跨部门摊账游戏。

## 3. Working Backwards：先用客户语言定义价值

Werner Vogels 在 2006 年的 All Things Distributed 文章里写到，在 Amazon 的细粒度服务方法中，服务不只是软件结构，也代表组织结构；这些服务有强所有权模型，小团队规模则帮助创新。更关键的是，每个服务都必须明确自己的客户是谁，无论客户是外部客户还是内部客户。[^4]

这段话提供了一个常被忽略的连接点：Amazon 的服务化组织不是只为外部产品服务，也覆盖内部服务。Vogels 进一步解释了逆向工作法（Working Backwards）：先从客户出发，倒推到满足客户需求所需的最小技术要求；产品定义从发布时需要的新闻稿（Press Release）和常见问题（FAQ）开始，再逐步靠近实现。[^4] Colin Bryar 和 Bill Carr 后来在《Working Backwards》一书中系统化讲述了这一套 Amazon 管理实践，包括 PR/FAQ、叙事文档、输入指标、WBR 和组织机制等内容。[^5]

Working Backwards 对本文主题的价值，是把团队竞争从“谁的账面收入更大”往“谁解决了客户问题”拉回去。PaaS 团队如果只用内部收入证明自己，就容易把 IaaS 团队视为成本中心或议价对象；IaaS 团队如果只看底层资源收入，也可能不愿意支持上层抽象降低客户复杂度。PR/FAQ 的作用不是替他们算分成比例，而是在产品立项时迫使团队说清楚客户是谁、痛点是什么、为什么现有方案不够、推出后客户体验如何变化。

需要特别澄清的是，公开材料支持“PR/FAQ 用来澄清产品定义和客户体验”，但不支持“Lambda 团队在 PR/FAQ 中必须定义如何与 EC2 团队结算计算资源”这类具体说法。内部 FAQ 是否包含定价、成本、资源消耗或对既有服务的影响，作为大型公司产品立项的一般实践可以推测；但若具体到 AWS 内部结算口径，未找到公开来源支持。

Working Backwards 的组织意义在于，它让团队先在客户语境中对齐价值，再讨论实现方式和资源消耗。对于强 P&L 文化而言，这提供了一个重要缓冲：财务机制可以衡量结果，但产品定义不应从内部账本开始。

## 4. Leadership Principles：不是口号，而是局部博弈的约束条件

Amazon 的领导力准则（Leadership Principles）是公开资料中最容易被滥用的一类来源。它可以支持 Amazon 如何描述自己的管理价值观，但不能直接证明某个内部财务机制如何运行。本文只讨论四条与组织前提有关的原则。

第一是客户至上（Customer Obsession）。Amazon 官方定义是，领导者从客户出发并逆向工作，努力赢得并保持客户信任；虽然也关注竞争对手，但更执着于客户。[^6] 对内部利益对齐而言，这条原则的作用是设定仲裁方向：当两个服务团队的局部收益冲突时，组织至少有一个公开且反复强调的上位标准，即客户信任和客户体验。它不能自动解决分钱问题，但能降低“内部收入最大化”成为唯一目标的风险。

第二是主人翁意识（Ownership）。Amazon 官方定义强调长期思考，不为短期结果牺牲长期价值，并代表整个公司行动，而不只代表自己团队。[^6] 这对 PaaS / IaaS 协作尤其关键。一个只对本团队短期收入负责的团队，可能会把复杂度、成本或故障风险外部化给别的团队；Ownership 至少在文化上要求团队看到公司整体和长期客户价值。注意，这仍然是文化约束，不是公开可验证的内部考核公式。

第三是勤俭节约（Frugality）。Amazon 对 Frugality 的公开表述是“用更少完成更多”，约束会孕育资源fulness、自给自足和发明，并且不会因为增加人头、预算或固定费用而得额外分。[^7] 对云服务组织来说，这条原则让成本不是财务部门事后审计的问题，而是产品和架构设计时就要面对的问题。它与 transfer pricing 的理论目标相容：让资源消耗显性化，促使团队降本增效。但 AWS 内部是否用某个 transfer price 把这种约束传递到团队账面，未找到公开来源支持。

第四是最高标准（Insist on the Highest Standards）。Amazon 官方定义强调领导者持续提高标准，推动团队交付高质量产品、服务和流程，并确保缺陷不会被传递下去。[^7] 在服务化组织里，这条原则特别重要，因为内部服务也是别人的依赖。一个 IaaS 服务如果只把上层团队当“内部客户”，质量松动会沿调用链放大；一个 PaaS 服务如果只包装底层能力而不承担端到端体验，也会把问题推回底层。最高标准不能替代 SLA、SLO 或运营机制，但它为内部服务像外部产品一样被要求提供文化基础。

这四条原则的共同作用，是为强独立核算加上非财务约束。没有这些约束，团队很容易把 P&L 理解成局部利润最大化；有了这些约束，P&L 至少被放在客户、长期、成本和质量的框架里讨论。

## 5. Input Metrics：降低“只看账面结果”的诱因

Jeff Bezos 在 2016 年致股东信中专门提醒大公司要警惕代理指标（Proxies）。流程本来是为结果服务的，但在复杂组织里，流程很容易变成目标本身；他还强调要保持 Day 1 状态，依靠客户至上、警惕代理指标、拥抱外部趋势和高速度决策。[^8]

Amazon 的 Leadership Principles 也把输入指标（Input Metrics）的思想写进 Deliver Results：领导者关注业务的关键输入，并以正确质量和及时性把它们交付出来。[^7] 《Working Backwards》进一步系统讨论了 Amazon 如何用可控输入指标连接团队动作和业务结果。[^5] 这里不使用上一版草稿中的“WBR 会议 80% 时间讨论输入指标”说法，因为未找到公开合规来源支持该具体数字。

输入指标文化对内部核算尤其重要。收入、利润、归属收入这类输出指标（Output Metrics）通常滞后，而且受市场、销售、定价、客户预算周期和其他团队依赖影响。如果只看输出，团队会有强动机把问题归因给别人：上层服务说底层成本太高，底层服务说上层产品没有需求，平台团队说销售没有卖好，销售说产品不够成熟。

输入指标把讨论拉回团队可控动作：API 可用性、延迟、错误率、单位成本、容量交付速度、客户迁移摩擦、文档质量、支持工单根因等。公开资料不能证明 AWS 内部如何把这些输入指标和具体财务归属绑定，但可以支持一个更稳健的结论：在强 P&L 文化下，如果没有输入指标，财务结果会变成互相甩锅的证据；有了输入指标，管理层至少可以追问团队是否做了自己能控制的正确动作。

这也是 PaaS 团队做出好产品的关键前提。好用的 PaaS 往往会隐藏底层复杂度，甚至减少客户直接消费某些 IaaS 资源的必要性。如果只按短期账面收入衡量，上层抽象可能会被误判为“吃掉底层收入”。输入指标提供了另一种评价语言：它看客户是否更快上线、更少运维、更低故障率、更低总成本，而不是只看某个内部服务的收入归属。

## 6. Disagree and Commit：让争议有终结机制

强独立核算带来的最大组织风险，是争议无法结束。每个团队都能拿出自己的数据、客户、路线图和成本压力。如果没有终结机制，所谓“对齐”会变成无休止评审，最后由行政权力、谈判耐力或预算政治决定。

Bezos 在 2016 年致股东信中把“不同意但执行（Disagree and Commit）”作为高速度决策的一部分。他同时提醒，真正的目标不只是高质量决策，还要保持决策速度；许多决策应在大约 70% 信息时作出，而不是等到 90%；当团队存在深层不一致时，要尽早升级，而不是靠“把对方磨到同意”为止。[^9] Amazon Leadership Principles 也把 Have Backbone; Disagree and Commit 写成正式原则：领导者有义务提出不同意见，但一旦决定作出，就要完整投入执行。[^7]

这对内部计费争议的启示很直接，但仍需克制：公开资料支持 Amazon 有这种决策原则，不支持 AWS 某个内部结算争议具体如何升级或由谁裁决。可以推测的是，当 PaaS 和 IaaS 团队在客户体验、成本承担或路线图优先级上发生冲突时，一个高速度组织必须有机制让争议结束。否则，任何 attributed revenue 或 transfer pricing 都会变成新战场：规则本身持续被谈判，团队无法把精力放回产品。

Disagree and Commit 的价值不在于压制分歧，而在于把分歧限定在决策之前。对强 P&L 文化来说，这一点尤其关键：团队可以为自己的判断辩护，但不能在组织已经选择客户价值路径后，用消极执行继续维护本团队账面利益。

## 7. 机制失效、公开质疑与反例

这套组织 OS 有明显副作用。第一类副作用是接口和体验不一致。Last Week in AWS 在 2021 年刊登过一篇关于 AWS API 不一致性的文章，作者 Luc van Donkersgoed 基于调用大量 AWS `List` / `Describe` API 的经历，列举了 IAM、DynamoDB、RDS、Kinesis、API Gateway、CloudFront、WorkSpaces 等服务在命名、返回结构和空结果行为上的差异，并认为这种不一致增加了开发者心智负担。[^10] 这不是 AWS 官方确认的根因分析，也不能证明“不一致是二披萨团队导致的”。它只能作为外部用户对结果的可见批评：高度自治、服务众多、长期演进的系统，确实可能让统一体验变难。

第二类副作用是跨边界产品可能推进较慢。Amazon EFS 是一个合适但需要谨慎使用的例子。AWS 在 2015 年 4 月 9 日宣布 Amazon Elastic File System，并说明预览版即将开放；2016 年 6 月 28 日，AWS News Blog 宣布 EFS 在三个区域达到 production-ready；AWS What's New 在 2016 年 6 月 29 日发布一般可用公告。[^11][^12][^13] 这说明 EFS 从公布到 GA 大约经历了 14 个多月。公开资料支持这个时间线，也支持 EFS 需要为多个 EC2 实例提供共享、低延迟、托管文件系统访问，并涉及多可用区高可用和耐久设计。[^12] 但“它因为 STL 模式推进缓慢”或“耗时远超行业平均水平”没有公开来源支持，本文不作此判断。

第三类副作用是治理成本。AWS 官方的二披萨团队文章承认，自治团队可能带来重复建设和孤岛，需要合适治理来判断何时合并重复努力。[^2] 这正是强独立核算组织必须付出的管理成本：边界清楚以后，每个团队都更有能力快速行动，也更有能力局部优化。治理机制的任务不是取消自治，而是在重复、冲突、客户体验断裂和底层平台复用之间不断校准。

这些反例提醒我们：组织 OS 不是万能药。服务接口、二披萨团队、STL、PR/FAQ、LP、输入指标和 Disagree and Commit 共同降低了内部博弈的概率，但不会消除博弈。它们把问题从“谁说了算”转化为“客户是谁、接口是什么、责任主体是谁、输入指标是否可控、争议何时结束”。这已经是很大进步，但仍然需要持续治理。

## 收尾：组织设计先于机制设计

回到本系列的本质问题：在一个强独立核算、强 P&L 文化的组织里，如何让 PaaS 层团队有动力做出真正好用的产品，而不是为了自己的账面收入去和 IaaS 团队博弈？

AWS 给后来者的启示，不应被简化成“照抄 attributed revenue 和 transfer pricing”。公开资料不足以让我们复原 AWS 内部财务规则，贸然照抄只会制造新的部门政治。真正可学的是前置条件：接口边界必须清楚，服务必须有责任主体，产品定义必须从客户语言开始，领导力原则必须约束局部优化，输入指标必须让团队对可控动作负责，争议必须有终结机制。

因此，组织设计先于机制设计。没有 API mandate 式的服务边界，内部归因缺少可观察锚点；没有二披萨团队和 STL 式的责任主体，账面信号找不到承接者；没有 Working Backwards 和 Customer Obsession，团队会把内部收入误当客户价值；没有输入指标和 Disagree and Commit，财务机制会变成甩锅和拉扯的工具。

这套 OS 不能保证内部计费机制一定公平，但它让“公平”有了可讨论的对象。对其他组织而言，最危险的路径是先上复杂分账模型，再希望组织自然对齐。AWS 的经验更像相反：先把组织改造成能承受分账信号的形态，再让财务机制成为客户价值链的翻译器。

## 参考资料

[^1]: [Tier 2] Stevey's Google Platforms Rant — Steve Yegge / GitHub Gist mirror by chitchcock — 2011-10-12 — https://gist.github.com/chitchcock/1281611
[^2]: [Tier 1] Amazon's Two Pizza Teams — AWS Executive Insights / Daniel Slater — n.d.（访问 2026-05-28）— https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/
[^3]: [Tier 1] Breaking Through Bureaucracy: A Leader’s Guide to Establishing Your First Autonomous Team — AWS Enterprise Strategy Blog — 2025-03-10 — https://aws.amazon.com/blogs/enterprise-strategy/breaking-through-bureaucracy-a-leaders-guide-to-establishing-your-first-autonomous-team/
[^4]: [Tier 2] Working Backwards — Werner Vogels — 2006-11-01 — https://www.allthingsdistributed.com/2006/11/working_backwards.html
[^5]: [Tier 2] Working Backwards: Insights, Stories, and Secrets from Inside Amazon — Colin Bryar & Bill Carr — 2021-02-09 — https://us.macmillan.com/books/9781250267597/workingbackwards
[^6]: [Tier 1] Leadership Principles — Amazon Jobs — n.d.（访问 2026-05-28）— https://www.amazon.jobs/content/en/our-workplace/leadership-principles
[^7]: [Tier 1] Leadership Principles — Amazon Jobs — n.d.（访问 2026-05-28）— https://www.amazon.jobs/content/en/our-workplace/leadership-principles
[^8]: [Tier 1] 2016 Letter to Shareholders — Jeff Bezos / Amazon — 2017-04-12 — https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
[^9]: [Tier 1] 2016 Letter to Shareholders — Jeff Bezos / Amazon — 2017-04-12 — https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
[^10]: [Tier 3，未经 AWS 官方确认] How AWS dumps the mental burden of inconsistent APIs on developers — Luc van Donkersgoed / Last Week in AWS — 2021-09-24 — https://www.lastweekinaws.com/blog/how-aws-dumps-the-mental-burden-of-inconsistent-apis-on-developers/
[^11]: [Tier 1] Introducing Amazon EFS — AWS What's New — 2015-04-09 — https://aws.amazon.com/about-aws/whats-new/2015/04/introducing-amazon-efs/
[^12]: [Tier 1] Amazon Elastic File System – Production-Ready in Three Regions — Jeff Barr / AWS News Blog — 2016-06-28 — https://aws.amazon.com/blogs/aws/amazon-elastic-file-system-production-ready-in-three-regions/
[^13]: [Tier 1] Amazon Elastic File System (Amazon EFS) is Now Generally Available — AWS What's New — 2016-06-29 — https://aws.amazon.com/about-aws/whats-new/2016/06/amazon-elastic-file-system-efs-is-now-generally-available/
