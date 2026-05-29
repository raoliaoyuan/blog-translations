# 任务：重写第 2 篇《组织与文化底座》

这是一次**重写任务**。之前由 Gemini 生成的初稿被另一个模型（Codex）核对后发现严重问题：大量 URL 编造、关键论断无源、把外部公开机制外推为内部财务机制。你的任务是从零重写，严格避免那些问题。

## 重写硬约束

1. **绝不引用未亲自核实存在的 URL**。每条引用的 URL 必须真实可访问。
2. **AWS 内部 Attributed Revenue / Transfer Pricing / P&L / KPI / 内部结算比例**这些细节没有合规公开来源。你的写法必须：
   - 引用第 1 篇已经建立的论点（外部 attribution 机制 + 强 P&L 团队文化 + Yegge 转述的 service interface mandate），把"内部存在 attributed revenue"作为**合理推断**而不是断言
   - 凡是属于"内部计费如何分配"的具体论断，必须明确写"未找到公开来源支持"或改为"可推测"
3. **Working Backwards / 14 LPs / 2-Pizza / STL 等 Amazon 组织实践都有公开来源**，这部分要扎实写，不要为了短而省略源。
4. 不要为"组织实践如何精确支撑内部计费机制"硬造因果链。可以用"组织设计为这套机制提供了必要前提"这种克制措辞。

## 必读：上一版的问题清单

下面是 Codex 对 Gemini 初稿的 review report。所有标 ❌ 的引用必须删除或替换。所有"未引用但需要源"的句子要么补源要么删掉/弱化。

```
<INSERT_REVIEW_HERE>
```

## 上一版初稿（仅供参考，了解被批评的对象。不要复用其中的编造引用）

```
<INSERT_DRAFT_HERE>
```

## 文章结构（参考第一版，但你可以调整）

### 开篇钩子
回顾第 1 篇结尾：机制听起来很美，但为什么 Amazon 能跑通？答案在它的组织设计。

### 第 1 节：Bezos 2002 API Mandate
- Steve Yegge 2011 实名 rant（用现存可访问的 GitHub gist `chitchcock/1281611`，不要用 `chadaustin/1395230`）
- 论点：service interface mandate 为后续的内部 attribution 提供了接口边界

### 第 2 节：2-Pizza Team & Single-Threaded Leader
- 用 AWS Executive Insights 官方页（如 amazon-two-pizza-team）+《Working Backwards》一书
- 论点：清晰边界 + 责任主体让"账"有归属

### 第 3 节：Working Backwards & PR-FAQ
- 用 Werner Vogels 2006 年 All Things Distributed 帖（确认可访问后引用）+《Working Backwards》同名书
- 论点：客户语言驱动设计，团队不易陷入内部博弈

### 第 4 节：14 Leadership Principles 的精确作用
- 用 amazon.jobs 官方 LP 页
- 拆 4 条：Customer Obsession / Ownership / Frugality / Insist on the Highest Standards
- 每条解释对"机制能跑"的具体贡献，**不要硬造因果**

### 第 5 节：Input Metrics 文化
- 用 Bezos 2016 致股东信（aboutamazon.com 原文存档）+《Working Backwards》
- 删除"WBR 80% 时间讨论输入指标"这种无源具体数字
- 论点：考核动作而非账面收入，降低团队互相博弈的动力

### 第 6 节：Disagree and Commit
- 用 Bezos 2016 致股东信
- 论点：争议有终结机制

### 第 7 节：机制失效 / 反例
- 必须存在但要真实可考
- 候选：AWS Console UX 不统一（用 Last Week in AWS 具体可访问文章，不要用编造的 HN 链接）
- 候选：Amazon EFS 从公布到 GA 的时间长（AWS What's New 公告 + 官方时间线）

### 收尾
组织设计先于机制设计；这套 OS 是机制的必要前提。

## 必须包含的源（必须每条都真实可访问）

- Steve Yegge gist `chitchcock/1281611`（Tier 2）
- Werner Vogels 2006 All Things Distributed《Working Backwards》帖（Tier 2）
- AWS Executive Insights two-pizza team 页 或 类似 AWS 官方对该实践的描述（Tier 1）
- amazon.jobs Leadership Principles 页（Tier 1）
- Bezos 2016 致股东信 aboutamazon.com 原文存档（Tier 1）
- Colin Bryar & Bill Carr《Working Backwards》一书（Tier 2，可注明章节）
- 至少 2 个其他可访问 Tier 1 源（如 AWS 官方 blog、Andy Jassy 真实可访问的访谈 transcript）

## 字数

约 5000 中文字。

## 输出格式

完整 Markdown（YAML front matter `part: 2` + 正文 + 参考资料表）。**直接输出最终结果，不要解释性前后文，不要在前后加 review report 引用。**

如果某个论点你查不到合规来源，直接在文中说"未找到公开来源支持"，不要硬造引用。这是最重要的规则。
