<以下内容请先在上下文中加载 _shared-header.md 的所有约束，然后执行下面的具体任务>

# 任务：撰写第 1 篇《机制本身》

## 核心论点

AWS 用 **Attributed Revenue（影子收入 / 关联归属收入）+ Transfer Pricing（内部转移定价）** 解决了一个非常具体的组织难题：高阶服务（EKS、Lambda、Bedrock）虽然在外部账单上只能收一点点"服务费"，但它们带动的 EC2/EBS/网络消耗在内部财务系统中会被归属到自己头上，从而获得真实的业绩与利润分成。

## 文章结构（建议）

### 开篇案例：EKS 代客拉起的 EC2 节点

- 外部账单视角：EKS 控制平面 `$0.10/h` 计入 `AmazonEKS`；Node EC2 + EBS + Data Transfer 全部计入 `AmazonEC2`
- 引用：AWS 官方 EKS Pricing 页 + AWS Billing 文档关于 cost allocation 的部分
- 提出"如果只看账单，EKS 团队只赚 $0.10/h" 的悖论

### 第 2 节：AWS 内部财务系统怎么解这个悖论

- 引入 Attributed Revenue 概念：EC2 收入被打上"EKS-Driven"标签
- 引入 Transfer Pricing：EC2 团队把该部分利润按比例划给 EKS 团队
- 这两个机制在 AWS 内部如何被讨论 — 找 Andy Jassy / Werner Vogels / Charlie Bell 公开访谈中提及"how we measure service teams"的部分
- 引用 Brad Porter（前 AWS VP Robotics，写过 STL 实践）或 James Hamilton 的博客中关于 service-level accounting 的描述

### 第 3 节：对照案例 — Lambda on Firecracker

- Lambda 团队不拥有 EC2 容量池，但 Firecracker 跑在 EC2 之上
- 引用：Marc Brooker 的论文 / re:Invent 2022 Firecracker deep dive / AWS re:Invent SVS401 / SVS404
- 说明 Lambda 团队的"业绩"如何被 attribute（它的 invocation 量驱动的 EC2 消耗）

### 第 4 节：政策事件证据 — 2019 EKS 集群费降价

- 2019 年某月 EKS 集群费从 $0.20/h 降到 $0.10/h
- 引用：AWS What's New 公告 / Werner Vogels 博客 / Jeff Barr 公告博客
- 论点：能这样降价的底气恰恰来自 attributed revenue — 控制平面"赔本"无所谓，重要的是带动的 EC2 消耗

### 第 5 节：产品形态差异印证机制

- Fargate launch type：on-EC2 vs on-ECS 的定价结构差异
- 引用 AWS Fargate Pricing 官方页 + AWS docs about launch types
- Savings Plans 对 EKS Node 和 Fargate 的不同抵扣行为 — 引用 AWS Billing 文档

### 第 6 节：机制失效 / 公开质疑

- 找一个公开案例：内部团队对 attribution 边界的争议
- 候选：CloudWatch 计费曾被 Corey Quinn 多次吐槽是"独立计费实体"（Last Week in AWS），暗示其团队 P&L 独立性过强、不愿被 attribute
- 候选：Data Transfer 计费长年不变背后的部门博弈
- 这一节不需要长，但必须存在

### 收尾：把这件事和本质问题对齐

一两段，点出 attributed revenue 和 transfer pricing 是把"客户价值链上的协同"翻译成"内部利益对齐"的具体手段。

## 必须包含的源（至少）

- AWS EKS Pricing 官方页（Tier 1）
- AWS Billing & Cost Management 文档关于 cost allocation tags（Tier 1）
- AWS Fargate Pricing 官方页（Tier 1）
- AWS Savings Plans 文档（Tier 1）
- Marc Brooker 博客或论文一篇（Tier 2）
- Werner Vogels《All Things Distributed》一篇（Tier 2）
- Last Week in AWS 一篇 Corey Quinn 文章（Tier 2）
- 一个 re:Invent session 视频 URL（Tier 1）

## 字数

约 5000 中文字。

## 提交

直接把完整 Markdown（含 YAML front matter + 正文 + 参考资料表）作为你的最终输出。不要带任何解释性前后文。
