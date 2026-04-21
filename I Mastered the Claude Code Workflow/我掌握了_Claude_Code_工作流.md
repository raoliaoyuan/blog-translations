> 作者：Ashley Ha
> 发布日期：2025-10-16
> 原文：Medium，Humaine Interface

# 我掌握了 Claude Code 工作流

*免责声明：本文由人类撰写。作者 Ashley 写作此文的目的是分享真正有用的知识和可操作的内容。如果你是来找 AI 生成内容的，这里没有。*

## 内容摘要

永远不要超过 60% 的上下文。将工作分为四个阶段：调研 → 规划 → 实现 → 验证，每个阶段之间清空上下文。所有内容保存到符号链接（symlink）的 `thoughts/` 目录（使用 `npx humanlayer thoughts init`）。

关于符号链接的 `thoughts/` 目录，有一点非常重要：该目录可以跨代码库全局共享，团队和组织中的每个人都能访问 Claude 正在编辑和参考的文档，这是极其强大的能力。

强烈建议下载 humanlayer 的 `.claude/commands` 和 `.claude/agents`，并花时间根据自己的代码库进行调整。[点击这里下载](https://github.com/humanlayer/humanlayer)

---

## 上下文的理想状态

六个月前，我与 AI 编程助手的对话大概是这样的：开始做一个功能，加载一堆文件，提问，得到回答，做修改，遇到报错，再加更多文件，再提问。很快就到了 95% 的上下文容量，代码只实现了一半，文件夹里堆满了 `final_implementation_final_feature.md` 💀

将注意力转向上下文工程（context engineering）改变了这一切。特别感谢 humanlayer 团队，尤其是 Dex，他对这个问题的阐释非常透彻，给了我很大的启发。现在我能更有信心地交付数千行代码，依托的是一套让上下文保持干净、计划保持可靠、实现结果更可预测的结构化工作流。

---

## 上下文工程就是一切

问题不在于有多少上下文，而在于在正确的时机拥有正确的上下文。

分配到上下文窗口（context window）里的内容越多，输出质量越差、行为越出人意料——无论使用哪个大模型，这一规律都成立。

**我的个人原则：永远不让上下文超过 60%。** 我在每次会话中始终通过 `/context` 检查。

我通常将工作流分为四个核心阶段，每个阶段之间清空上下文，例如：

1. **调研**：我的 Claude 提示词：`/research_codebase` + 要实现的功能或代码库调研内容 → `/context`，如果调研后超过 60%（通常都会），则 `/clear`，其余三个阶段以此类推。

2. **规划**：我的 Claude 提示词：`/create_plan` + `@thoughts/research/researched_feature.md` → `/context` → 70% → `/clear`

3. **实现**：我的 Claude 提示词：`/implement_plan` + `@thoughts/plans/research_and_planned_feature.md Phase 1 only of this plan` → `/context` → 67% → `/clear`

4. **验证**：我的 Claude 提示词：`/validate_plan` + `@thoughts/plans/research_and_planned_feature.md` + 我已经实现了这个计划文档的第一阶段，请验证 → `/context` → 42% → 继续本次对话（即不清空上下文）

每个阶段有各自的职责，每个阶段的产物（artifact）由下一个阶段消费。

---

## 我的 Claude Code 工作流

### 阶段一：调研（@research_codebase.md）

**目标**：了解现有内容以及需要更改的内容。本阶段**不应编写任何代码**。

开始一个新功能时，我从不直接进入实现，而是先调研，调用我的自定义 Claude 命令（`.claude/commands/research_codebase.md`）：

```
/research_codebase + {要调研或构建的内容，或要实现的功能}
```

命令执行后，我提出调研问题。例如，当我需要了解一个网页自动化框架中的浏览器页面管理机制时：

```
/research_codebase + How does the current browser page management system work?
```

或者：

```
/research_codebase + Where are pages created, tracked, and cleaned up?
```

调研命令会并行启动多个子智能体（sub-agent），同时调查不同方面：

- **codebase-locator agent**：找出所有相关文件
- **codebase-analyzer agent**：分析当前实现的工作方式
- **thoughts-locator agent**：搜索现有文档或过往调研记录
- **thoughts-analyzer agent**：从相关文档中提取洞察

这些 agent 并行运行，返回具体的文件路径和行号。

调研阶段结束后，会在 `thoughts/` 目录下生成一份综合调研文档：

```
thoughts/shared/research/2025-10-09_browser-page-management.md
```

该文档内容详尽，包括：

- 发现摘要
- 带有 `file:line` 行号的代码引用（**非常重要**）
- 架构洞察
- 需要澄清的开放性问题

通过并行启动 agent，我能快速得到全面的答案，而不需要手动阅读几十个文件。由于所有内容都保存到 `thoughts/` 目录，我、我的团队和 Claude 之后都可以引用，而无需把它保留在上下文里。

---

### 阶段二：规划（@create_plan.md）

**目标**：创建详细的、迭代式的实现计划。

调研完成后，清空上下文，重新开始规划：

```
@create_plan.md thoughts/shared/research/2025-10-09_browser-page-management.md
```

这条命令读取调研文档，启动一个交互式规划会话。在 Claude 给出初始回应后，我通常会迭代约五次，仔细阅读整份 `.md` 文件后再最终确定计划。

**这份计划文档是我们的唯一可信来源。**

为什么要迭代这么多次？因为第一稿从来都不完整。规划阶段是交互式的：

1. **第一稿**：Claude 读取调研内容，提出澄清性问题
2. **第二稿**：我提供答案，Claude 细化方案
3. **第三稿**：讨论设计权衡，Claude 更新各阶段
4. **第四稿**：识别边界情况，Claude 补充成功标准
5. **第五稿**：最终审阅，所有内容都可落地执行

每次迭代让计划更具体。最终的计划包含：

- 带有具体变更内容的清晰阶段
- 需要修改的精确文件路径
- 展示新增或变更内容的代码片段
- 自动化验证（测试、lint、类型检查）
- 手动验证（需要人工测试的内容）
- 每个阶段的成功标准

最终计划保存到：

```
thoughts/shared/plans/2025-10-09-browser-page-management.md
```

以下是计划中某个阶段的示例：

```markdown
Phase 1: Add Page Tracking to BrowserContext

Overview
Add a page registry to BrowserContext to track all created pages 
and their lifecycle state.

Changes Required:
1. Update BrowserContext class
File: src/browser/browser_context.py
class BrowserContext:
    def __init__(self, ...):
        self._pages: Dict[str, Page] = {}
        self._active_page: Optional[Page] = None

Success Criteria:
Automated Verification:
- [ ] Unit tests pass: uv run pytest src/browser/tests/
- [ ] No linting errors: make lint
- [ ] Type checking clean: make check

Manual Verification:
- [ ] Can track multiple pages simultaneously
- [ ] Page cleanup works in headed browser mode
- [ ] No memory leaks with repeated page creation
```

关键洞察：在规划上花时间迭代，能节省实现阶段数小时的成本，也能避免劣质代码。有了扎实的计划，我很少会卡住或需要回退。

调研命令已经找到了相关代码行，因此规划命令节省了大量上下文，可以更有效地用于实现阶段。

---

### 阶段三：实现（@implement_plan.md）

**目标**：每次只执行一个阶段，保持信心。

规划完成后，再次清空上下文，开始实现：

```
@implement_plan.md thoughts/shared/plans/2025-10-09-browser-page-management.md
```

**我的原则：每次只实现一个阶段。**

实现命令会：

1. 完整读取计划
2. 读取第一阶段中提到的所有文件
3. 执行指定的变更
4. 运行自动化验证
5. 暂停等待手动测试

最后一点至关重要。所有自动化检查通过后，Claude 会告知我：

```
Phase 1 Complete - Ready for Manual Verification
Automated verification passed:
- ✓ Unit tests pass
- ✓ No linting errors
- ✓ Type checking clean

Please perform manual verification:
- [ ] Can track multiple pages simultaneously
- [ ] Page cleanup works in headed browser mode

Let me know when manual testing is complete.
```

然后我手动测试该功能。如果通过，我告诉 Claude 进入第二阶段（前提是上下文仍低于 60%）。如果未通过，我报告失败内容，在推进之前先修复。

这种方式能避免一个常见陷阱：把所有阶段都实现完，才发现第一阶段有一个关键 bug，导致后续全部崩溃。

**关键洞察：每次一个阶段 = 持续验证 = 更少意外。**

---

### 阶段四：验证（@validate_plan.md）

**目标**：系统性地验证整个实现。

实现完所有阶段（或哪怕只是一个阶段）后，再次清空上下文，进行验证：

```
@validate_plan.md thoughts/shared/plans/2025-10-09-browser-page-management.md
```

验证命令会：

1. 读取计划
2. 检查近期的 git 提交
3. 运行所有自动化验证命令
4. 对照计划规格审查代码变更
5. 生成综合验证报告

报告会展示：

- ✓ 正确实现的内容
- ⚠ 与计划的偏差
- ✗ 需要修复的问题
- 手动测试清单

这最后一步能发现诸如：

- "第二阶段额外增加了验证逻辑（好）"
- "缺少对边界情况 X 的错误处理（需修复）"
- "自动化测试通过，但手动测试暴露出 UX 问题"

**关键洞察：验证是安全网，确保你在交付之前没有遗漏任何内容。**

---

## 秘密武器：`thoughts/` 目录

在整个工作流中，所有内容都保存到我的 `thoughts/` 目录：

```
thoughts/
├── ashley/
│   ├── tickets/
│   │   └── eng_1478.md          # 原始 linear 工单
│   └── notes/
│       └── notes.md              # 个人观察与随手记录
├── shared/
│   ├── research/
│   │   └── 2025-10-09_browser-page-management.md
│   ├── plans/
│   │   └── 2025-10-09-browser-page-management.md
│   └── prs/
│       └── pr_456_browser_pages.md
└── searchable/                    # 用于搜索的符号链接目录
```

**为何强大？**

1. **持久记忆**：调研和计划在清空上下文后依然存在
2. **知识复用**：未来的功能可以参考过去的决策
3. **团队协作**：共享调研让每个人都能受益
4. **审计追踪**：几个月后仍能看到决策的来龙去脉

`searchable/` 目录包含指向所有文档的硬链接，方便 Claude 的搜索工具在需要时找到相关上下文。

---

## 为什么这套工作流有效

这套工作流之所以有效，是因为它契合了人类和 AI 各自最佳的工作方式：

**对 AI（Claude）而言：**

- 明确目标：每个阶段只做一件事
- 相关上下文：只加载所需内容，不冗余
- 验证循环：自动化检查防止偏差
- 文件记忆：不需要跨会话"记住"内容

**对人类（我和你）而言：**

- 认知负担：每次一个阶段，可管理
- 信心：扎实的计划减少不确定性
- 质量：多个验证节点早发现问题
- 速度：并行调研加清晰阶段划分 = 更快交付

**对代码库而言：**

- 文档化：每个功能都有调研记录和计划
- 一致性：遵循调研阶段发现的已有模式
- 可维护性：未来的开发者能理解决策背景
- 质量：系统化验证 = 更少 bug

---

## 建议

**1. 不要跳过调研**

即使你觉得自己已经熟悉代码库，也要跑一遍调研。你会发现一些被遗忘的模式和边界情况。

**2. 比你以为的更多地迭代计划**

早期的计划总是太浅。现在我为规划预留 30–45 分钟，迭代 5 次以上。时间投入是值得的。

**3. 对上下文毫不留情**

如果上下文达到 60%，停下来问自己："有什么可以保存到文件里、之后再引用的？" 通常是调研结论或计划细节。

**4. 手动测试同样重要**

自动化测试捕捉代码层面的问题，手动测试捕捉 UX 问题、性能问题和真实场景中的边界情况。两者都要做。

**5. 实现过程中更新计划**

如果在第二阶段发现了影响第三阶段的新情况，更新计划文件，让它始终是唯一可信来源。

**6. 坚持使用 `thoughts/` 目录**

所有调研文档、计划和笔记都放进 `thoughts/`。

未来的你会感谢现在的你。

---

## 如何开始

**1. 创建命令文件**

在 `.claude/commands/`（或 `.cursor/commands/`）目录下创建以下文件：

- `research_codebase.md`
- `create_plan.md`
- `implement_plan.md`
- `validate_plan.md`

可以根据我分享的命令进行调整，也可以创建自己的版本。

**2. 创建符号链接的 `thoughts/` 目录**

```bash
mkdir -p thoughts/{personal,shared,searchable}
mkdir -p thoughts/shared/{research,plans,prs}
mkdir -p thoughts/personal/{tickets,notes}
```

**3. 用完整工作流完成一个功能**

选一个小功能，不要一次性学所有东西：

1. 调研 → 清空上下文
2. 规划（迭代）→ 清空上下文
3. 实现（一个阶段）→ 清空上下文
4. 验证 → 清空上下文

如此循环。

**4. 观察什么有效**

完成第一个功能后，反思：

- 在哪里卡住了？
- 命令里有哪些地方可以更清晰？
- 是否保持了低于 60% 的上下文？

迭代工作流本身。

---

## 结语：元技能——上下文工程

我真正学到的是：与 AI 协作，并不总是关于提出正确的问题，而是工程化出正确的上下文。

每次调用 Claude，你都在将特定的上下文加载到它的工作记忆中。就像你不会为了修改一个函数而编译整个代码库一样，你也不应该为了实现一个功能而加载整个项目的历史。

我分享的这套工作流，就是上下文工程的实践体现：

- **调研**：加载上下文以理解
- **规划**：加载上下文以设计
- **实现**：加载上下文以执行
- **验证**：加载上下文以确认

每个阶段目标明确，产出产物，为下一个阶段清场。

如果你还在与 AI 编程时反复碰壁，对不断触及上下文限制感到沮丧，试试这套工作流。

从小处开始，迭代，让它成为你自己的方法。

感谢阅读，

— Ashley Brooke Ha

---

## 附录：快速参考

### 四阶段工作流

**1. 调研（@research_codebase.md）**

- 理解现有代码
- 启动并行 agent
- 生成调研文档
- 清空上下文

**2. 规划（@create_plan.md）**

- 创建实现计划
- 迭代 5 次以上
- 定义成功标准
- 清空上下文

**3. 实现（@implement_plan.md）**

- 每次执行一个阶段
- 运行自动化验证
- 进行手动测试
- 各阶段之间清空上下文

**4. 验证（@validate_plan.md）**

- 系统性验证
- 生成验证报告
- 确保没有遗漏
- 清空上下文

### 上下文管理原则

- 永远不超过 60% 的上下文容量
- 每个主要阶段后清空上下文
- 所有内容保存到 `thoughts/` 目录（`npx humanlayer thoughts init`）
- 引用文件而不是将内容保留在记忆中
- 使用并行 agent 高效收集信息

### 目录结构

```
thoughts/
├── [personal]/           # 个人笔记与工单
│   ├── tickets/
│   └── notes/
├── shared/               # 团队共享文档
│   ├── research/
│   ├── plans/
│   └── prs/
└── searchable/          # 用于搜索的硬链接
```

---

## 参考资料

**视频**

- Advanced context engineering for coding agents
- 12-Factor Agents: Patterns of reliable LLM applications — Dex Horthy, HumanLayer
- Advanced Context Engineering for Agents

**文章**

- The New Skill in AI is Not Prompting, It's Context Engineering — Phil Schmid on Context Engineering
- Effective context engineering for AI agents — Anthropic on Context Engineering for AI Agents

**工具与资源**

- [Humanlayer GitHub](https://github.com/humanlayer/humanlayer) — 上下文管理与 `thoughts/` 目录工具
