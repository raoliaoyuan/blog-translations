# CLAUDE.md 最佳实践：面向机器的 7 条格式化规则（7 formatting rules for the Machine）

> 作者：Gábor Mészáros
> 发布日期：2026年3月3日
> 原文链接：https://dev.to/cleverhoods/-claudemd-best-practices-7-formatting-rules-for-the-machine-3d3l

---

我曾亲眼目睹一个智能体（Agent）无视了我两小时前刚写下的规则。

那不是一条模糊的规则，而是一条非常具体的规则：“在提交（commit）前运行 pytest”。它就写在 `CLAUDE.md` 里，位于项目描述和 lint 设置之间的第二段。智能体阅读了该文件，我在上下文（context）中看到了它。但它就是……没有执行。

我将同样的指令移动到了 `## Testing` 标题下，用反引号包裹了 `pytest`，并添加了一行理由（rationale）。下次运行时，智能体一字不差地执行了。

```markdown
## Testing
- `pytest` — 在提交前运行测试
```

指令没有改变，但信号强度（Signal strength）变了。

在[上一篇文章](https://dev.to/cleverhoods/why-bootstrap-should-be-the-first-command-in-every-agent-session-4jg2)中，我们让智能体建立了方向感 —— `/bootstrap` 加载了地图、工作流和边界。但方向感和执行力（Compliance）是两回事。你可以给某人一份完美的简报，但如果简报是一堆密密麻麻的文字，你依然会失去他们。智能体也是如此。

```bash
/bootstrap
```

问题不在于你的指令是否已加载，而在于智能体是否遵循它们。

## 对比

这里有两条指令，内容相同，形式不同。

**版本 A：**

> 在本项目中工作时，请始终确保在提交任何更改之前运行测试套件。运行测试的命令是 `pytest`，你应该在项目根目录下运行它。如果测试失败，请在提交前修复它们。另外，请确保使用 `ruff` 进行格式化。

**版本 B：**

```markdown
## Testing
- `pytest` — 每次提交前在项目根目录运行
- 提交前修复所有失败项

## Formatting
- `ruff check --fix && ruff format` — 提交前运行
```

内容完全一样。版本 B 被执行了，而版本 A 被埋没了。

这不仅仅关乎美感。标题、代码围栏（code fences）和列表等结构化元素为智能体创造了可以捕捉的锚点（anchor points）。散文（prose）式的段落则不行。你提供的结构越多，每条指令落地的可靠性就越高。

## 不仅仅是长度问题

你已经学会了保持 `CLAUDE.md` 短小精悍。这是一个好的开始，但还不够。一个 20 行的文本段落和 200 行的段落一样容易丢失。变量不是字数，而是结构。

一个没有标题、没有代码块、没有理由的简短文件，其表现会逊色于一个结构良好的长文件。

**长度是上限，格式是信号。**

## 七条结构化规则

这些不是内容指南，而是格式选择，它们决定了指令能否从文件成功转化为智能体的行为。我将先介绍三条你在其他指南中找不到的规则，然后再涵盖另外四条大家都提到但没人解释原因的规则。

### 1. 包含理由（Include rationale）

“严禁强制推送（force push）”是一条指令。“严禁强制推送 —— 会重写共享历史，对协作者来说不可恢复”则是一条智能体会权衡的指令。

```markdown
# 没有理由
- 严禁在项目根目录使用 `rm -rf`
- 提交前务必运行测试
- 不要手动修改 `package-lock.json`

# 包含理由
- 严禁在项目根目录使用 `rm -rf` —— 无法恢复
- 提交前务必运行测试 —— CI 会拒绝未测试的代码
- 不要手动修改 `package-lock.json` —— 会导致合并冲突和依赖解析问题
```

理由不仅是解释，它还给了智能体泛化的能力。理解了为什么禁止强制推送的智能体，即使没被告知，也会主动避免使用 `git reset --hard origin/main`。**“为什么”能将单一规则转化为一类行为。**

```bash
git reset --hard origin/main
```

这是最被低估的格式选择。每一条禁令都应该附带它的理由。

### 2. 保持标题层级扁平（Keep heading hierarchy shallow）

三层就足够了。H1 用于文件标题，H2 用于章节，H3 用于子章节。仅此而已。

```markdown
# 项目名称 (H1)
## 测试 (H2)
### 单元测试 (H3)
```

深度嵌套会分散注意力。一个 H5 标题会与它上方的所有标题争夺智能体的焦点。它不会丢掉 H2，但这种层级结构会产生歧义，即哪一层才是起主导作用的。**扁平结构能让每条指令都浮现在表面。** 如果你需要用到 H4，你可能需要一个单独的文件。

### 3. 文件命名具有描述性（Name files descriptively）

当智能体搜索你的项目时 —— 浏览目录列表、运行 glob、决定阅读哪个文件 —— 文件名是第一道过滤器。它先于内容、先于标题、先于一切。

```text
# 修改前
docs/guide.md
docs/notes.md
scripts/setup.sh

# 修改后
docs/api-authentication.md
docs/deployment-checklist.md
scripts/setup-local-dev.sh
```

智能体看到目录列表并挑选要打开的文件。`api-authentication.md` 能告诉它该文件是否与当前任务相关。`guide.md` 则迫使它必须打开并阅读后才能做出决定。**描述性的名称为智能体节省了一个往返（round trip）。** 在一个拥有几十个文件的项目中，这种节省是巨大的。

这适用于智能体可能发现的任何文件：文档、脚本、配置。

---

现在是那四条你听过的规则 —— 但这次带有“为什么”。

### 4. 使用标题（Use headers）

智能体扫描标题就像开发者扫描 README 一样：将其作为目录。标题意味着“新话题，重置注意力”。

```markdown
# 修改前
项目使用启用了严格模式的 TypeScript。我们使用 vitest 进行测试。CI 流水线运行在 GitHub Actions 上。

# 修改后
## 语言 (Language)
启用了严格模式的 TypeScript。

## 测试 (Testing)
- `npx vitest` — 从项目根目录运行

## CI
- `.github/workflows/` — GitHub Actions
```

每个标题只涵盖一个主题。智能体可以直接导航到正确的章节，而不是解析整个段落。没有标题，每条指令都会为了争夺注意力而相互竞争。

### 5. 将命令包裹在反引号中（Wrap commands in backticks）

散文中的命令会被读作描述，而代码块中的命令会被视为可执行的。

```markdown
# 修改前
你可以通过运行 npm run lint 来运行 linter，通过运行 npm test 来运行测试。

# 修改后
- `npm run lint` — 检查问题
- `npm test` — 运行测试套件
```

如果你从这篇文章中只学到一件事，那就是**用反引号包裹你的命令**。这是影响力最高的一项改变 —— 代码围栏里的命令就是命令，句子里的命令只是建议。

### 6. 使用标准的章节名称（Use standard section names）

智能体已经在数百万个 README 文件上进行过训练。它们知道 `## Testing`、`## Commands`、`## Structure` 和 `## Conventions` 意味着什么。这些名称自带上下文。

熟悉的名字是信号，创意的名字是噪音。

| 建议避免使用 (Instead of) | 建议使用 (Use) |
| :--- | :--- |
| Quality Assurance | Testing |
| Development Guidelines | Conventions |
| Operational Instructions | Commands |
| Safety and Compliance | Boundaries |
| Project Organization | Structure |


### 7. 使指令具有可操作性（Make instructions actionable）

“遵循最佳实践”不是一条指令。“使用 `ruff` 进行格式化，提交前运行”才是。

测试标准是：**智能体现在能否直接执行这条指令，而不需要问任何澄清性问题？** 如果不能，它就太模糊了。

```markdown
# 修改前
确保维护代码质量并遵循我们的标准。

# 修改后
## 约定 (Conventions)
- 提交前使用 `ruff format` 进行格式化
- 所有公共函数需添加类型注解
- 生产环境代码中严禁使用 `print()` —— 请使用 `logging`
```

每条指令都应该通过“立即行动”测试。如果无法行动，那它只是一个愿望，而不是指令。

## 复合效应（The compound effect）

单独看每一条规则都是微小的改进。但它们结合在一起是乘法效应 —— 不是因为规则在叠加，而是因为它们在相互强化。标题创建了章节，章节容纳了代码块，代码块包含了可执行命令，理由解释了原因，描述性文件名将注意力引导到正确的文件，扁平层级让一切都易于查找。

这是一个应用了全部七条规则后的真实对比：

**修改前：**

> 这个项目是一个 Python CLI 工具。我们使用 pytest 进行测试，使用 ruff 进行 lint。确保在提交任何内容之前运行测试。源码在 src/myapp 中，测试在 tests/ 中。不要修改 dist/ 文件夹中的任何内容，因为那是生成的。另外，我们还有一些关于编写测试的规则 —— 它们应该测试行为而不是实现细节，并且使用 parametrize 而不是编写许多执行相同操作的独立测试函数。

**修改后：**

```markdown
## 测试 (Testing)
- `pytest` — 每次提交前在项目根目录运行
- 测试行为而非实现 —— 断言结果，而非内部调用
- 当用例共享相同的断言形式时，使用 `@pytest.mark.parametrize`

## 格式化 (Formatting)
- `ruff check --fix && ruff format`

## 结构 (Structure)
- 源码：`src/myapp/`
- 测试：`tests/`

## 边界 (Boundaries)
- `dist/` — 生成目录，严禁修改
```

同样的信息，一半的字数，每一条指令都能落地。

## 何时重构

如果你注意到：
- 智能体为你漏掉文件中的某条指令而道歉
- 同一条规则在连续的对话中被违反
- 你不断向一条指令添加更多文字，希望智能体能“明白”
- 你的 `CLAUDE.md` 是一个没有标题的长章节
- 命令出现在句子里而不是代码块中

你的指令不需要更多内容，它们需要更多**结构**。

## 与 /bootstrap 的联系

在之前的文章中，我们构建了交付系统：`backbone.yml` 映射项目，Mermaid 绘制工作流，`/bootstrap` 在几秒钟内加载两者。那是定向层（orientation layer） —— 智能体知道了它在哪里以及事情是如何运作的。

这是关于**注意力预算分配**的。智能体的上下文窗口（context window）有限。重要的不仅是窗口里有什么，还有智能体在每一步中如何决定什么才是相关的。结构能让你的指令在竞争中胜出。

有方向感而无执行力，意味着智能体了解你的项目但无视你的规则。有执行力而无方向感，意味着智能体遵循指令但在错误的地方工作。你两者都需要。

## 尝试一下

1. 打开你的 `CLAUDE.md`（或你的智能体读取的任何指令文件）
2. 找到最长的文本段落
3. 拆解它：每个话题一个标题，每个命令一个代码块，每条禁令一句理由。
4. 在智能体上运行你昨天运行过的相同任务。

指令没有改变，信号变了。

**不要只是写更多的指令，格式化你已有的指令。**
