# Claude Code Insights（使用洞察报告）

**361 条消息，38 个会话（共 65 个）| 2026-04-08 至 2026-04-20**

---

## 总览

**运转良好的地方：** 你已搭建起一套真正实用的内容本地化流水线——绕过付费墙抓取文章、按术语表规则翻译、输出精排版的中文 PDF。你在多智能体编排方面的系统性学习方式，以及在选股工作中坚持数据驱动分析、拒绝接受推测性建议的态度，都体现出你驾驭 Claude 的清醒意图。[→ 你做到的亮点](#你做到的亮点)

**阻碍你的地方：** 在 Claude 这侧，它频繁对你的环境做出错误判断——包名错、端口错、配置文件错——导致令人沮丧的反复重试（例如 mcp-drawio 根本不存在，或试图 SSH 到远程服务器而非本地操作）。在你这侧，Claude 在每次会话开始时往往缺乏足够的环境上下文，难以避免这些弯路；你的翻译工作流也在每次会话中从头解释，而不是编码为可复用的规则。[→ 哪些地方出了问题](#哪些地方出了问题)

**可快速尝试的改进：** 为你的翻译工作流创建一个自定义 skill（通过 `/skill`）——它已经足够固定，完全可以编码为单条命令，其中包含你的术语表规则、图片处理逻辑和输出格式。另外，考虑添加 hook 在安装前自动验证包是否存在，这能短路掉你最常见的摩擦点。[→ 值得尝试的功能](#值得尝试的现有功能)

**更大胆的工作流：** 随着模型能力提升，你的翻译流水线可以实现完全自治——一条命令处理绕付费墙、资产下载、术语表约束翻译和 PDF 生成，全程自我校验，无需人工看守。你的选股系统可以演进为迭代式回测循环，让 Claude 自动扫描阈值参数并给出有统计支撑的推荐，而不是每次只跑一遍脚本。[→ 未来展望](#未来展望)

---

## 数据概览

| 指标 | 数值 |
|---|---|
| 消息数 | 361 |
| 代码行变动 | +11,275 / -370 |
| 涉及文件数 | 65 |
| 天数 | 11 |
| 日均消息数 | 32.8 |

---

## 你在做什么

### 博客与文章翻译（约 7 个会话）

将英文技术文章（Medium、Datadog 等）翻译为中文，包括图片下载与 PDF 转换。使用 Playwright MCP 绕过付费墙、抓取内容、管理术语表规则，输出格式化的 Markdown/PDF。

### 本地 LLM 与 AI 工具搭建（约 8 个会话）

搭建和调试本地 LLM 基础设施，包括 Gemma4、Qwen 模型、Open WebUI、Hermes 以及微信机器人集成。Claude Code 协助处理配置调试、端口冲突、模型服务崩溃，以及 Apple Silicon 上的性能优化。

### 多智能体编排与 Multica（约 4 个会话）

使用 Multica 和 Claude Managed Agents 学习并构建多智能体系统，系统性地完成涵盖工具、配置、hooks 和编排的实操教程。Claude Code 引导了结构化学习流程、创建了文档，并协助排查 CLI 和 Docker 问题。

### 量化选股（Plan B）（约 3 个会话）

优化并运行 Plan B 选股系统，包含自动交易日检测、数据驱动的阈值优化和报告生成。Claude Code 执行分析脚本、实现逻辑改进，并生成带结果的 HTML 报告。

### 开发环境与工具配置（约 8 个会话）

搭建和配置开发工具，包括 GitHub CLI 认证、MCP server（dbay、drawio）、Homebrew 包、SSH 连接以及 Claude Code 本身（CLAUDE.md、skills）。Claude Code 诊断缺失依赖、解决 PATH 问题、管理认证流程。

---

### 你最常做的事（按会话数）

| 任务类型 | 会话数 |
|---|---|
| 翻译 | 6 |
| 调试 | 5 |
| 排障 | 4 |
| 搭建与配置 | 4 |
| 信息咨询 | 4 |
| 运行 Plan B 选股 | 4 |

### 最常用工具（按调用次数）

| 工具 | 次数 |
|---|---|
| Bash | 508 |
| Edit | 132 |
| Read | 125 |
| Write | 51 |
| ToolSearch | 35 |
| TaskOutput | 19 |

---

## 你如何使用 Claude Code

你是一个**动手型探索者**，将 Claude Code 当作跨越多类任务的万能瑞士军刀——从将文章翻译为中文，到配置本地 LLM 基础设施，到运行选股脚本，到构建 GUI 工具。12 天内 38 个会话、361 条消息，你保持着**高频、短平快、目标导向**的使用节奏。许多会话是快速的一次性任务（创建文件、运行脚本、列出目录），另一些则是雄心勃勃的多阶段项目，比如搭建带模型切换器的 Open WebUI，或完成多智能体编排教程。你高度依赖 Bash（508 次调用），让 Claude 主导执行，但**在出错时果断介入**——当 Claude SSH 到远程服务器而不是你的本地 Mac 时你打断它，当它无法绕过 Medium 付费墙时你重新引导，当它使用错误配置文件时你纠正它。

你的摩擦模式揭示出你**能容忍迭代，但期望 Claude 快速学会**。16 起"走错方向"事件和 13 起"代码有 bug"问题表明 Claude 频繁需要纠偏——包名错、端口错、CLI 参数错——但你 84% 的"完全/基本达成"率和 90% 的满意度说明你有足够的耐心度过这些磕碰。你尤其擅长**识别 Claude 走偏的时机**并快速转向，比如在遇到计费限制时从 Claude API 切换到 Multica，或在 GitHub 认证时从 HTTPS 改为 gh OAuth。你的翻译工作（最常见的目标）已形成精练的工作流：通过 Playwright 抓取内容、下载图片、输出精排版中文 Markdown，有时还转换为 PDF——这是一条你在多次会话中反复打磨过的流水线。

**核心模式：** 你运行频繁、多样、行动导向的会话，将执行委托给 Claude，但在它走错路时快速、果断地介入。

---

### 用户响应时间分布

| 响应时间段 | 次数 |
|---|---|
| 2–10 秒 | 4 |
| 10–30 秒 | 32 |
| 30 秒–1 分钟 | 63 |
| 1–2 分钟 | 78 |
| 2–5 分钟 | 71 |
| 5–15 分钟 | 21 |
| >15 分钟 | 14 |

**中位数：81.1 秒 · 平均数：207.3 秒**

### Multi-Clauding（并行会话）

| 指标 | 数值 |
|---|---|
| 重叠事件数 | 8 |
| 涉及会话数 | 10 |
| 占消息比例 | 13% |

你会同时运行多个 Claude Code 会话。当会话在时间上重叠时即判定为 multi-clauding，表明存在并行工作流。

---

## 你做到的亮点

38 个会话不到两周，你以 84% 的完成率在多样化任务中搭建起了令人印象深刻的多语言内容与自动化工作流。

### 网页→中文翻译流水线

你开发出一套精密的翻译工作流，使用 Playwright MCP 绕过付费墙、下载图片，并输出精排版的英文文章中文译本。你甚至将其扩展到 PDF 生成，支持正确的 CJK 渲染，将 Claude Code 变成了完整的内容本地化流水线。

### 多智能体编排学习

你系统性地完成了 Multica 多智能体编排的实操教程，覆盖工具、配置、hooks 和智能体协作的结构化学习阶段。在遇到计费限制时，你务实地从 API 方式切换到 Claude Code + Multica，表现出强烈的适应能力。

### 数据驱动选股自动化

你构建并迭代优化了 Plan B 选股系统，包含自动交易日检测和数据驱动的阈值优化。你推动 Claude 采用纯数据驱动的分析方式，拒绝推测性建议，并在选股逻辑之外生成了完整的分析报告。

---

### 最有帮助的 Claude 能力（按提及次数）

| 能力 | 次数 |
|---|---|
| 调试质量好 | 9 |
| 跨文件修改 | 8 |
| 主动提供帮助 | 6 |
| 代码编辑准确 | 6 |
| 解释清晰 | 5 |
| 搜索快速准确 | 3 |

### 任务完成情况

| 结果 | 次数 |
|---|---|
| 未达成 | 2 |
| 部分达成 | 4 |
| 基本达成 | 7 |
| 完全达成 | 25 |

---

## 哪些地方出了问题

你的会话频繁因 Claude 走错初始方向而受阻，需要多次纠偏循环，尤其集中在工具/包名、环境假设和过于激进的操作上。

### 对你环境的错误假设

Claude 反复猜错东西的位置、包的名称或你系统的配置方式，迫使你打断并重新引导。可以通过在 CLAUDE.md 或会话开头提供更多环境上下文（本地 Mac、已安装的具体工具）来减少此类问题。

**典型案例：**
- Claude 试图 SSH 到远程服务器去删除 Hermes，而不是在你的本地 Mac 上操作，你不得不打断并说明目标环境
- Claude 使用了错误的 Hermes/Qwen 配置文件名和端口（用 11434 而非 8080），导致反复连接失败，才最终找到正确配置

### 工具/包名错误，需要反复试错

Claude 经常猜错包名、CLI 参数或 Docker 镜像，白白消耗重试次数。考虑让 Claude 在安装前先验证包是否存在，或在项目文档中维护一份已知可用包的参考列表。

**典型案例：**
- Claude 尝试了不存在的 `mcp-drawio` 包，并遭遇 PATH 问题，最终才找到正确的 `@drawio/mcp` 并使用绝对路径
- Claude 在更新过程中给出了错误的 multica CLI 参数（`--backend`）和错误的 Docker 镜像名，需要多次重试才得以修正

### 过于激进或破坏性的操作

Claude 有时采取了超出必要范围的操作——关闭应用、应用未经测试的优化、进行推测性修改——导致你随后需要调试。可以通过让 Claude 在执行前先提出高风险操作的方案来规避这一问题。

**典型案例：**
- Claude 只需要重启 MCP 服务，却关闭了你整个 Chrome 浏览器，不必要地打断了你的工作流
- Claude 在没有草稿模型的情况下应用了 `--num-draft-tokens 5`，导致崩溃 bug，使 LLM 服务不稳定，需要完整的调试周期才能修复

---

### 主要摩擦类型（按次数）

| 类型 | 次数 |
|---|---|
| 走错方向 | 16 |
| 代码有 bug | 13 |
| 误解请求 | 4 |
| 改动过多 | 1 |
| 未知包 | 1 |
| API 错误 | 1 |

---

## 值得尝试的现有功能

### 建议添加到 CLAUDE.md 的内容

```
所有翻译默认输出简体中文，除非另有说明。按术语表保留 "vibe coding" 等技术术语不译。
```
**原因：** 翻译到中文是跨会话最高频的目标（6+ 个会话），每次重复说明很浪费。

```
在删除/修改任何内容之前，始终确认目标环境（本地 Mac 还是远程服务器）。
```
**原因：** Claude 多次混淆本地和远程目标（Hermes 删除、MCP 禁用），造成无谓的重试和用户沮丧。

```
不得关闭用户的浏览器或终止无关进程。只重启需要处理的具体服务或进程。
```
**原因：** Claude 只需要重启 MCP 服务，却关闭了用户整个 Chrome 浏览器，打乱了工作流。

```
安装包或配置 MCP server 时，先验证包名确实存在（如检查 npm/PyPI），再尝试安装。MCP server 命令使用绝对路径以避免 PATH 问题。
```
**原因：** 多个会话因包名错误（mcp-drawio、dbay-cli）和 PATH 解析失败造成反复重试。

```
编辑文件后，始终重新读取修改后的文件，检查是否存在重复或残留（如重复的函数定义），再继续。
```
**原因：** 13 个会话中出现了重复函数和残留产物导致的 buggy code 问题，需要额外的清理轮次。

---

### Custom Skills

**可复用的提示工作流，通过单条 `/命令` 触发**

**为什么适合你：** 你频繁翻译文章（6+ 个会话）。一个 `/translate` skill 可以将"抓取→翻译→下载图片→保存"的工作流标准化，让你不必每次重新解释流程。

```bash
mkdir -p .claude/skills/translate && cat > .claude/skills/translate/SKILL.md << 'EOF'
# Translate Article to Chinese
1. Fetch the article from the provided URL (use Playwright if paywalled)
2. Download all images to a local ./images/ folder
3. Translate the full article to 简体中文, keeping technical terms per glossary
4. Save as markdown with embedded image references
5. Do NOT close or interfere with the user's browser
EOF
```

### Hooks

**在特定生命周期事件时自动运行 shell 命令**

**为什么适合你：** 你在 13 个会话中遇到了 buggy code 摩擦（重复函数、编码问题）。一个在编辑后运行 linter 或重复检查的 post-edit hook 可以在你注意到之前就自动捕获这些问题。

```json
// 添加到 .claude/settings.json:
{
  "hooks": {
    "postToolUse": [
      {
        "matcher": "Edit|Write",
        "command": "python3 -c \"import sys, collections; lines=open(sys.argv[1]).readlines(); dups=[l for l,c in collections.Counter(lines).items() if c>1 and 'def ' in l]; print('WARNING: duplicate defs found: '+str(dups)) if dups else None\" \"$CLAUDE_FILE_PATH\" 2>/dev/null || true"
      }
    ]
  }
}
```

### Headless Mode

**以非交互方式从脚本中运行 Claude**

**为什么适合你：** 你定期运行 Plan B 选股脚本（4 个会话）。可以将其自动化为定时任务，无需手动交互即可运行分析并保存结果。

```bash
# 自动运行选股：
claude -p "Run the Plan B stock selection script at ~/plan-b/select.py, save results to ~/plan-b/results/$(date +%Y-%m-%d).md, and summarize the top picks" --allowedTools "Bash,Read,Write"
```

---

## 使用 Claude Code 的新方式

### 走错方向是你最大的瓶颈

16 个会话出现了"走错方向"摩擦——超过任何其他问题。在你的提示中前置约束条件。

Claude 频繁选错目标（远程 vs 本地）、错误的包、错误的配置文件和错误的端口。这个模式表明 Claude 在应该询问的时候选择了猜测。在 CLAUDE.md 中添加一个关于你环境的章节（macOS、本地服务、常用端口），将能消除大多数此类问题。也可以在相关请求前加上"在我的本地 Mac 上..."。

**可直接粘贴到 Claude Code 的提示：**
```
On my local Mac, remove Hermes completely. Check ~/Library, /usr/local, brew, and Docker. List what you find BEFORE deleting anything.
```

### 用标准模板打包翻译请求

你的翻译工作流是一致的，但每次都要重新解释。使用结构化的提示模板。

在 6 个翻译会话中，工作流始终如一：抓取 URL → 处理付费墙 → 下载图片 → 翻译为中文 → 保存为 Markdown。部分会话在付费墙和浏览器问题上有摩擦。一个预先说明处理方式的标准提示（先试 WebFetch，回退到 Playwright，绝不关闭 Chrome）将显著减少迭代次数。

**可直接粘贴到 Claude Code 的提示：**
```
Translate this article to 简体中文: [URL]. Steps: 1) Try WebFetch first. 2) If paywalled, use Playwright MCP (do NOT close my Chrome). 3) Download all images to ./images/. 4) Output as markdown with relative image paths. 5) Keep technical terms per glossary untranslated.
```

### 要求 Claude 在执行高风险操作前先确认

为搭建、配置和删除任务添加"提议后执行"模式，以避免走错方向的循环。

许多摩擦点来自 Claude 带着错误假设立即执行——错误的 SSH 目标、错误的包名、无权限的 sudo 命令。对于搭建/配置/删除任务，让 Claude 先提出方案能提前捕获大多数错误。这在你的 MCP 配置和服务管理工作中尤为重要。

**可直接粘贴到 Claude Code 的提示：**
```
I need to configure [X]. Before doing anything, list: 1) exactly what you'll install and from where, 2) what config files you'll modify, 3) what commands need elevated permissions. Wait for my approval before executing.
```

---

## 未来展望

你的 38 个会话呈现出一位跨翻译、自动化和本地基础设施高度使用 Claude Code 的高阶用户——通过自治化、并行化工作流消除摩擦的机会清晰可见。

### 带质量门控的自治翻译流水线

翻译是你最高频的使用场景，但仍涉及付费墙、图片下载和格式转换的手动反复。一个自治 agent 可以通过 Playwright 抓取文章、按术语表约束翻译、下载所有资产、生成 PDF 输出，并根据你的 CLAUDE.md 规范进行自我校验——全程只需一条命令。并行子 agent 可同时处理图片提取和术语表检查。

**快速入门提示：**
```
I need you to autonomously translate this article to Chinese: [URL]. Follow this full pipeline without stopping for confirmation: 1) Fetch the full article using Playwright (handle paywalls by extracting from rendered DOM), 2) Download all images and save to ./images/, 3) Translate to Chinese following our CLAUDE.md glossary rules (keep terms like 'vibe coding' untranslated), 4) Embed images with relative paths in the markdown, 5) Generate a PDF with proper Chinese font rendering using Puppeteer, 6) Self-review: re-read the translation and check for any glossary violations, missing images, or formatting issues, then fix them. Output a final status summary of what was done and any issues found during self-review.
```

### Plan B 选股与迭代式回测

你的选股工作流目前是单次脚本执行。一个自治 agent 可以对历史数据迭代阈值参数、并行运行回测、比较不同配置的性能指标，并给出带统计置信度的优化推荐——将手动分析变成自我优化的循环。

**快速入门提示：**
```
Run an autonomous optimization loop on the Plan-B stock selection strategy: 1) Read the current selection logic and identify all tunable thresholds/parameters, 2) Generate 5 parameter variations spanning conservative to aggressive, 3) For each variation, run the selection script against the last 90 trading days of data and capture results, 4) Score each variation by hit rate, average return, and max drawdown, 5) Pick the best-performing config and run it again on a held-out validation period, 6) Write a full analysis report in Markdown with comparison tables and the recommended configuration. If any run fails, debug and retry automatically. Save everything to ./optimization_results/.
```

### 自愈式本地基础设施搭建 Agent

你有 16 起摩擦事件源于走错方向——包名错、端口错、配置文件错。一个自治 agent 可以先探测实际系统状态（已安装的包、运行中的端口、配置文件位置），建立经过验证的环境模型，再执行变更并在失败时自动回滚。这将消除困扰你 Hermes、微信和 MCP 搭建会话的"猜测-修复"循环。

**快速入门提示：**
```
I need you to set up [SERVICE] on this machine. Follow this strict protocol: PHASE 1 - DISCOVER: Before making ANY changes, run diagnostic commands to map the current state: check OS/arch, installed package managers, running services and their ports, existing config files related to this service, and available disk/memory. Write findings to ./setup_audit.md. PHASE 2 - PLAN: Based on discovered state (not assumptions), write a step-by-step plan to ./setup_plan.md. For each step, note what could go wrong and how to verify success. PHASE 3 - EXECUTE: Run each step, verify it succeeded before proceeding. If any step fails, diagnose using actual error output, adjust approach, and retry (max 3 retries per step). Back up any config files before modifying them. PHASE 4 - VERIFY: Run end-to-end health checks confirming the service works. Document the final state and any deviations from the plan in ./setup_report.md.
```

---

## 趣事

> **"Claude 贴心地关掉了用户整个 Chrome 浏览器，其实它只需要重启一个 MCP 服务"**
>
> 在一次 Medium 文章翻译会话中，Claude 有点过于积极，关闭了用户整个 Chrome 浏览器，而不是仅仅重启它所需要的后台服务——效率的名义下造成的附带损伤。
