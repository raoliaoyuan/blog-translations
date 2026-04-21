# Anthropic 发布 Claude Managed Agents（让 AI 智能体工作流真正落地）

> 作者：Joe Njenga
> 发布日期：2026年4月9日 · 阅读时长约 8 分钟
> 原文链接：[Medium](https://medium.com/@joenjega/anthropic-launches-claude-managed-agents-that-make-agentic-ai-workflows-real)

---

Claude Managed Agents 让你不再为了拼凑脚本、使智能体（agent）运转而耗费时间。

我刚测试了全新的 Claude Managed Agents，发现了 AI 智能体工作流中一直缺失的那个环节。

如果你一直在使用或构建 AI 智能体，一定熟悉那个老问题。

用在基础逻辑上的时间，远多于用在产品本身的时间。

智能体循环（agent loop）、工具执行（tool execution）、上下文管理（context management）、沙箱隔离（sandboxing）和会话管理（session handling）——在写一行真正的业务逻辑之前，所有这些都要你从头搭建。

任务执行到一半出了问题，你又得回头调试基础设施，而不是继续交付产品。

这正是 Claude Managed Agents 承诺解决的问题。Anthropic 这次给的不是又一个让你自己套循环的 API，而是直接把运行时（runtime）交到了你手里。

这是一个完全托管的云端运行环境，Claude 在其中独立完成文件读取、命令执行、网页浏览和代码运行。

会话连续性和上下文管理均已内置处理。我花时间做了完整的测评，看它是否兑现了这个承诺。

## Claude Managed Agents

Anthropic 这次发布了两样东西：

其一是 Claude Managed Agents——一套完全托管、运行于 Anthropic 基础设施上的智能体 harness。你定义智能体、发起任务，其余一切——容器、工具、执行过程、会话——均由 Anthropic 的云端负责。

其二是 Claude Agent SDK（前身为 Claude Code SDK）——一个将驱动 Claude Code 的同款智能体循环嵌入你自己应用的 Python 和 TypeScript 库。你自行托管，但所有难点均已预先构建好。

两者解决同一个问题，区别在于智能体运行的位置：

- **SDK**——智能体运行于你自己的基础设施内
- **Managed Agents**——智能体运行于 Anthropic 云端，完全托管

对大多数读者而言，Managed Agents 是意义更重大的发布。本文将聚焦于 Claude Managed Agents。

## 四个核心概念

Managed Agents 围绕四个核心概念构建。理解了这四个概念，整个系统就豁然开朗了：

你的应用向运行于 Anthropic 云端的会话发送事件，智能体与环境均已在其中配置完毕。

- **智能体（Agent）**——你的配置项：模型、系统提示词（system prompt）、工具、MCP servers 和 skill。定义一次，之后在每个会话中通过 ID 引用。
- **环境（Environment）**——一个预装了常用包（Python、Node.js、Go 等）、配置了网络访问规则并挂载了文件的云端容器，是你的智能体的操作空间。
- **会话（Session）**——智能体在环境中运行的实例，执行特定任务。文件、对话历史和上下文在会话生命周期内全程持久化。
- **事件（Events）**——在你的应用与智能体之间流动的消息：用户轮次（user turns）、工具返回结果、状态更新和流式响应。

以下是代码示例。你只需创建一次智能体：

```python
import anthropic

client = anthropic.Anthropic()

# 创建智能体——只做一次，之后通过 ID 复用
agent = client.beta.agents.create(
    model="claude-sonnet-4-6",
    system="You are a software engineer. Fix bugs, run tests, and report results.",
    tools=[{"type": "bash"}, {"type": "file_operations"}, {"type": "web_search"}],
    name="bug-fixer"
)

print(agent.id)  # 保存此 ID——后续每个会话都会引用它
```

然后创建会话并发送任务：

```python
# 创建包含所需包的环境
environment = client.beta.environments.create(
    packages=["pytest", "requests"]
)

# 创建会话，引用你的智能体和环境
session = client.beta.sessions.create(
    agent_id=agent.id,
    environment_id=environment.id
)

# 以事件形式发送任务
response = client.beta.sessions.events.create(
    session_id=session.id,
    content="Find and fix the failing tests in auth.py"
)
```

整个设置就是这些：一个智能体定义、一个环境、一个会话，之后交给 Claude 自行完成。

## 智能体循环如何运转

会话启动后，Claude 不会只响应一次就等待。

它运行一个连续循环：接收提示词、评估任务、调用工具、处理结果，循环往复，直到任务完成。每个完整的来回为一个轮次（turn）。

Claude 在每个轮次自主评估、调用工具、处理结果，循环执行，直到任务完成或触及上限。

以下是一个真实任务的示例："找出并修复 auth.py 中失败的测试"。

- **第 1 轮**——Claude 通过 Bash 运行测试套件，返回三个失败。
- **第 2 轮**——Claude 读取 auth.py 和测试文件，理解问题所在。
- **第 3 轮**——Claude 修改文件并重新运行测试，三个全部通过。
- **最终轮**——Claude 返回纯文本响应，无工具调用，任务结束。

以下是对应的代码示例：

```python
import anthropic

client = anthropic.Anthropic()

async for event in client.beta.sessions.stream(
    session_id=session.id,
    event={
        "type": "user",
        "content": "Find and fix the failing tests in auth.py"
    }
):
    # 查看 Claude 每个轮次的操作
    if event.type == "assistant_message":
        print(event.content)

    # 捕获最终结果
    if event.type == "result":
        print(f"Done: {event.result}")
        print(f"Turns used: {event.num_turns}")
        print(f"Cost: ${event.total_cost_usd:.4f}")
        session_id = event.session_id  # 保存以便后续恢复
```

这个流式输出让你完整地看到每个工具调用、返回结果和轮次的实时状态。

## 上下文管理

大多数自搭智能体方案的瓶颈都在上下文。

每个轮次都会向上下文窗口（context window）中累积内容：提示词、工具定义、文件读取内容、命令输出和对话历史。一旦触及上限，会话就会中断。

Managed Agents 自动处理这一问题。

当上下文窗口接近上限时，系统会通过摘要压缩（compacts）旧历史来释放空间，同时保留近期交互和关键决策。这样会话得以不中断地持续进行。

## 三项控制手段

**推理深度（Effort level）**——控制 Claude 每个轮次的推理深度。

需要有意识地设置，因为它直接影响 token 用量和费用。

**最大轮次与预算（Max turns and budget）**——在循环失控之前设置上限。

```python
session = client.beta.sessions.create(
    agent_id=agent.id,
    environment_id=environment.id,
    max_turns=20,           # 执行 20 个工具调用轮次后停止
    max_budget_usd=0.50     # 或花费达到 $0.50 时停止
)
```

任意限制触发后，会话会返回明确的结果子类型，告知你停止原因；如有需要，可通过 session ID 恢复执行。

**权限模式（Permission mode）**——控制 Claude 可以在无需询问的情况下执行哪些操作。

- `default`——通过回调（callback）对未预先批准的操作进行拦截
- `acceptEdits`——自动批准文件编辑，对 shell 命令仍进行拦截
- `bypassPermissions`——跳过所有询问直接执行，仅适用于隔离容器和 CI 环境

## 任务执行中途可随时干预

会话运行期间，你可以发送额外事件来调整方向、补充上下文或停止执行。

```python
# 发送中途修正指令
client.beta.sessions.events.create(
    session_id=session.id,
    content="Actually, only fix the auth_token tests — leave the login tests alone"
)
```

如果 Claude 的方向不对，无需等它跑完。

会话同样是持久化的，记录 session ID 后可随时从上次中断处恢复。

```python
# 恢复之前的会话
async for event in client.beta.sessions.stream(
    session_id="sess_abc123",   # 来自之前的运行
    event={"type": "user", "content": "Continue — now fix the payment module too"}
):
    if event.type == "result":
        print(event.result)
```

## Claude Managed Agents 工具集

手动搭建智能体时，工具执行是最耗时的环节之一。

编写封装器、处理错误、将结果回传到上下文——Managed Agents 已经替你做好了这一切。

以下是完整工具集，按类别分组：

**文件操作（File operations）**

- `Read`——读取容器内的任意文件
- `Write`——创建新文件
- `Edit`——修改已有文件

**搜索（Search）**

- `Glob`——按模式匹配查找文件
- `Grep`——使用正则表达式搜索内容

**执行（Execution）**

- `Bash`——运行 shell 命令、脚本、git 操作、安装包、运行测试

**网络（Web）**

- `WebSearch`——搜索互联网
- `WebFetch`——抓取并解析任意 URL 的完整页面内容

**编排（Orchestration）**

- `Task`——启动子智能体（subagent）执行隔离任务
- `Skill`——调用可复用工作流
- `AskUserQuestion`——暂停并请求人工输入
- `TodoWrite`——在会话中跟踪多步骤工作进度

除内置工具外，你还可以通过 MCP servers 接入外部服务，并用自定义处理器定义自己的工具。

## 快速上手

Claude Managed Agents 目前处于 beta 阶段。

所有 API 账户默认开启访问权限；只要有 Claude API key，即可开始使用。

你需要准备以下内容：

- platform.claude.com 的 Claude API key
- 所有请求须携带 `managed-agents-2026-04-01` beta header
- Python 或 TypeScript SDK——SDK 会自动设置该 header

安装 SDK：

```bash
pip install anthropic
```

设置 API key：

```bash
export ANTHROPIC_API_KEY=your-api-key
```

不到 20 行代码，完成你的第一个可运行智能体：

```python
import anthropic
import asyncio

client = anthropic.Anthropic()

async def main():
    agent = client.beta.agents.create(
        model="claude-sonnet-4-6",
        system="You are a helpful engineering assistant.",
        tools=[{"type": "bash"}, {"type": "file_operations"}],
        name="my-first-agent"
    )

    environment = client.beta.environments.create(
        packages=["pytest"]
    )

    session = client.beta.sessions.create(
        agent_id=agent.id,
        environment_id=environment.id,
        max_turns=10,
        max_budget_usd=0.25
    )

    async for event in client.beta.sessions.stream(
        session_id=session.id,
        event={"type": "user", "content": "List all Python files in this directory"}
    ):
        if event.type == "result":
            print(event.result)
            print(f"Cost: ${event.total_cost_usd:.4f}")

asyncio.run(main())
```

另有三项功能处于研究预览阶段：

- 产出结果（Outcomes）
- 多智能体协调（Multi-agent coordination）
- 持久化记忆（Persistent memory）

以上三项均需在 claude.com/form/claude-managed-agents 单独申请访问。

## 总结

Claude Managed Agents 的核心思路很扎实：智能体循环、上下文管理、工具执行和会话连续性，全部内置。

原本需要数周才能搭建的基础设施，现在只需一个配置文件加一次 API 调用。这对于快速构建生产级智能体是重要的一步。

代价是，输出的质量仍然取决于输入的质量。

你试过 Claude Managed Agents 了吗？欢迎在评论区分享你的体验。
