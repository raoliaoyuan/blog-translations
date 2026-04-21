> 作者：Rohan Mistry
> 发布日期：2026-03-16
> 原文链接：https://medium.com/@rohanmistry231/claude-code-has-50-commands-most-developers-use-only-5-1e15ef92daee

# Claude Code 有 50 多个命令，大多数开发者只用 5 个

斜线命令（slash commands）、CLI 参数（CLI flags）、键盘快捷键（keyboard shortcuts）及隐藏功能完整指南，让开发效率提升 10 倍。

---

Claude Code 有 50 多个命令。

大多数开发者只用其中 3 到 5 个。

其余命令静静躺在 `/help` 里，等待有人发现——如果你知道它们的存在，效率将提升 10 倍。

根据 2026 年 3 月的数据，掌握 15 个以上 Claude Code 命令的开发者，功能交付速度比那些把它当作"终端里的 ChatGPT"使用的开发者快 3 到 4 倍。

这是一份没人写过的完整参考指南。

涵盖每一条斜线命令、每一个 CLI 参数、每一个键盘快捷键，以及开发团队"顺带一提"却从未正式公告的隐藏功能。

读完之后，你将掌握大多数 Claude Code 用户甚至不知道存在的命令。

---

## 理解三种命令类型

在深入每一条命令之前，先了解 Claude Code 命令的工作方式。

### 类型一：CLI 命令（终端启动）

在终端启动 Claude Code 时使用：

```bash
claude                    # 在当前目录启动
claude -c                 # 继续最近一次会话
claude --print "question" # 单次查询后退出
```

### 类型二：斜线命令（交互会话）

在 Claude Code 会话中输入 `/` 触发：

```
/init      # 初始化 CLAUDE.md
/compact   # 压缩上下文
/model     # 切换模型
```

输入 `/` 即可查看所有可用命令，并支持即时过滤。

### 类型三：键盘快捷键（效率倍增器）

在交互会话中使用：

```
Ctrl+C     # 取消当前生成
Ctrl+R     # 搜索命令历史
Shift+Tab  # 切换模式（普通 → 自动接受 → 计划）
```

---

## 第一部分：每日核心命令（Core 10）

这些是你每天都会用到的命令，优先掌握。

### 1. /init — 项目初始化

**作用：**
在项目根目录创建 CLAUDE.md——一个 Claude 每次会话都会读取的持久化记忆文件（persistent memory file）。

**使用方式：**

```
/init
```

Claude 会自动生成一份 CLAUDE.md 初稿，包含：

- 项目描述
- 技术栈
- 代码风格偏好
- 常见模式

**为什么重要：**

根据开发者工作流分析，每个项目都从 `/init` 开始，可以消除 80% 的重复上下文说明。

不必每次会话都解释"用 async/await，不用 promise"，写进 CLAUDE.md 就永久生效。

**进阶建议：**
`/init` 之后立即补充你的专项规则：

```markdown
# CLAUDE.md

## 认证
- 使用 JWT token，不用 session
- 存储在 httpOnly cookie 中

## 测试
- 为所有 API 端点编写测试
- 使用 Jest，不用 Mocha

## 错误处理
- 返回结构化错误：{ error: string, code: number }
```

---

### 2. /compact — 上下文压缩

**作用：**
当上下文窗口（context window）即将填满时，压缩对话历史，以摘要形式释放空间。

**使用方式：**

```
# 基础压缩
/compact

# 定向压缩（保留特定上下文）
/compact retain the error handling patterns and auth module changes
```

**适用场景：**

- 会话已持续 30 分钟以上
- 出现"上下文过大"警告
- Claude 开始遗忘早期决策

**技术细节：**

根据 2026 年 2 月的发版说明，`/compact` 现已即时完成（此前需要 3 到 5 秒）。

压缩时保留：
- CLAUDE.md 内容
- 任务列表条目
- 关键决策和模式

丢弃：
- 冗长的来回对话
- 已被替代的代码迭代

**常见错误：**
不要等到上下文完全填满再压缩。在使用量达到 70% 到 80% 时主动执行。

通过 `/context` 查看当前用量。

---

### 3. /clear — 完全清空

**作用：**
彻底清空对话历史，重新开始。

**使用方式：**

```
/clear
```

**适用场景：**

- 切换到完全不同的任务
- 完成一个功能后
- 当前上下文与下一项工作无关

**`/compact` 与 `/clear` 对比：**

| 命令 | 效果 | 适用场景 |
|------|------|----------|
| `/compact` | 压缩并保留上下文 | 继续当前任务，上下文已较重 |
| `/clear` | 完全清空，重新开始 | 切换到不同任务 |

**注意：**
`/clear` 同时会清空该目录的命令历史。如果希望保留对历史提示词的访问，请使用 `/compact`。

---

### 4. /model — 切换模型

**作用：**
在会话中途切换 Claude Sonnet、Opus 和 Haiku。

**使用方式：**

```
/model                 # 交互式选择器
/model sonnet          # 切换到 Sonnet 4.6
/model opus            # 切换到 Opus 4.6
/model haiku           # 切换到 Haiku 4.5
```

**各模型适用场景：**

**Sonnet 4.6**（Pro/Max5 计划默认模型）：
- 日常编码
- 重构
- bug 修复
- 大多数常规任务的可靠选择

**Opus 4.6**（最强模型，配合 Max20 计划使用）：
- 复杂的多步骤规划
- 架构决策
- 关键生产代码
- 质量优先于成本时

**Haiku 4.5**（最快、最便宜）：
- 简单编辑
- 样板代码生成
- 快速问答
- 速度优先于精度时

**推荐工作流：**
从 Sonnet 开始，遇到瓶颈时切换到 Opus，琐碎任务用 Haiku。

---

### 5. /cost — Token 用量

**作用：**
显示当前会话的 token 消耗和费用。

**使用方式：**

```
/cost
```

**输出示例：**

```
Session cost: $2.47
Input tokens: 48,392
Output tokens: 12,847
Model: claude-sonnet-4-20250514
```

**为什么重要：**

对于活跃开发来说，根据模型和会话时长，单次会话可能花费 5 到 50 美元。

**成本优化建议：**

- 简单任务用 Haiku
- 运行 `/compact` 减少上下文成本
- 尽量从 Opus 切回 Sonnet
- 每次主要交互后用 `/cost` 确认

---

### 6. /context — 上下文窗口用量

**作用：**
实时显示上下文窗口的使用百分比。

**使用方式：**

```
/context
```

**输出示例：**

```
Context usage: 67% (134,400 / 200,000 tokens)
```

**何时压缩：**

- 70% 到 80%：主动运行 `/compact`
- 90% 以上：Claude 可能开始遗忘早期上下文

**进阶建议：**
上下文过多会导致大语言模型（LLM）性能下降。用 `/context` 随时掌握用量，在触及上限之前压缩。

---

### 7. /diff — 查看近期改动

**作用：**
显示本次会话中 Claude 所做改动的 git diff。

**使用方式：**

```
/diff              # 显示所有改动
/diff src/auth.ts  # 显示指定文件的改动
```

**适用场景：**

- 提交代码之前
- 审查 Claude 实际修改了什么
- 捕捉意外改动

**推荐工作流：**
每个功能完成后：`/diff` → 审查 → 提交。这是你的提交前代码审查环节。

---

### 8. /help — 命令列表

**作用：**
显示所有可用的斜线命令。

**使用方式：**

```
/help
```

**为什么重要：**

Claude Code 持续更新，命令也会随之变化。`/help` 始终是你当前版本的权威命令参考。

**查看当前版本：**

```bash
claude --version
```

---

### 9. /memory — 编辑 CLAUDE.md

**作用：**
不离开会话，直接打开 CLAUDE.md 进行编辑。

**使用方式：**

```
/memory
```

**适用场景：**

- 会话中途新增代码规范
- 更新项目上下文
- 记录 Claude 应遵循的新模式

**快速记忆语法：**

```
# 为所有数据库查询使用 async/await
```

`#` 前缀会将快速备注追加到 CLAUDE.md 中。

---

### 10. /resume — 继续历史会话

**作用：**
加载并继续之前的对话。

**使用方式：**

```bash
# 继续最近一次会话
claude --resume

# 按名称继续指定会话
claude --resume auth-refactor

# 从列表中选择
/resume
```

**隐藏技巧：**
会话数据存储在 `~/.claude/projects/`。你可以直接问 Claude："找出我 2024 年 12 月的会话"，它会帮你搜索。

---

## 第二部分：进阶效率命令

这些命令是高级用户与普通用户的分水岭。

### 11. /btw — 不打断上下文的提问

**作用：**
在不中断 Claude 当前任务、不污染上下文的情况下，临时提一个问题。

**使用方式：**

```
# Claude 正在重构一个大型模块
# 你突然需要确认一件事

/btw What is the difference between useEffect and useLayoutEffect?
# Claude 回答后，继续之前的重构
```

**为什么颠覆工作流：**

有了 `/btw` 之前，你必须：
1. 取消当前任务
2. 提问
3. 重新发起原始任务

现在只需 `/btw`，继续往前走。

发布日期：2026 年 3 月 11 日（相关推文获得 220 万次浏览）

---

### 12. /fast — 极速模式

**作用：**
开启 Fast Mode，使用经过速度优化的 API 设置。

**使用方式：**

```
/fast         # 开关切换
```

**技术细节：**

Fast Mode 并非切换到不同模型——它仍然运行同一个 Opus 4.6，只是采用了优化后的 API 设置。

**适用场景：**
- 快速交互迭代
- 实时调试
- 快速实验

**不适用场景：**
- 成本敏感的场景
- 生产代码

**注意：**
在会话中途开启 Fast Mode 后，之前的全部上下文将按 Fast Mode 费率重新计费。

---

### 13. /plan — 计划模式（只读）

**作用：**
代码改动以计划形式提出，需要审批后才会执行。

**使用方式：**

```
# 切换计划模式
Shift+Tab   # 循环切换模式

# 或显式启用
/plan
```

**三种模式：**

- **普通（Normal）**：每次工具调用前询问确认
- **自动接受（Auto-Accept）**：所有工具调用无需确认直接执行
- **计划模式（Plan Mode）**：提出改动方案，等待审批后再执行

**实用工作流：**

- 自动接受：编写测试、生成样板代码
- 计划模式：涉及生产关键文件（配置、数据库迁移、package.json）

"展示计划 → 审批 → 执行"的流程可以有效防止意外操作。

---

### 14. /fork — 试验分支

**作用：**
创建一个临时会话分支，用于探索想法，不影响主上下文。

**使用方式：**

```
/fork

# 尝试实验性重构
# 效果不理想？
# 关闭分支，返回主会话
```

**适用场景：**

- 测试风险较高的重构
- 探索多种方案
- 快速实验

---

### 15. /rewind — 撤销对话或代码

**作用：**
回退对话历史和/或代码改动。

2026 年 2 月增强：现在可以分别撤销对话和代码。

**使用方式：**

```
Esc Esc   # 打开撤销菜单

# 选项：
# - 仅撤销对话（保留代码）
# - 仅撤销代码（保留对话）
# - 同时撤销
```

**工作流示例：**

```
# 尝试实验性重构
# → 效果不理想
# → Esc Esc
# → 选择"仅撤销代码"
# → 代码回退，对话历史保留
```

当你不小心批准了错误改动时，这个功能能救你于水火。

---

### 16. /todos — 持久化任务列表

**作用：**
维护一个即使关闭会话也不会消失的任务列表。

新增版本：v2.1.16（2026 年 1 月）

**使用方式：**

```
# 切换任务列表显示
Ctrl+T

# 用自然语言创建任务
"Add authentication feature. Break it down into tasks by dependency"
```

**为什么重要：**

关闭会话后任务不会消失，在上下文压缩时任务列表同样保留。

**团队协作工作流：**

设置环境变量 `CLAUDE_CODE_TASK_LIST_ID`，可在多个 Claude Code 会话之间共享任务列表。

适用于多个并行会话分别处理同一项目不同部分的场景。

---

### 17. /review → /simplify（2026 年 3 月新增）

**作用：**
使用三个并行 agent 进行代码审查。

**使用方式：**

```
/simplify   # 替代已弃用的 /review
```

**检查内容：**

- 代码质量
- 安全漏洞
- 最佳实践违规
- 性能问题
- 测试覆盖率

**推荐工作流：**

1. 编写功能
2. `/simplify`
3. 审查反馈
4. 修复问题
5. 提交

---

### 18. /output-style — 调整 Claude 的回复风格

**作用：**
自定义 Claude 的回复方式。

**使用方式：**

```
/output-style

# 选项：
# - Concise（简洁）
# - Educational（教学）
# - Code Reviewer（代码审查）
# - Rapid Prototyping（快速原型）
```

**未公开功能：**

`@agent-output-mode-setup` 会在 `~/.claude/output-modes/` 下生成四种自定义模式：

- Concise（简洁）
- Educational（教学）
- Code Reviewer（代码审查）
- Rapid Prototyping（快速原型）

---

### 19. /permissions — 管理自动审批

**作用：**
配置哪些操作可以由 Claude 直接执行，无需询问。

**使用方式：**

```
/permissions

# 配置示例：
# 自动批准：npm install、git status、文件读取
# 需要审批：git push、文件删除、npm publish
```

**最佳实践：**

对常规操作开启自动批准，把注意力留给关键决策。

---

### 20. /agents — 子代理管理

**作用：**
创建和管理专用于特定任务的子代理（sub-agent）。

**使用方式：**

```
/agents

# 创建子代理
@agent-create test-writer "Writes comprehensive Jest tests"
```

**适用场景：**

- 委托特定任务
- 保持主会话聚焦
- 防止上下文被无关工作污染

**进阶建议：**
不要犹豫，大胆委托。子代理能防止主上下文被旁支工作塞满。

---

## 第三部分：CLI 参数与启动选项

这些参数在从终端启动 Claude Code 时控制其行为。

### 21. claude --print — 单次查询

**作用：**
执行一次查询后退出，不进入交互会话。

**使用方式：**

```bash
# 提问、获取答案、退出
claude --print "Explain the difference between async/await and promises"

# 适合用于脚本
result=$(claude --print "Generate a random UUID")
echo $result
```

**使用场景：**

- Shell 脚本
- CI/CD 流水线
- 不想启动完整会话的快速问答

---

### 22. claude -c 或 --continue — 继续最近会话

**作用：**
在当前目录中继续最近一次会话。

**使用方式：**

```bash
cd ~/projects/my-app
claude -c   # 继续此目录的最近会话
```

**从不同目录继续：**

```bash
claude --resume session-id
```

**从 Pull Request 继续：**

```bash
claude --from-pr 123
```

直接继续与 PR #123 关联的会话。

---

### 23. --append-system-prompt 与 --system-prompt

**作用：**
自定义系统提示词（system prompt）。

**使用方式：**

```bash
# 追加到默认指令（安全）
claude --append-system-prompt "Always use TypeScript strict mode"

# 替换全部默认指令（危险）
claude --system-prompt "You are a Python expert"
```

**各自适用场景：**

`--append-system-prompt`（推荐）：
- 在保留 Claude Code 默认能力的同时添加自定义规则
- 适合大多数场景

`--system-prompt`（高级用法）：
- 完全替换默认指令
- 仅在需要完全掌控时使用
- 会移除 Claude Code 的所有默认行为

---

### 24. --dangerously-skip-permissions

**作用：**
对所有操作自动审批，不再询问。

**使用方式：**

```bash
# 警告：仅在可信容器中使用
claude --dangerously-skip-permissions
```

**使用条件：**

**仅限**在可信容器环境（Docker、CI/CD）中使用。

**绝对不要**在本地机器上对生产数据使用。

使用此参数前，请参阅自动审批安全使用指南。

---

### 25. --agents — 启动时定义子代理

**作用：**
在启动时通过 JSON 定义子代理。

**使用方式：**

```bash
claude --agents '{
  "test-writer": {
    "role": "Write comprehensive Jest tests",
    "model": "claude-sonnet-4"
  }
}'
```

**使用场景：**

为团队工作流和 CI/CD 预配置 agent。

---

### 26. --output-format json — 结构化输出

**作用：**
以 JSON 格式返回结果，而非纯文本。

**使用方式：**

```bash
claude --print "List all functions in app.js" --output-format json
```

**使用场景：**

- Shell 脚本
- CI/CD 集成
- 程序化解析 Claude 的输出

---

## 第四部分：键盘快捷键（效率倍增器）

这些快捷键能大幅提升工作流速度。

### 核心快捷键

```
Ctrl+C         取消当前生成
Ctrl+R         搜索命令历史
Tab            切换思考过程显示
Shift+Tab      循环切换模式（普通 → 自动接受 → 计划）
Esc Esc        打开撤销菜单
```

### 导航与编辑

```
Ctrl+T         切换任务列表
Alt+M          切换模式（同 Shift+Tab）
Alt+P          上一条消息
Alt+N          下一条消息
Alt+B          在对话中后退
Alt+F          在对话中前进
```

**macOS 用户注意：**
使用 Alt 的快捷键需要在终端中将 Option 键配置为 Meta 键。

iTerm2 配置路径：Settings → Profiles → Keys → 将左/右 Option 设置为"Esc+"

### 高级快捷键

```
Shift+Enter    多行输入（不发送）
Ctrl+L         清屏（仅视觉效果，不清除对话）
Ctrl+D         退出 Claude Code
```

**WSL 用户注意：**
在 Windows Terminal 中，`Shift+Enter` 可能无法直接使用。运行 `/terminal-setup` 安装键位绑定。

### 文件与命令快捷键

```
@ + 路径       文件自动补全
! + 命令       直接执行 bash 命令
# + 文本       快速添加记忆
```

**示例：**

```bash
# 文件自动补全
@src/auth.ts   # 自动补全为完整路径

# 直接执行 bash
! git status   # 立即执行，输出纳入上下文

# 快速添加记忆
# Use JWT tokens for authentication
```

---

## 第五部分：隐藏及未公开功能

以下功能不在官方文档中，但在生产环境中可用。

### 27. /vim — Vim 键位绑定

**作用：**
为提示词输入启用 Vim 键位绑定。

**使用方式：**

```
/vim
```

**支持的功能：**

- 模式切换（普通模式、插入模式）
- 导航（`h`/`j`/`k`/`l`、`w`/`b`/`e`、`0`/`$`）
- 字符跳转（`f`/`F`/`t`/`T`）
- 编辑操作符（`d`、`c`、`y`、`p`）
- 文本对象（`iw`、`aw`、`i"`、`a(`）

这不是简化版的 Vim 模拟，而是完整实现。

---

### 28. /remote-control — 手机远程控制

**作用：**
通过 claude.ai 网页界面远程控制本地 Claude Code。

**使用方式：**

```
/remote-control
```

**使用场景：**

离开工位时通过手机远程指挥本地工作。

例如：上班途中想起需要修复一个 bug，打开手机上的 claude.ai，连接本地会话，指挥 Claude 实现修复。

---

### 29. /export — 将会话导出为文档

**作用：**
将对话导出为可搜索的文档。

**使用方式：**

```
/export
```

**适用场景：**

解决棘手问题后导出，导出内容可作为：

- 可搜索的文档
- 学习资源
- 团队知识库

---

### 30. 会话克隆（Conversation Cloning）

**作用：**
克隆一个会话，从同一起点探索不同思路。

**使用方式：**

没有专门的命令，但可以通过以下方式实现：

```
# 保存会话状态
/export

# 开启新会话
# 导入之前的状态上下文
```

**使用场景：**

从同一个起点尝试多种架构方案。

---

### 31. /usage-report — 月度用量报告

**作用：**
读取过去一个月的用量数据，生成 HTML 报告。

**使用方式：**

```
/usage-report
```

**报告内容：**

- 会话总数
- token 消耗量
- 费用明细
- 最常用命令
- 每个项目的时间投入

---

### 32. 底栏显示 PR 状态

**作用：**
在有未关闭 PR 的分支上工作时，Claude Code 会在底栏显示 PR 状态。

**视觉标识：**

PR 链接下方的彩色下划线表示审查状态：

- 绿色：已批准
- 黄色：需要修改
- 红色：被阻止
- 灰色：待审查

每 60 秒自动更新。

---

## 第六部分：配置文件与自定义

了解 Claude Code 存储数据的位置以及如何自定义配置。

### 文件目录

```
~/.claude/                    # 主配置目录
~/.claude/projects/           # 会话历史
~/.claude/commands/           # 自定义斜线命令（旧版标准）
~/.claude/skills/             # Agent 技能（2026 年新标准）
~/.claude/output-modes/       # 自定义回复风格
~/.claude/keybindings.json    # 键盘快捷键
```

### CLAUDE.md — 项目记忆

**位置：** 项目根目录

**存储内容：**

- 项目描述
- 技术栈
- 代码风格规则
- 常见模式
- 测试要求

**示例：**

```markdown
# Project: E-Commerce API

## Tech Stack
- Node.js + Express
- PostgreSQL via Prisma
- JWT authentication

## Rules
- Use async/await, never callbacks
- Write tests for all endpoints
- Return structured errors: { error, code }

## Patterns
- All database queries in /services
- Route handlers in /routes
- Middleware in /middleware
```

### 自定义技能（与命令统一）

**位置：** `~/.claude/skills/`

**2026 年的变化：**

传统的自定义命令（`.claude/commands/`）与技能（`.claude/skills/`）已合并。

现有的 `.claude/commands/` 文件仍然有效，但新标准是 Skills。

Skills 新增了：

- 基于元数据头（frontmatter）的自动触发控制
- 文件管理能力
- 符合 Agent Skills Open Standard
- 跨工具兼容性

**技能示例：**

```markdown
---
name: deploy-staging
description: Deploy current branch to staging
auto_invoke: false
---

# Deploy to Staging
1. Run tests
2. Build production bundle
3. Push to staging server
4. Run smoke tests
```

### 自定义键位绑定

**位置：** `~/.claude/keybindings.json`

**编辑方式：**

```
/keybindings
```

**示例：**

```json
{
  "toggle_thinking": "Tab",
  "cancel": "Ctrl+C",
  "search_history": "Ctrl+R",
  "toggle_task_list": "Ctrl+T"
}
```

修改后无需重启 Claude Code，立即生效。

---

## 第七部分：生产工作流与最佳实践

如何在真实开发中运用这些命令。

### 工作流一：功能开发

```bash
# 1. 启动会话
claude

# 2. 设置上下文
/init   # 第一次进入项目时
/memory # 更新当前功能需求

# 3. 为本次功能快速添加记忆
# Use JWT for auth
# Write tests for all endpoints
# Follow RESTful conventions

# 4. 实现功能
"Create authentication middleware for Express that validates JWT tokens"

# 5. 审查改动
/diff

# 6. 运行测试
! npm test

# 7. 确认费用
/cost

# 8. 提交
! git add .
! git commit -m "feat: add JWT auth middleware"
```

### 工作流二：调试

```bash
# 1. 继续现有会话
claude -c

# 2. 描述错误
"Here's the error I'm getting:"
[粘贴报错信息]

# 3. Claude 排查
# 用 /btw 提旁支问题，不打断主流程

# 4. 应用修复
/diff   # 审查改动

# 5. 测试
! npm test

# 6. 修复成功后压缩并继续
/compact
```

### 工作流三：大型重构

```bash
# 1. 以计划模式开始
claude
Shift+Tab  # 开启计划模式

# 2. 描述重构目标
"Refactor auth module to use bcrypt instead of plain passwords"

# 3. 执行前审查计划
# 批准或调整方案

# 4. 监控上下文用量
/context

# 5. 在 70% 时主动压缩
/compact retain auth patterns and migration strategy

# 6. 常规改动切换为自动接受模式
Shift+Tab  # 自动接受模式

# 7. 最终审查
/diff
/simplify  # 代码审查

# 8. 导出文档
/export
```

### 工作流四：多 Agent 委托

```bash
# 1. 主会话：负责架构
"Design the database schema for user authentication"

# 2. 委托给子代理
/agents
@agent-create test-writer "Write comprehensive tests"

# 3. 主会话继续推进
"Now implement the auth middleware"

# 4. 子代理并行工作
@test-writer "Generate tests for auth middleware"

# 5. 整合结果
# 主会话保持简洁、聚焦
```

---

## 关键要点

**1. 先掌握 Core 10**

`/init`、`/compact`、`/clear`、`/model`、`/cost`、`/context`、`/diff`、`/help`、`/memory`、`/resume`

仅凭这十个命令，效率就能提升 3 到 4 倍。

**2. `/btw` 会改变你的工作方式**

在不干扰上下文的情况下提问，可以大量使用。

**3. 主动压缩，而非被动应对**

在上下文使用量达到 70% 到 80% 时运行 `/compact`，不要等到 95%。

**4. CLAUDE.md 是效率倍增器**

一次设置，每次会话节省 10 到 15 分钟。

**5. 切换模式防止意外操作**

- 自动接受：样板代码和测试
- 计划模式：生产关键文件
- 普通模式：其他所有情况

**6. 导出突破性会话**

`/export` 将解决方案变成可搜索的文档。

**7. 使用 Opus 时关注费用**

每次重要交互后运行 `/cost`，Opus 会话可能花费 50 美元。

**8. 键盘快捷键让速度倍增**

`Shift+Tab`、`Ctrl+T`、`Esc Esc`、`Ctrl+R`——务必熟练掌握。

**9. 子代理让上下文保持整洁**

委托专项任务，主会话保持聚焦。

**10. 隐藏功能值得探索**

`/vim`、`/remote-control`、`/usage-report`——定期翻阅 `/help`，总有新发现。

---

Claude Code 有 50 多个命令。

你刚刚全部学完了。

大多数开发者仍将只用 3 到 5 个。

你现在拥有完整的武器库。

把 Claude Code 当作"终端里的 ChatGPT"的开发者，与把它当作可编程开发搭档的开发者，差距就在于对命令的掌握程度。

从 Core 10 开始，每周新增一个命令，导出你的突破性会话。

---

*来源：Claude Code 官方文档 v2.1.72、Anthropic 发版说明 2026 年 3 月、SmartScope 完整参考、DEV Community 命令指南、32blog Cheat Sheet、awesome-claude-code 仓库、多位开发者生产工作流——2026 年 3 月*
