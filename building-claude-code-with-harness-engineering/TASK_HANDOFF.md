# 任务交接文件

## 任务状态

**已完成：**
- 从原始 URL 抓取全文并解码为干净文本
- 识别全部 31 张图片 URL 并按 DOM 顺序记录位置
- 下载全部 31 张图片到当前目录（`img-01-*.png` … `img-31-*.png`）
- 创建输出目录：`/Users/roger/Work/Blog/building-claude-code-with-harness-engineering/`

**待完成：**
- 将原文翻译为中文并写入 `用harness工程构建Claude-Code.md`

---

## 原始材料

| 文件 | 说明 |
|------|------|
| `/Users/roger/Work/Blog/article-source-clean.txt` | 原文全文（纯文本，3728 行，已解码） |
| `/Users/roger/Work/Blog/article-images.txt` | 31 张图片的 URL、宽度、DOM 位置（JSON 格式） |
| `img-01-claude-code-architecture.png` … `img-31-worktree-lifecycle.png` | 下载好的图片（当前目录） |

**读取原文时请分段读取**，每次不超过 300 行，避免超出上下文。

---

## 文章基本信息

- **标题**：Building Claude Code with Harness Engineering
- **副标题**：Multi-agents, MCP, skills system, context pipelines and more
- **作者**：Fareed Khan
- **发布日期**：Apr 6, 2026
- **原文 URL**：https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0
- **GitHub 仓库**：https://github.com/FareedKhan-dev/claude-code-from-scratch

---

## 输出文件

翻译结果保存至（当前目录）：

```
/Users/roger/Work/Blog/building-claude-code-with-harness-engineering/用harness工程构建Claude-Code.md
```

---

## 文件前置元信息（必须放在译文最开头）

```markdown
> 作者：Fareed Khan
> 发布日期：2026 年 4 月 6 日
> 原文链接：https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0
```

---

## 文章结构与图片插入位置

图片按顺序插入，位于对应标题段落之后。

| 图片文件 | 插入位置（对应原文标题/段落） |
|----------|-------------------------------|
| `img-01-claude-code-architecture.png` | 文章开头架构介绍段落之后（"Claude Code is built from five core components…" 之前） |
| `img-02-harness-architecture.png` | "How Claude Code Uses Harness Engineering?" 章节，第一段正文之后 |
| `img-03-core-agent-loop.png` | "Phase 1: The Core Agent Loop" 章节，开头段落之后 |
| `img-04-minimal-while-loop.png` | "Minimal While Loop:" 小节，开头段落之后 |
| `img-05-tool-dispatch-pattern.png` | "Tool Dispatch Map Pattern" 小节，"What makes this system elegant…" 之后 |
| `img-06-todo-write.png` | "TodoWrite Planning Before Execution" 小节，"The plan comes before the action…" 之后 |
| `img-07-subagent-context.png` | "Subagent Context Isolation" 小节，"This is subagent context isolation…" 之前 |
| `img-08-knowledge-context-management.png` | "Phase 2: Knowledge & Context Management" 章节，开头段落之后 |
| `img-09-on-demand-skill.png` | "On-Demand Skill Loading" 小节，"Claude Code solves this with progressive disclosure…" 之后 |
| `img-10-context-compression.png` | "Three-Layer Context Compression" 小节，"It does not discard history…" 之后 |
| `img-11-file-based-task-graph.png` | "File-Based Task Dependency Graph" 小节，开头段落之后 |
| `img-12-multi-agent-teams.png` | "Phase 3: Async Execution & Multi-Agent Teams" 章节，开头段落之后 |
| `img-13-background-task-execution.png` | "Background Task Execution with Notifications" 小节，"Without this mechanism…" 之前 |
| `img-14-persistent-teammates.png` | "Persistent Teammates with JSONL Mailboxes" 小节，开头段落之后 |
| `img-15-fsm-protocol.png` | "FSM Team Communication Protocol" 小节，"Claude Code solves inter-agent coordination…" 之前 |
| `img-16-autonomous-self-assignment.png` | "Autonomous Task Self-Assignment" 小节，开头段落之后 |
| `img-17-worktree-isolation.png` | "Git Worktree Task Isolation" 小节，"Git worktrees give each agent…" 之前 |
| `img-18-production-hardening.png` | "Phase 4: Production Hardening" 章节，开头段落之后 |
| `img-19-real-time-streaming.png` | "Real-Time Token Streaming" 小节，"The difference between a streaming agent…" 之后 |
| `img-20-extended-tools.png` | "Extended Tool Arsenal and File Snapshots" 小节，开头段落之后（"not because bash cannot do…" 之后） |
| `img-21-permission-governance.png` | "YAML Rule-Based Permission Governance" 小节，开头段落之后 |
| `img-22-event-bus.png` | "Event Bus and Lifecycle Hooks" 小节，"The event bus makes observability…" 之前 |
| `img-23-session-persistence.png` | "Session Persistence, Resume, and Fork" 小节，开头段落之后 |
| `img-24-async-runtime.png` | "Phase 5: High-Performance Async Runtime" 章节，开头段落之后 |
| `img-25-parallel-tool-execution.png` | "Parallel Tool Execution with asyncio.gather" 小节，"The implementation requires refactoring…" 之前 |
| `img-26-real-time-interrupt.png` | "Real-Time Interrupt Injection" 小节，"Without this mechanism…" 之前 |
| `img-27-kv-cache.png` | "Prompt Caching and KV Cache Optimisation" 小节，"The system prompt and tool definitions…" 之前 |
| `img-28-mcp-runtime.png` | "Official MCP Runtime Integration" 小节，"The MCP runtime reads server configurations…" 之前 |
| `img-29-enterprise-upgrades.png` | "Phase 6: Enterprise Upgrades" 章节，开头段落之后 |
| `img-30-redis-pubsub.png` | "Redis Pub/Sub Production Mailboxes" 小节，"Claude Code's internal agent coordination…" 之前 |
| `img-31-worktree-lifecycle.png` | "Advanced Worktree Lifecycle Management" 小节，"Claude Code avoids most of these issues…" 之前 |

---

## 翻译规范摘要

### 首次出现时必须标注的术语

| 中文 | 英文原文 |
|------|---------|
| harness 工程 | harness engineering |
| 感知-行动-观察循环 | perception-action-observation cycle |
| 分发映射 | dispatch map |
| 上下文窗口 | context window |
| 子 agent | subagent |
| 技能 | skill |
| 有限状态机 | finite state machine (FSM) |
| 工作树 | worktree |
| 生命周期钩子 | lifecycle hook |
| 事件总线 | event bus |
| 提示词缓存 | prompt caching |
| KV 缓存 | KV cache |
| 分发注册表 | dispatch registry |
| 快照 | snapshot |
| 渐进式披露 | progressive disclosure |

标注格式：`中文翻译（English Original）`，例如：`harness 工程（harness engineering）`

### 绝对不翻译的内容

- 所有代码标识符（函数名、变量名、类名）：`run_bash()`、`agent_loop()`、`EXTENDED_DISPATCH` 等
- 命令和路径：`python -m pytest`、`.agent_todo.json` 等
- 产品/项目名：Claude Code, Anthropic, Redis, asyncio, GitHub
- 行业缩写：API, CLI, MCP, FSM, YAML, JSONL, JSON, I/O
- 约定俗成词：`token`、`bug`、`stream`、`harness`

### 灵活翻译的术语（直接使用，无需标注）

- model → 模型
- streaming → 流式传输 / 流式
- cache → 缓存
- context → 上下文

### 文章风格

- 使用简短的主动句式
- 英文长句拆分为自然的中文短句
- 不加感叹号，不使用网络用语
- 不添加原文没有的解释性文字

### 超链接处理

原文所有超链接必须保留：

```markdown
[中文锚文字](原始URL)
```

例如原文的 GitHub 仓库链接：
```markdown
[GitHub - FareedKhan-dev/claude-code-from-scratch：Claude Code 架构的 23 个组件](https://github.com/FareedKhan-dev/claude-code-from-scratch)
```

---

## 建议的分段翻译策略

由于原文长达 3728 行，建议分三段处理：

**第一段**（原文第 1-900 行）：
- 前言 / 引言
- What is Harness Engineering?
- How Claude Code Uses Harness Engineering?
- Phase 1 全部（Minimal While Loop / Tool Dispatch / TodoWrite / Subagent）

**第二段**（原文第 900-1820 行）：
- Phase 2 全部（Skill Loading / Context Compression / Task Graph）
- Phase 3 全部（Background Tasks / JSONL Mailboxes / FSM / Self-Assignment / Worktree）

**第三段**（原文第 1820-3728 行）：
- Phase 4 全部（Streaming / Tool Arsenal / Permissions / Event Bus / Session）
- Phase 5 全部（asyncio / Interrupt / Prompt Caching / MCP）
- Phase 6 全部（Redis / Advanced Worktree / All Combined）
- How to Improve It Further

**写入方式**：
- 第一段：用 `Write` 工具创建文件
- 第二、三段：用 `bash` 的 `cat >> 文件` 追加，避免覆盖前段内容

---

## 已知注意事项

1. 原文第 680 行提到 "compressor wU2"、第 1118 行提到 "h2A async queue"，这些是作者自造的内部标识符，直接保留英文。
2. 原文中 `s01 >>`, `s02 >>` 等是 REPL 提示符示例，代码块中保留原样。
3. 原文多处出现 "Press enter or click to view image in full size"，这是 Medium 的图片说明文字，翻译时替换为对应的 `![图片说明](img-XX-xxx.png)` 即可，不需要保留该文字。
4. 文章开头的 "Top highlight"、"Member-only story"、"Read this story for free: link" 是 Medium 界面元素，翻译时跳过。
5. 原文末尾 "You can follow me on Medium if you find this article useful" 可以保留或跳过。
