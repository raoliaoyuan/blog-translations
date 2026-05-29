<以下内容请先在上下文中加载 _shared-header.md 的所有约束，然后执行下面的具体任务>

# 任务：撰写第 2 篇《组织与文化底座》

## 核心论点

第 1 篇讲的 Attributed Revenue + Transfer Pricing 不是凭空能跑通的 — 它需要 Amazon 这套独特的组织 OS 兜底：2-Pizza Team、Single-Threaded Leader（STL）、Bezos 2002 API Mandate、Working Backwards、14 Leadership Principles。本篇要把这套 OS 拆给读者看，让读者理解"机制能成立"的前提条件。

## 文章结构（建议）

### 开篇钩子

回顾第 1 篇结尾：机制听起来很美，但为什么 Amazon 能跑通而别家做不到？答案在它的组织设计。

### 第 1 节：Bezos 2002 API Mandate — 一切的起点

- 这道 memo 至今未被 Amazon 官方公开，但有 Steve Yegge 2011 年在 Google+ 实名长文中转述
- 引用：Steve Yegge 2011 Google+ 原帖（archive.org 备份链接）+ Hacker News 当年的原始讨论帖
- 关键内容：所有团队必须以 service interface 暴露能力；不许走捷径；不遵守的人会被开除；外部化的接口和内部接口必须一致
- 论点：这道 memo 强行把 Amazon 从单体公司切成"互相之间是客户和供应商"的服务网络，为后来的 attributed revenue 提供了天然的接口边界

### 第 2 节：2-Pizza Team & Single-Threaded Leader

- 2-Pizza Team：人数能被 2 个 pizza 喂饱（~6-10 人）。引用：Bezos 在 2018 年 Forum on Leadership Q&A 的视频（YouTube）+ Colin Bryar & Bill Carr《Working Backwards》第 4 章
- STL：每个团队 / 项目只有一个"single-threaded leader"对结果负全责。引用：Brad Porter 的 LinkedIn 长文「Single-Threaded Leadership」+ Jeff Wilke 在 Recode Decode 访谈中的描述
- 论点：当每个 team 都有清晰的边界 + 一个能拍板的人，他们就可以独立核算 — attributed revenue 的"账"才有归属对象

### 第 3 节：Working Backwards & PR-FAQ

- 写产品先写新闻稿和 FAQ — 引用：Colin Bryar & Bill Carr《Working Backwards》同名章节 + Werner Vogels 博客对 PR-FAQ 的描述 + Amazon careers 官方对该流程的提及
- 论点：这个仪式强制所有团队从"客户语言"出发设计产品 — 这意味着 EKS 团队设计时会想"客户的 EC2 跑得好不好"，而不是"怎么从 EC2 团队抢预算"

### 第 4 节：14 Leadership Principles 的精确作用

重点拆 4 条与"机制能跑"直接相关的：

- **Customer Obsession**：让团队把外部客户而不是内部 KPI 放第一
- **Ownership**：你为你的服务的长期结果负全责（包括"是否带动了底层消耗"）
- **Frugality**：限制资源能强迫团队优化体验而不是堆人头
- **Insist on the Highest Standards**：内部服务质量也要被严苛要求 — 这是为什么 EC2 团队不能"自降标准"应付内部消费者

每条引用 amazon.jobs 官方页 + 一个公开访谈中高管对该 LP 的解释。

### 第 5 节：Input Metrics vs Output Metrics

- Amazon 内部考核重输入指标（你能控的）轻输出指标（结果指标）。引用：Colin Bryar & Bill Carr《Working Backwards》第 3 章 + Bezos 2016 致股东信
- 论点：attributed revenue 之所以不会变成"团队互相甩锅"，是因为团队本来就被以"它做了什么动作"而非"它收到了多少钱"来评价

### 第 6 节：6-Pager & Disagree and Commit

- 会议读 6 页备忘录、决策后"不同意但承诺"
- 引用：Bezos 2016 致股东信（aboutamazon.com 原文存档）
- 论点：当机制设计有争议时（如 EC2 团队该划给 EKS 多少利润），这套决策文化让事情能落定而不是无穷扯皮

### 第 7 节：机制失效 / 反例

- 这套 OS 也有副作用：例如团队过度独立导致服务碎片化（AWS 控制台 UI 不统一臭名昭著） — 引用 Last Week in AWS 或 Hacker News 讨论
- 例如 EFS 2015 年公布到 2016 年才 GA — STL 模式下小团队推大项目的痛点
- 这一节不长但必须有

### 收尾：把这件事和本质问题对齐

一两段，点出"组织设计先于机制设计" — 没有 API Mandate + 2-Pizza + STL 的前置投入，attributed revenue 就只是一个会计游戏。

## 必须包含的源（至少）

- Steve Yegge 2011 Google+ rant（archive.org 链接，Tier 2）
- Bezos 2018 Forum on Leadership Q&A YouTube 视频（Tier 1）
- Colin Bryar & Bill Carr《Working Backwards》一书（具体章节，Tier 2）
- Brad Porter「Single-Threaded Leadership」LinkedIn 长文（Tier 2）
- amazon.jobs 14 LPs 官方页（Tier 1）
- Bezos 2016 致股东信 aboutamazon.com 原文存档（Tier 1）
- Jeff Wilke 或 Andy Jassy 一个公开访谈（Tier 1 或 Tier 2 视渠道）
- Werner Vogels 博客一篇相关帖子（Tier 2）

## 字数

约 5000 中文字。

## 提交

直接把完整 Markdown（含 YAML front matter + 正文 + 参考资料表）作为你的最终输出。不要带任何解释性前后文。
