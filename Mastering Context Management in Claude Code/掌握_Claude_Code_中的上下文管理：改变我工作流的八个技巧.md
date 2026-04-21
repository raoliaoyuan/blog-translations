> 作者：Manav Ghosh
> 发布日期：2026-01-30
> 原文链接：https://medium.com/@manav-ghosh/mastering-context-management-in-claude-code-8-tips-that-changed-my-workflow

# 掌握 Claude Code 中的上下文管理：改变我工作流的八个技巧

> "上下文工程（context engineering）对企业 AI 成功的重要性，超过模型选型。" —— CData Research

如果你在用 Claude Code，大概已经遇到过这种沮丧：AI 逐渐忘记了你在构建什么。关键在于：管理上下文不是把更多文件塞给 Claude，而是要做有策略的上下文工程。

在用 Claude Code 完成生产级项目的几个月里，我总结出了以下八个技巧，它们大幅提升了我的开发效率。

---

## 1. 用 `CLAUDE.md` 作为北极星

把 `CLAUDE.md` 当作项目的"宪法"，放在根目录，内容包括：

- 架构概览
- 开发命令
- 模块结构
- 常见工作流
- 关键约束

Claude Code 会自动读取该文件，以此理解代码库。引入这个实践后，我的代码偏差率（misaligned code）下降了 60%。

---

## 2. 按阶段组织对话

不要把调研、规划和实现混在一次对话里完成。拆分步骤：

- **第一阶段**：调研与探索（使用 `/explore` 或 Task 工具）
- **第二阶段**：规划（复杂功能使用 `EnterPlanMode`）
- **第三阶段**：实现（专注的编码会话）

这种顺序化方式能防止上下文漂移（context drift），让 Claude 始终与你的意图保持对齐。

---

## 3. 用调研文件管理外部知识

构建需要外部数据的功能时，采用"先调研、后实现"的工作流：

- 让 Claude 通过 MCP 工具完成调研
- 将调研结果保存为 JSON 文件
- 实现阶段引用这些文件

这种模式保持上下文干净，让 Claude 每次只专注一件事。

---

## 4. 使用精确的文件引用

不要说"更新认证逻辑"，而要说"更新 `src/auth/login.ts:45–67` 中的登录流程"。包含文件路径和行号，能确保 Claude：

- 先读取正确的文件
- 理解已有的代码模式
- 不会误改其他文件

这个简单做法消除了 80% 的"改错文件"问题。

---

## 5. 对 MCP Server 采用渐进式披露（Progressive Disclosure）

大多数开发者在这里犯错：他们把找到的每个 MCP Server 都接进来，用根本用不着的工具把 Claude 的上下文窗口塞满。

**渐进式披露的做法：**

从最小集开始。只连接当前任务必需的 MCP Server：

- 构建数据管道？→ 只连接 PostgreSQL MCP
- 添加通知功能？→ 需要时再连接 Slack MCP
- 自动化部署？→ 在该阶段才连接 GitHub MCP

**为什么重要**：每个 MCP Server 都会向 Claude 的上下文添加工具描述。连接 5 个以上的 Server，Claude 在开始你的任务之前就要处理 50 多条工具说明，这是对上下文的浪费，也会拖慢响应速度。

**我的工作流：**

1. 只保持核心 Server：默认只连接 2–3 个必要的 Server（文件系统、git 工具）
2. 按需添加：只在需要时连接专用 Server
3. 确认连接状态：运行 `claude mcp list` 查看当前活跃的 Server
4. 用完即断：当该项目阶段完成后，断开对应 Server

**实际案例**：构建电商结账系统时，我在支付集成阶段连接了 Stripe MCP，完成后断开；切换到商品目录开发时连接 Shopify MCP 用于库存管理。这样 Claude 能专注于当前任务，而不会在我构建商品列表 UI 时不断提出支付处理方面的建议。

另一个场景：在网页抓取项目中，我只在自动化阶段连接 Puppeteer MCP。抓取功能完成后断开，改接 Slack MCP 用于通知。构建告警系统时，浏览器自动化工具留在上下文里没有任何意义。

结果：响应速度提升 40%，对话更聚焦、更清晰。

---

## 6. 用子智能体（SubAgent）保留主上下文

这是大多数开发者错过的关键：子智能体（SubAgent）运行在各自独立的上下文窗口中。

当你让 Claude 探索大型代码库或调研复杂话题时，所有这些探索都会消耗主对话的上下文。应对方法是：使用 Task 工具将这些任务委派给专用的 SubAgent。

**SubAgent 如何节省上下文：**

每个 SubAgent 独立运行，只把最终结果返回给主对话。所有中间的文件读取、搜索和探索都发生在 SubAgent 的上下文里，不影响主上下文。

**何时使用 SubAgent：**

- Explore Agent：「找出代码库中所有 API 端点」→ 只返回列表，不是 50 多次文件读取的过程
- Plan Agent：「为用户认证设计架构」→ 只返回方案，不是完整的调研过程
- Bash Agent：复杂的 git 操作或构建流程 → 只返回结果，不是每条命令的输出
- general-purpose Agent：多步骤调研任务 → 返回综合后的结论，不是原始数据

**真实案例**：我在调试一个微服务架构的性能问题。我没有让 Claude 在主对话中逐一读取 20 多个服务文件，而是委派了这个任务：

> 「使用 Explore agent 找出 services 目录中所有数据库查询的实现，识别慢查询。」

SubAgent 完成了所有繁重工作（读文件、分析查询、执行 grep 搜索），返回了一份包含 5 个问题查询的简洁摘要。我的主上下文始终专注于实现修复方案。

**数字对比**：不使用 SubAgent，这次探索会消耗约 3 万个 token；使用 SubAgent，只消耗约 2000 个 token（仅摘要部分）。节省了 93% 的上下文。

**进阶用法**：对于不需要阻塞主对话的任务，可以用 `run_in_background: true` 在后台运行 SubAgent。SubAgent 在后台探索测试覆盖率时，你可以继续在主对话中实现功能。

---

## 7. 用 Skill 承载领域专属上下文

Claude Code 的 Skill（技能）是预加载的专家，自带上下文和专业知识。与其每次解释完整的工作流，不如直接调用 Skill，让它处理领域专属的工作。

**Skill 为何能节省上下文：**

每个 Skill 都是封装好的工作流，内置领域知识。使用 `/commit` 时，你不需要解释：

- git 最佳实践
- commit message 规范
- 哪些文件需要暂存（stage）
- 如何处理 pre-commit hook

Skill 自己知道，每次交互省去数千个 token。

**我日常使用的 Skill：**

**1. 代码审查与测试（`/review`、`/test`）**

不再解释"分析认证模块，检查安全问题，提出改进建议，并编写单元测试"，直接：

```
/review src/auth/login.ts --security --suggest-tests
```

Skill 了解代码模式、安全漏洞和测试最佳实践。我用它审查 pull request 时，它识别出了边界情况、建议了错误处理改进，并在无需我指定测试框架的情况下生成了对应测试。每次代码审查节省约 5000 个 token。

**2. 测试生成（`/test`、`/coverage`）**

不再解释"为支付服务编写单元测试，包含边界情况，mock 外部 API，确保 80% 覆盖率"，直接：

```
/test src/services/payment.ts --mocks --coverage 80
```

Skill 理解测试框架、mock 模式和覆盖率要求。我用它做测试驱动开发时，它生成了包含完整 setup/teardown、mock 实现和断言模式的测试套件。每个测试套件节省约 5000 个 token。

**3. Git 操作（`/commit`）**

不再引导 Claude 一步步完成 git status、分析变更、撰写 commit message、处理暂存，直接：

```
/commit
```

Skill 处理整个工作流。在最近一次跨 12 个文件的 API 重构中，Skill 自动分析了变更、将相关修改归组，并生成了格式规范的 commit。节省约 8000 个 token。

**4. 前端设计（`/frontend-design`）**

构建 UI 组件时，不再提供设计系统文档、调色板和布局原则，直接：

```
/frontend-design create a dashboard card component with metrics
```

Skill 预加载了设计最佳实践和现代 UI 模式。我用它构建数据分析看板时，它生成了带有正确样式和无障碍访问（accessibility）支持的生产级 React 组件。每个组件节省约 1 万个 token。

**战略优势：**

Skill 本质上是上下文压缩。这就像雇用已经懂行的专家，而不是每次从头培训通才。

使用 Skill 之前：

- 「分析支付模块的安全问题，提出改进建议……」
- 「生成带 mock 的测试用例，覆盖率达到 80%……」
- 「写一条 commit message 总结所有变更……」

使用 Skill 之后：

- `/review src/services/payment.ts --security`
- `/test src/services/payment.ts --mocks --coverage 80`
- `/commit`

每个工作流节省 60–70% 的上下文。

**最佳实践**：把重复性工作流映射到 Skill 上。如果同一件事做了超过 3 次，要么使用已有的 Skill，要么创建一个自定义 Skill。上下文管理变得轻松后，你会感谢现在的自己。

---

## 8. 切换任务时清空上下文

在无关任务之间切换时，开启一个新对话。试图跨多个功能维护上下文会导致：

- AI 对当前目标产生混淆
- 不同模块的代码模式相互干扰
- 因上下文膨胀（context bloat）导致响应变慢

把它想象成切换项目时清空桌面——这对保持专注至关重要。

---

## 结语

Claude Code 中的上下文管理，不是把所有东西都喂给它，而是在正确的时机喂给它正确的内容。把上下文当作战略资源，而不是垃圾桶。

落实这八个实践后，我观察到：

- 开发周期加快 40%
- 实现偏差减少 65%
- 跨模块代码一致性提升 3 倍
- 通过精细化 MCP 管理，上下文相关错误减少 50%
- 通过 SubAgent 委派，可用于实现的上下文增加 70%
- 通过策略性使用 Skill，上下文压缩率达 60%

你在 Claude Code 上有哪些使用心得？有什么上下文管理策略对你有效？欢迎在评论区分享。
