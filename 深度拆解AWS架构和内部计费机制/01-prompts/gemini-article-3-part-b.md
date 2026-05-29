<以下内容请先在上下文中加载 _shared-header.md 的所有约束，然后执行下面的具体任务>

# 任务：撰写第 3 篇《边界与反思》— 后半部分（GCP / Azure 为什么学不来）

## 第 3 篇的整体定位

前两篇讲完机制和组织底座，第 3 篇要回答两个问题：(1) 这套机制什么时候失效？(2) 别家云厂商为什么学不来？前半（计费副作用与 Bedrock 案例）由 Codex 完成，本任务负责后半（约 2000 中文字）。

## 你负责的三节

### 第 1 节：GCP 的「One Google」文化与产品后果

- Google 历史上是"One Google"文化 — 所有产品共享同一套 infra、同一套 review、同一套 promo 体系
- 经典对比：Steve Yegge 2011 年 Google+ 长文里专门有大段对比 Google 平台化能力的弱势
- 引用：Steve Yegge 2011 Google+ 原帖（archive.org）+ Yegge 后续 podcast 访谈（如 Software Engineering Daily 或 Changelog）补充观点
- 找 1-2 个公开例子说明这种文化对 GCP PaaS 服务的影响（如 Anthos / Cloud Run 的演进路径、与 GCE 之间的关系）
- 引用：GCP 官方 blog / Google Cloud Next 主旨演讲 / 前 Google Cloud 员工实名博客

### 第 2 节：Azure 的 Sales-led 与 ACR 分配机制

- Azure 在 Satya Nadella 上任后转向 Customer Success / Sales-led 结构
- 关键指标 ACR（Azure Consumed Revenue）如何在 Sales 团队和产品团队之间分配
- 引用：Satya Nadella《Hit Refresh》（Tier 2）+ The Information 关于 Azure ACR 分配机制的报道（Tier 2）
- 论点：Azure 是把"卖出去"作为优先级，而 AWS 是把"用起来"作为优先级 — 两种激励产生不同产品形态（Azure 更强 enterprise field motion，AWS 更强自助上手）
- 引用一个 Microsoft 官方对 ACR 的解释（Microsoft 财报电话会 / 投资者关系页 — Tier 1）

### 第 3 节：结尾 — 为什么这套机制是"不可复制"的

- 把 AWS 机制能跑通的前提条件总结成一个清单：API Mandate + 2-Pizza + STL + 14 LPs + Working Backwards + Input Metrics 文化 + Attributed Revenue + Transfer Pricing
- 论点：缺任何一项，机制都会退化成"内部转账游戏"
- 一两段呼应整个系列的本质问题，给读者留下可带走的判断框架（例如：评估一家公司能否做好 PaaS，看它的 IaaS 和 PaaS 团队的考核关系）
- 不需要再引太多新源，主要是收束

## 必须包含的源（至少）

- Steve Yegge 2011 Google+ rant（archive.org，Tier 2）
- Steve Yegge 后续公开访谈一篇（Tier 2）
- Satya Nadella《Hit Refresh》（Tier 2）
- The Information 或类似具名媒体关于 Azure ACR 的报道（Tier 2）
- Microsoft 财报或 IR 页对 ACR 的定义（Tier 1）
- GCP 官方 blog 或 Cloud Next keynote 一处（Tier 1）
- 前 GCP / Azure 员工实名博客一处（Tier 2）

## 字数

约 2000 中文字。

## 输出格式

完整 Markdown 片段（含 YAML front matter `part: 3b`）+ 自己的参考资料表。Claude 整合时会合并到第 3 篇统一参考资料表。

## 提交

直接输出最终 Markdown，不要解释性前后文。
