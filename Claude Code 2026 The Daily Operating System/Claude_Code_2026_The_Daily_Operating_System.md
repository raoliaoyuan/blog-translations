> 作者：Rick Hightower
> 发布日期：2026-04-06
> 原文链接：https://medium.com/@rickhigh/claude-code-2026-the-daily-operating-system-top-developers-actually-use

# Claude Code 2026：顶尖开发者实际使用的日常操作系统

精确的五部分模型、10 分钟例程、斜杠命令（slash commands）、上下文卫生（context hygiene）技巧、收尾仪式，以及资深用户依赖的精英工作流（2026 年 4 月更新）

---

从终端辅助工具到始终在线的智能体（agent）平台。精确的五部分模型、最新斜杠命令、上下文卫生技巧，以及 Anthropic 资深用户依赖的收尾仪式。更新至 2026 年 4 月 6 日。

将本文保存为日常参考。这是你的 Claude Code 日常指南。

大多数团队仍然把 Claude Code 当作更智能的自动补全工具。

那些交付更快的团队把它当作操作系统。

2025 年底至 2026 年第一季度的真实故事，不在于某个斜杠命令或模型发布，而在于一套可复用的 AI 辅助开发操作模型的成形。该模型有五个部分：

1. 保持始终在线的上下文精简。
2. 将重复流程转化为技能（skills）或命令。
3. 保护活跃会话免受上下文污染（context pollution）。
4. 在有明确监督和隔离的前提下并行化工作。
5. 让防护机制去除噪音，而不是去除判断力。

## 目录

- 你的 10 分钟 Claude Code 日常例程
- 你现在就需要用的最新功能（/powerup、/insights、/loop、Channels）
- 随意型 vs. 专业型 vs. 精英型工作流
- 顶尖用户实际如何工作（Boris、Karpathy、Anthropic）
- 四大内置技能式命令
- 上下文卫生是隐藏的效率乘数
- 审批疲劳（Approval Fatigue）与 Auto Mode
- 常见陷阱及修复方法
- 可靠性才是真正的功能
- 从日常使用到精通
- 参考资料

---

## 你的 10 分钟 Claude Code 日常例程

如果你想让 Claude Code 每天都能发挥作用，而不只是偶尔令人印象深刻，那就从一套短到能在真实工作周中坚持下去的例程开始。

### 早晨准备

- **重新锚定代码库。** 打开分支，扫描 `CLAUDE.md`，在让 Claude 编辑任何内容之前确认项目的测试和审查命令。
- **让 Claude 先规划再编写。** 要求它说明各阶段、可能涉及的文件、风险和验收标准。
- **在开始之前决定这个任务适合单个会话还是多个隔离的 git 工作树（worktrees）。**
- `/memory`
- `/loop "run tests and summarize failures" every 30m`

### 工作期间

- **保持主线程干净。** 对于支线探索，使用旁路频道（side channels）、分叉（fork）或全新会话，而不是把所有内容都堆进一个会话记录（transcript）里。
- **把任何重复两次的操作转化为技能、斜杠命令或可复用的代码库约定。** 使用子智能体（subagents）保持上下文紧凑和聚焦。
- **随时验证。** 测试、浏览器检查、截图和二次审查是工作的一部分，而不是收尾步骤。

### 收尾仪式

- 对遗留问题、重复代码和未完成的备注执行一次清理。
- 将下次会话默认需要知道的内容更新到 `CLAUDE.md` 或 memory 中。
- 终止过期的 loop、关闭嘈杂的会话，并为明天留下一份清晰的交接说明。

**今天就做**

- 把一条特定于代码库的规则加入 `CLAUDE.md`，而不是在对话中重复说。
- 为一项真正令人烦恼的任务（如测试、截图或 PR 摘要）启动一个周期性循环（recurring loop）。

---

## 你现在就需要用的最新功能（2026 年第一季度）

这两个命令很容易被忽视，但它们现在是 Claude Code 中杠杆效应最高的"元"功能之一：一个告诉你哪些功能你还没在用，另一个告诉你是什么在拖慢你的速度。

### /powerup：终端内交互式教程

`/powerup` 是 Claude Code 内置的引导/教程系统。它通过交互式课程（通常附有终端动画演示）教你大多数人从未发现的功能。

适合在以下情况使用：

- 刚更新了 Claude Code 并想了解新内容
- 感觉自己只用了产品的 20%（hooks、子智能体、rewind、工作树、技能、MCP 等）
- 想要一个不需要离开终端的自闭环学习方式

它的核心价值不在于命令列表，而在于它端到端地演示工作流，让你可以立即复用。

### /insights：过去约 30 天会话的 HTML 报告

`/insights` 分析你本地的 Claude Code 会话历史，并生成一份交互式 HTML 报告（通常保存至 `~/.claude/usage-data/report.html`）。

报告通常展示：

- 项目和会话概览
- 工具使用模式及时间/token 流向
- 反复出现的摩擦点（你卡住、重启或放弃会话的地方）
- 个性化的"哪些有效 / 哪些在阻碍 / 快速胜利 / 雄心勃勃的工作流"建议

实际使用方式：运行 `/insights`，取出排名前 1–3 的摩擦点，然后通过将规则提升到 `CLAUDE.md`、创建技能或添加 hook 来消除重复的手动工作，逐一修复。

落后最快的方式就是继续把 Claude Code 当作 2025 年的纯终端助手来用。以下是 2026 年第一季度改变日常工作流影响最大的几个界面。

### 关于两个细节，比头条功能更重要

第一，`/loop` 之所以强大，是因为它足够轻量。它不是云端调度器，而是活跃会话内的轻量级周期提示，非常适合在你主动工作时进行测试轮询、审查提醒和周期性检查。

第二，Remote Control 和 Channels 改变了工作日的形态。一旦同一个会话可以从手机、浏览器或另一台机器恢复，Claude 就不再只是一个终端 tab，而开始感觉像一个持久的工作平面。

**今天就做**

- 添加一个每天能省去一次手动检查的 `/loop` 任务。
- 在真正需要用到之前，先在一个安全的代码库上测试 Remote Control。
- 配置 Channels。

### Channels：iMessage、Telegram、Discord（研究预览版）

"Channels"是一个研究预览版功能，允许你从聊天应用发送消息到正在运行的 Claude Code 会话，适合在不切换回终端的情况下启动任务、询问状态或发送快速指令。

**重要心智模型**：Channels 是消息传输机制，而不是独立的智能体。你仍然在与 Mac 上同一个本地会话交互，使用同样的代码库检出和同样的工具访问权限。如果会话停止，频道也随之停止。

**团队为何关注（以及 Slack/Telegram 在哪里适用）**

- Slack/Telegram/Discord 是团队工作流的实用选项：共享频道、跨平台访问，以及用于轻量级"调度"（如"运行测试套件"、"汇总失败"、"起草 PR 说明"）的熟悉聊天界面。
- iMessage 是 Apple 重度用户最快的个人配置：无需 bot token、无需外部 webhook 服务，是从 iPhone/iPad/Mac ping 正在运行会话的极低摩擦方式。

**iMessage 配置快速指南**

前提条件：Claude Code v2.1.80+ 且已安装 Bun。

1. 为你的终端应用授予"完全磁盘访问"权限（需要读取 `~/Library/Messages/chat.db`）。我不会撒谎，这感觉有点不对劲。
2. 在 Claude Code 会话内安装插件：

```
plugin install imessage@claude-plugins-official
```

3. 启用 channels 后重新启动：

```
claude --channels plugin:imessage@claude-plugins-official
```

4. 冒烟测试：从任意 Apple 设备给自己发消息（self-chat）。
5. 第一次回复会触发一次性的 macOS 提示（"终端想要控制'信息'"）——批准即可。

**需要说明的操作限制**

- 会话必须保持运行（关闭终端后频道下线；下线期间发送的消息通常会丢失）。
- 权限提示仍会阻塞：如果会话需要批准，它会暂停直到你在本地确认。
- iMessage 仅限 macOS（Telegram/Discord 风格的频道是跨平台的）。

---

## 随意型 vs. 专业型 vs. 精英型 Claude Code 工作流

并非每种强大的工作流看起来都相同，但操作模型正变得越来越容易分类。

重点不是模仿某种人设，而是采纳每种模式共有的纪律：精简上下文、明确规划、隔离执行、真实验证。

---

## 顶尖用户实际如何工作：Boris、Karpathy 和 Anthropic 的模式

Anthropic 公开的 harness 设计理念很清晰：先规划再编辑、保持上下文精简且任务导向、使用评估器（evaluator）而非信任生成器来验证、让子智能体使用独立上下文，并将权限视为策略。截至 2026 年 4 月，公司大多数代码由 Claude Code 编写，但工程师扮演的是架构师、审查者和编排者角色，而不是逐行的代码录入员。

**Boris Cherny 的工作流**：在独立 git 工作树上同时运行五个或更多并行 Claude 会话，使每个智能体都有安全的写入空间。每个复杂任务在执行开始之前都从结构化规划启动。`CLAUDE.md` 被视为活的契约，持续更新以便未来会话默认更聪明地启动。子智能体被对抗性地使用（"让子智能体互相博弈"），让多个具有不同审查角色的智能体在人工接受之前相互质疑对方。结果是三层保护：在隔离检出间并行实现、编辑前明确规划、合并前对抗性审查。

**Karpathy 的工作流**：左侧是智能体，右侧是 IDE。Claude 处理首次实现，而人工保持审查者、规格撰写者和编辑者的角色，掌握架构控制权并捕捉错误方向。两种模式汇聚到同一个教训：人工角色从编写代码转向指导、验证和塑造智能体工作。

工作树隔离是核心基础单元：使用 `claude --worktree feature-auth`（或 `-w`）创建隔离检出。渐进式披露（progressive disclosure）优于指令囤积：`CLAUDE.md` 保存始终为真的上下文，rules 处理狭窄的文件约束，skills 封装可重复的流程，memory 存储已学事实。每一层都比一大段指令更小、更有针对性。

---

## 四大内置技能式命令

Claude Code 现在内置了四个"技能式"命令，展示了系统的完整能力。每个命令都解决了一个此前需要手动编排（或干脆放弃）的问题。

### /simplify

实现功能或修复 bug 后，运行 `/simplify` 来生成并行审查智能体：

- **代码复用**：减少重复
- **代码质量**：发现 bug、不清晰的逻辑、可维护性问题
- **效率**：识别性能改进点

这些智能体并发运行、汇总发现并应用修复。你可以聚焦审查范围，例如 `/simplify focus on memory efficiency`。

### /batch

最雄心勃勃的内置命令。给 `/batch` 一个变更描述，它会：

1. 研究代码库以理解范围
2. 将工作分解为 5–30 个独立单元
3. 提交计划供批准
4. 为每个单元生成一个智能体，每个智能体在隔离的 git 工作树中运行
5. 让每个智能体实现、测试并提交 PR

示例：`/batch migrate src/ from Solid to React`。

这就是工作树隔离成为一等基础单元的场景：每个智能体在自己的分支上工作以避免合并冲突。权衡在于分解质量——在批准前审查计划。

### /debug

当 Claude Code 本身出现问题时，`/debug` 读取会话调试日志并诊断问题。你可以传入聚焦提示，例如 `/debug why is the Bash tool failing?`。这非常重要：如果你遇到 Claude 的问题，先调用 `/debug` 启动调试日志，再描述你的问题。它了解 Claude 以及如何调试 hooks、memory、上下文、子智能体、技能等方面的问题。

### /claude-api

当你的项目导入 `anthropic`、`@anthropic-ai/sdk` 或 `claude_agent_sdk` 时，此命令自动激活。它加载特定语言的 API 参考材料（工具使用、流式传输、批处理、结构化输出和常见陷阱），让 Claude 无需你询问就能"理解 API"。

---

这一逻辑延伸到官方文档之外。

更广泛的 Claude Code 生态系统现在包括：推动模型远离通用 AI 生成布局的前端设计插件、使用多个评估器而非一次粗暴清理的 simplify 式工作流、将重复代码整合为共享库的技术债处理例程，以及提交、问题整理乃至动态图形生成的自动化工具。其中一些工具是公开的，一些是市场包，一些被描述为团队内部习惯。共同的模式才是重点：重复的工作被转化为明确的软件。

这就是 Claude Code 从"提示"感觉转变为"环境设计"感觉的节点。

---

## 上下文卫生是隐藏的效率乘数

下一个问题不是能力，而是污染。

长期运行的会话会在太多无关讨论粘附到主会话记录时退化。一个旁路问题、一个纠错链、一次设计替代方案的迂回——很快模型就在试图保持主任务连贯的同时，背负着一块堆满过时或次要内容的杂乱白板。

这正是上下文卫生工作流如此重要的原因。

社区工作流中描述的 `/btw`、`/fork` 和 `/rewind` 等命令解决了同一问题的不同部分。`/btw` 是廉价的旁路频道，用于快速理解。`/fork` 是深度探索的真正分支。`/rewind` 是模型走向错误路径时的手术式重置，比起在原地争论更愿意直接移除损害。

这些不是便利功能，而是高级用户长期保持会话质量的方式。

### 上下文卫生工具包：/btw、/fork、/rewind

#### /btw：廉价、快速，且刻意受限

`/btw` 智能体利用主会话的提示词缓存（prompt cache）——它搭载已处理的 token，而不是重新发送整个上下文。实际上，这意味着你可以以极低的成本进行频繁的"状态检查"或"快速澄清"，且不污染主线程。

**刻意设计的约束**：

- 仅单轮（一个问题，一个回答）
- 只读（无编辑、无命令、无产物）
- 不访问新工具/文件（它无法读取主会话尚未见过的内容）

当你需要的不只是单个回答，或需要 Claude 真正去做某件事时，请使用 `/fork`。

#### /fork：深度探索而不污染主会话

分叉（fork）创建一个继承分叉点之前会话历史的新会话，同时原始会话保持不变。

- 在会话内：`/fork`
- 从 CLI（例如在另一个终端打开）：`claude -r "session-name" --fork-session`

分叉实际上是运行中进程的复制：你保留了文件读取历史、决策和已发现的模式，因此可以立即探索替代方案（如 SSE vs WebSockets），而无需花费多轮重新解释上下文。

#### /rewind：走错方向时的手术式状态恢复

`/rewind` 是当污染已经在线程中时使用的工具；它移除错误上下文，而不仅仅是隔离它。

- 通过 `/rewind` 运行，或按两次 Esc。

实用变体：

- `/compact`：就地压缩当前上下文窗口（保持运行，丢弃原始历史）
- `/rewind summarization`：回滚到先前的检查点（上下文错误/受污染时最佳）

**快速选择指南**

| 场景 | 使用 |
|------|------|
| 快速问题 / 非干扰性检查 | `/btw` |
| 需要文件/工具访问或并行替代方案 | `/fork` |
| 方向错误 / 上下文受损 | `/rewind`（或 Esc, Esc 撤销最后一次更改） |
| 上下文太大（但没有错误） | `/compact` |

---

同样的逻辑在多智能体工作中再次出现。

一旦任务足够大，单个会话记录就成了错误的容器。大型迁移、广泛重构、多部分文档和全库清理都受益于分解。一个主导智能体制定计划、将工作拆分为单元并定义验收标准。子智能体或并行会话执行有边界的片段。隔离工作树或隔离环境阻止这些片段在主导智能体将它们合并回主线之前相互覆盖。

这就是批处理式工作流和智能体团队的重要意义。它们之所以有价值，不仅仅是因为并行，而是因为它们阻止并行工作退化为上下文蔓延和文件冲突。

---

## 审批疲劳是真实存在的，Auto Mode 是部分解决方案

Anthropic 2026 年 3 月 25 日关于 Auto Mode 的工程博文是最有用的 Claude Code 文档之一，因为它从一个令人不舒服的真相出发：大多数人在大多数情况下无论如何都会批准。

当这种情况发生时，权限系统仍然制造摩擦，但不再产生有意义的监督。Auto Mode 的存在就是为了减少这种失效模式。它使用基于模型的分类器（classifier）筛选操作，允许常规操作继续进行，同时升级看起来有风险的操作。

这是正确的方向，但成熟的解读不是"问题已解决"。

Anthropic 对其局限性很谨慎。该系统包括提示词注入（prompt injection）防御和基于会话记录的操作审查，但它并非全知。它无法将不受信任的环境变成受信任的环境，无法消除投毒指令或每一条多步攻击路径。在受信任的开发者环境中，它是一个更好的权衡，而不是针对受监管或高爆炸半径工作的通用答案。

这就是为什么日常工作流仍然需要明确的策略和验证。

Settings 文件、允许和拒绝规则以及企业策略的存在，是因为不同项目需要不同的风险包络。一个可复用的技能在 markdown 层面可能是安全的，而 shell 执行仍需要明确批准。快速编码流程可能仍需要一个专用的验证栈，在任何人信任结果之前运行 linter、测试、浏览器检查、截图和特定领域的验证。安全扫描属于同一类别。

换言之，自主性只有在被约束时才有用。

### 自动权限（Auto Mode）快速参考

**在 CLI 中启用**

使用 auto mode 标志启动 Claude Code：

```bash
claude --enable-auto-mode
```

进入会话后，按 Shift+Tab 循环切换权限模式。auto 选项仅在使用 `--enable-auto-mode` 启动后才会出现。

单次无头（headless）执行：

```bash
claude -p "refactor the auth module" --permission-mode auto
```

**将 Auto Mode 设为默认**

在 `settings.json` 中添加：

```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

在任何会话中，你仍可以用 Shift+Tab 切换回其他模式。

**查看默认分类器规则**

要查看分类器默认允许和阻止的内容：

```bash
claude auto-mode defaults
```

**禁用 Auto Mode**

- 用户层面：按 Shift+Tab 切换回 default、acceptEdits 或 plan 模式。
- 管理员层面（为所有用户禁用）：在托管设置中添加：

```json
{
  "disableAutoMode": "disable"
}
```

在 macOS 上，也可以通过 `defaults` 设置：

```bash
defaults write com.anthropic.claudecode disableAutoMode -string "disable"
```

---

## 从日常使用到精通

初学者的错误是把 Claude Code 当作"更好的自动补全"。中级者的错误是把它当作"带工具的超大提示词"。精通始于你意识到真正的技能单元是操作模型：上下文文件、harness 设计、子智能体、并行执行、memory 卫生和评估循环。

如果今天要围绕 Claude Code 构建一条认真的培训路径，各模块自然会成形。

从 `CLAUDE.md` 和提示词结构开始。开发者应学习如何构建全局规则和本地项目契约，然后衡量调优这些文件后模型的行为改善了多少。然后进入提示词优化：运行评估集，检查失败模式，重写系统上下文直到结果明显改善。再将 harness 和安全一起教，因为在没有边界的情况下给智能体更多工具，只是更快地制造错误。

从那里，进阶模块显而易见：

- 并行智能体团队及扇出/扇入（fan-out/fan-in）工作流
- 使用技能和子智能体的有范围上下文层级
- 具有明确成功指标的自动研究循环
- 具有清晰隔离边界的浏览器和计算机自动化
- 多模型路由以避免单一文化
- 工作区设计，使项目、技能和活跃产物保持清晰可读
- 安全审查、依赖健全性检查和 secret 纪律

这套课程很重要，因为它与工具的发展方向相符。

Claude Code 越来越不是关于"我现在怎么提示得更好？"，而更多是关于"我如何设计一个可复用的环境，让良好的智能体行为随时间复利增长？"这才是真正的精通层次。

---

## 常见陷阱及修复方法

大多数浪费的 Claude Code 时间来自一小撮可预测的错误。

这就是精英工作流比随意工作流看起来更平静的真正原因。他们不是在使用更多魔法，而是在消除更多阻力。

**今天就做**

- 从默认提示词中删除一条过时的指令，并将其移到正确的层次。
- 关闭一个嘈杂的会话，而不是把它的包袱拖到明天。

---

## 可靠性才是真正的功能

更深层的故事是可靠性。近期版本修复了内存泄漏、大负载处理、结构化输出稳定性、会话恢复连续性，以及 CJK、emoji 和天城文字（Devanagari）的文本正确性。Anthropic 不只是在扩大产品的功能面，还在硬化其周围的 harness。

近期关键新增：用于企业安全的 `disableSkillShellExecution`、用于更大 MCP 工具结果（最高 50 万字符）的 `_meta["anthropic/maxResultSizeChars"]`，以及多会话工作流的 `--resume` 修复。Anthropic 2026 年 3 月的 Code Review 发布文章描述了他们内部几乎每次 PR 都运行的多智能体审查系统。

Claude Code 真正的竞争优势不在于它能做更多，而在于它开始支持一种有纪律的方式——在不陷入自身复杂性的情况下做更多。

**将本文保存为你的 Claude Code 日常参考。**

---

## 延伸阅读

- Save Hours: Stop Repeating Yourself to Claude: Skills, Rules, Memory, and When to Use Each — 掌握 Claude Code：通过技能和定制化工具简化开发流程，提升生产力
- Stop Clicking "Approve": How I Killed Approval Fatigue with Claude Code 2.1 — 不再点击"批准"：我如何用 Claude Code 2.1 消除审批疲劳
- Claude Code Agent Teams: Multiple Claudes Working Together — Claude Code 智能体团队：多个 Claude 协同工作
- Put Claude on Autopilot: Scheduled Tasks with /loop and /schedule built-in Skills — 让 Claude 自动驾驶：使用 /loop 和 /schedule 内置技能执行计划任务
- The Claude Code Daily Handbook: Strategic AI Collaboration for Modern Developers — Claude Code 日常手册：面向现代开发者的战略性 AI 协作

### Claude Code 核心系列

- Claude Code Skills Deep Dive Part 1 — 编写智能体技能的基础及技能架构
- Claude Code Skills Deep Dive Part 2 — 继续编写技能
- Claude Code Agent Skills 2.0: From Custom Instructions to Programmable Agents — 技能和新内置技能的进展
- Claude Code Agent Teams: Multiple Claudes Working Together — 智能体团队简介
- Claude Code Hooks: Making AI Gen Deterministic — Hooks 简介
- Claude Code Hooks Implementation Guide: Audit System — 使用 Hooks 的示例
- Claude Code Rules: Stop Stuffing Everything into One CLAUDE.md — 组织规则和编码标准
- Claude Code Remote Control: Code From Your Phone — 使用 Claude Code 的 Remote 功能
- Claude Code Auto Mode: Escape Permission Fatigue — 逃离审批疲劳的 Auto Mode 简介
- Claude Code's Automatic Memory: No More Re-Explaining Your Project — 自动 Memory 简介
- Mastering Claude Code's /btw, /fork, and /rewind: The Context Hygiene Toolkit — 保持上下文干净和聚焦的工具
- Put Claude on Autopilot: Scheduled Tasks with /loop and /schedule built-in Skills — 新 cron 功能简介
- Stop Clicking "Approve": How I Killed Approval Fatigue with Claude Code 2.1 — 如何用 Claude Code 避免审批疲劳

---

## 参考资料

### Anthropic 官方文档与工程博文

- Anthropic, How Anthropic teams use Claude Code: https://claude.com/blog/how-anthropic-teams-use-claude-code
- Anthropic PDF, How Anthropic teams use Claude Code: https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf
- Anthropic, Claude Code auto mode: a safer way to skip permissions: https://www.anthropic.com/engineering/claude-code-auto-mode
- Anthropic, Code execution with MCP: Building more efficient agents: https://www.anthropic.com/engineering/code-execution-with-mcp
- Anthropic, Harness design for long-running application development: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Anthropic, Effective harnesses for long-running agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic, Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, Equipping agents for the real world with Agent Skills: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic, Building a C compiler with a team of parallel Claudes: https://www.anthropic.com/engineering/building-c-compiler
- Claude Code docs, Changelog: https://code.claude.com/docs/en/changelog
- Claude Code docs, Scheduled tasks: https://code.claude.com/docs/en/scheduled-tasks
- Claude Code docs, Remote Control: https://code.claude.com/docs/en/remote-control
- Anthropic docs, Claude Code memory: https://docs.anthropic.com/en/docs/claude-code/memory
- Claude Code docs, Slash commands: https://code.claude.com/docs/en/slash-commands
- Claude Code docs, Subagents: https://code.claude.com/docs/en/sub-agents
- Anthropic support, Using voice mode: https://support.claude.com/en/articles/11101966-using-voice-mode
- Anthropic support, Automated security reviews in Claude Code: https://support.anthropic.com/en/articles/11932705-automated-security-reviews-in-claude-code/
- Anthropic docs, Prompt engineering overview: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic docs, Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

### Boris Cherny 工作流资料

- Boris Cherny on X, How I use Claude Code: https://x.com/bcherny/status/2007179832300581177
- How Boris Uses Claude Code: https://howborisusesclaudecode.com
- Reddit mirror, bcherny, creator of Claude Code, shares how I use Claude Code: https://www.reddit.com/r/AI_Agents/comments/1q3xw15/bcherny_creator_of_claude_code_shares_how_i_use/
- InfoQ, Claude Code creator workflow: https://www.infoq.com/news/2026/01/claude-code-creator-workflow/
- Slashdot, Creator of Claude Code reveals his workflow: https://developers.slashdot.org/story/26/01/06/2239243/creator-of-claude-code-reveals-his-workflow
- FreeCodeCamp, Claude Code Handbook: https://www.freecodecamp.org/news/claude-code-handbook/
- Every, How to Use Claude Code Like the People Who Built It: https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it
- Paddo, 10 Tips from Inside the Claude Code Team: https://paddo.dev/blog/claude-code-team-tips/
- Jitendra Zaa, 10 Claude Code Tips from the Creator Boris Cherny: https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/
- YouTube, Building Claude Code with Boris Cherny: https://www.youtube.com/watch?v=julbw1JuAz0
- YouTube, His Claude Code Workflow Is Insane: https://www.youtube.com/watch?v=WpQZlKiy3zo
- YouTube, How to Use Claude Code the Boris Way: https://www.youtube.com/watch?v=1aCp9OT8rvw
- Get Push to Prod, How the creator of Claude Code actually uses Claude Code: https://getpushtoprod.substack.com/p/how-the-creator-of-claude-code-actually
- Lenny's Newsletter, Head of Claude Code: what happens: https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens
- Pragmatic Engineer, How Claude Code is built: https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built

### Karpathy 工作流与自动研究

- Andrej Karpathy on X, Claude agents on the left, IDE on the right: https://x.com/karpathy/status/2015883857489522876
- Business Insider, Andrej Karpathy says Claude Code is shifting his workflow: https://www.businessinsider.com/andrej-karpathy-claude-code-manual-skills-atrophy-software-engineering-tesla-2026-1
- Dev.to, Karpathy's Claude Code field notes: https://dev.to/jasonguo/karpathys-claude-code-field-notes-real-experience-and-deep-reflections-on-the-ai-programming-era-4e2f
- The AI Corner, Andrej Karpathy AI workflow shift: https://www.the-ai-corner.com/p/andrej-karpathy-ai-workflow-shift-agentic-era-2026
- Fortune, Andrej Karpathy's autoresearch: https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/
- Reddit, Andrej Karpathy's autoresearch breakdown: https://www.reddit.com/r/singularity/comments/1roo6v0/andrew_karpathys_autoresearch_an_autonomous_loop/
- YouTube, Autoresearch, Agent Loops and the Future of Work: https://www.youtube.com/watch?v=nt9j1k2IhUY
- YouTube, Karpathy on code agents and AutoResearch: https://www.youtube.com/watch?v=kwSVtQ7dziU

### 内部工具、技能与工作流报道

- YouTube, Copy These Claude Skills From The Claude Code's Creators: https://www.youtube.com/watch?v=AhXfI1rSUPc
- Reddit, Claude Code creator: introducing /simplify and /batch: https://www.reddit.com/r/ClaudeAI/comments/1rgthpn/claude_code_creator_in_the_next_version/
- LinkedIn, Introducing /simplify and /batch Skills for Claude: https://www.linkedin.com/posts/douglasfinke_claude-code-is-prepping-to-introduce-two-activity-7433531966244958208-Vb8Q
- MindStudio, What Is Claude Code /simplify and /batch?: https://www.mindstudio.ai/blog/claude-code-simplify-batch-commands/
- Mejba, Inside the Claude Code Team's Actual Workflow Tools: https://www.mejba.me/locale/en?next=%2Fblog%2Fclaude-code-team-workflow-tools
- Dev.to, How the creator of Claude Code uses Claude Code: https://dev.to/sivarampg/how-the-creator-of-claude-code-uses-claude-code-a-complete-breakdown-4f07
- CodingScape, How Anthropic engineering teams use Claude Code every day: https://codingscape.com/blog/how-anthropic-engineering-teams-use-claude-code-every-day

### 2026 年第一季度平台转变与始终在线功能

- MindStudio, Claude Code Q1 2026 Update Roundup: https://www.mindstudio.ai/blog/claude-code-q1-2026-update-roundup/
- MindStudio, Claude Code Q1 2026 Update Roundup 2: https://www.mindstudio.ai/blog/claude-code-q1-2026-update-roundup-2/
- CNBC, Anthropic Claude AI agent can use your computer: https://www.cnbc.com/2026/03/24/anthropic-claude-ai-agent-use-computer-finish-tasks.html
- 9to5Google, Claude can now remotely control your computer: https://9to5google.com/2026/03/24/claude-can-now-remotely-control-your-computer-and-it-looks-absolutely-wild-video/
- PCMag, Anthropic's Claude can now use your computer: https://www.pcmag.com/news/anthropics-claude-can-now-use-your-computer-to-complete-tasks-for-you
- Nicholas Rhodes, Claude Computer Use: Mac Setup Guide: https://nicholasrhodes.substack.com/p/claude-computer-use-mac-setup-guide
- LinkedIn, Claude Computer Use Now Available: https://www.linkedin.com/posts/a-banks_this-is-wild-claude-can-now-use-your-entire-activity-7442178633621893121-DAuV
- LinkedIn, Claude Code Introduces Auto Mode for Permission Handling: https://www.linkedin.com/posts/claude_new-in-claude-code-auto-mode-activity-7442269445970046976-GxwB
- Reddit, Claude Code now has auto mode: https://www.reddit.com/r/ClaudeAI/comments/1s2ok85/claude_code_now_has_auto_mode/
- LinkedIn, Nate Herkelman, Anthropic quietly dropped auto dream: https://www.linkedin.com/posts/nateherkelman_claude-code-just-dropped-memory-20-anthropic-activity-7442225812269068288-GWZ_
- Facebook, Claude Code auto-dream for memory consolidation: https://www.facebook.com/groups/aimlmalaysia/posts/2637089366691281/
- Zeabur, Paperclip: Run a Zero-Human Company with AI Agent Teams: https://zeabur.com/blogs/deploy-paperclip-ai-agent-orchestration
- LinkedIn, Nate Herkelman, Mission Control style dashboard for Claude Code: https://www.linkedin.com/posts/nateherkelman_this-one-tool-turns-claude-code-into-an-entire-activity-7443717127821303808-eprC
- Paddo, From Ralph Wiggum to /loop: The Absorption Continues: https://paddo.dev/blog/claude-code-loop-ralph-wiggum-evolution/
- Reddit, Anthropic just made Claude Code run without you: https://www.reddit.com/r/ClaudeAI/comments/1rna5mb/anthropic_just_made_claude_code_run_without_you/
- LinkedIn, Introducing /loop: https://www.linkedin.com/posts/julianalvarado_anthropic-quietly-released-an-openclaw-killer-activity-7436787507276656640-blm5
- Reddit, Anthropic shipped Remote Control for Claude Code: https://www.reddit.com/r/ClaudeAI/comments/1rfvv06/anthropic_shipped_remote_control_for_claude_code/
- YouTube, How to Use Claude Dispatch: https://www.youtube.com/watch?v=sP4GFZmR6wU
- YouTube, Claude Code Memory 2.0 With Unlimited Memory: https://www.youtube.com/watch?v=6pjETAf2XhU

### 语音模式及相关报道

- Deeper Insights, Anthropic Adds Voice Mode to Claude Code: https://deeperinsights.com/ai-blog/voice-mode-to-claude-code/
- TechCrunch, Claude Code rolls out a voice mode capability: https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/
- TechBuzz, Anthropic's Claude Code adds voice mode to challenge Copilot: https://www.techbuzz.ai/articles/anthropic-s-claude-code-adds-voice-mode-to-challenge-copilot
- YouTube, Voice + code workflow demo: https://www.youtube.com/watch?v=XvmEVMdFqOA

### 发布说明与 2.1.91+ 社区报道

- GitHub issue, disableSkillShellExecution docs gap: https://github.com/anthropics/claude-code/issues/42870
- GitHub issue, MCP docs missing anthropic/maxResultSizeChars: https://github.com/anthropics/claude-code/issues/42869
- GitHub issue, Exa MCP server result size discussion: https://github.com/exa-labs/exa-mcp-server/issues/133
- X, ClaudeCodeLog, Claude Code 2.1.91 released: https://x.com/ClaudeCodeLog/status/2039856633119969769
- X, Julian Goldie, Claude Code 2.1.91 update thread: https://x.com/JulianGoldieSEO/status/2040640574441553942
- Reddit, Claude Code 2.1.91 Is INSANE!: https://www.reddit.com/r/AISEOInsider/comments/1sbkswv/claude_code_2191_is_insane/

### 提示词工程、CLAUDE.md、Harness 与精通

- Arize, CLAUDE.md best practices learned from prompt learning: https://arize.com/blog/claude-md-best-practices-learned-from-optimizing-claude-code-with-prompt-learning/
- Walturn, Mastering prompt engineering for Claude: https://www.walturn.com/insights/mastering-prompt-engineering-for-claude
- MintMCP, Claude Code security: https://www.mintmcp.com/blog/claude-code-security
- Augment Code, Google Antigravity vs Claude Code: https://www.augmentcode.com/tools/google-antigravity-vs-claude-code
- GitHub, Awesome Claude Code subagents: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/prompt-engineer.md
- MCP Market, Advanced Prompt Engineer: https://mcpmarket.com/tools/skills/advanced-prompt-engineer
- GitHub, Claude Code playbook security best practices: https://github.com/RiyaParikh0112/claude-code-playbook/blob/main/docs/fundamentals/security-best-practices.md
- Julian Goldie, Claude Skills: https://juliangoldie.com/claude-skills/
