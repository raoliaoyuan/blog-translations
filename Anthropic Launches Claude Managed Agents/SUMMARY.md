# 内容总结：Anthropic 发布 Claude Managed Agents

## 文章核心观点

本文介绍了 Anthropic 于 2026 年 4 月发布的 Claude Managed Agents，核心价值主张是：**将智能体运行所需的基础设施完全托管化**，让开发者无需自行搭建 agent loop、上下文管理、沙箱隔离和会话管理，直接通过 API 获得一个生产可用的智能体运行时。

Anthropic 同期发布了两样东西：

- **Claude Managed Agents**——完全托管，智能体运行于 Anthropic 云端
- **Claude Agent SDK**（前身为 Claude Code SDK）——自托管，将同款 agent loop 嵌入开发者自己的应用

---

## 四个核心概念

| 概念 | 说明 |
|---|---|
| **Agent** | 配置项：模型、system prompt、工具、MCP servers、skill，定义一次后通过 ID 复用 |
| **Environment** | 云端容器：预装包、网络规则、挂载文件，是智能体的操作空间 |
| **Session** | 智能体在环境中运行的实例，文件、对话历史、上下文全程持久化 |
| **Events** | 在应用与智能体之间流动的消息：user turns、工具返回结果、状态更新、流式响应 |

---

## 智能体循环机制

会话启动后 Claude 持续运行：接收提示词 → 评估任务 → 调用工具 → 处理结果 → 循环，直到任务完成或触及上限。每个完整来回为一个轮次（turn）。

---

## 三项关键控制手段

- **Effort level**——控制每轮推理深度，直接影响 token 用量
- **Max turns / max_budget_usd**——防止循环失控的硬上限
- **Permission mode**——`default`（回调拦截）/ `acceptEdits`（自动批准文件编辑）/ `bypassPermissions`（适用于隔离容器/CI）

---

## 内置工具集

文件操作（Read/Write/Edit）、搜索（Glob/Grep）、执行（Bash）、网络（WebSearch/WebFetch）、编排（Task/Skill/AskUserQuestion/TodoWrite），另支持 MCP servers 和自定义工具。

---

## Claude Managed Agents 与 Claude Code web Sandbox 的关系

> 本节内容来自本会话的补充讨论。

### 本质关系

两者共享同一套底层基础设施。文章明确说明 Claude Agent SDK 是"Claude Code SDK 的前身"，揭示了核心事实：**Claude Code 本身就是用这套技术栈构建的产品**，Managed Agents 是把同样的能力以 API 形式开放给开发者。

### 相同之处

- 均运行于 Anthropic 云端容器
- 工具集完全相同（Bash、Read/Write/Edit、Glob、Grep、WebSearch、WebFetch、Task、TodoWrite 等）
- 均自动处理上下文压缩（compaction）
- 均支持会话持久化
- 权限模式（default / acceptEdits / bypassPermissions）完全相同

### 不同之处

| 维度 | Claude Code web Sandbox | Claude Managed Agents |
|---|---|---|
| **定位** | 面向终端用户的产品 | 面向开发者的平台 API |
| **交互方式** | 浏览器 UI，人工实时对话 | 编程接口，代码驱动 |
| **控制粒度** | 用户无法设置轮次/费用上限 | 可精确设置 max_turns / max_budget_usd |
| **多智能体** | 单会话 | 可通过 Task 工具启动子智能体并行 |
| **智能体定制** | 固定配置 | 可自定义 system prompt、工具、MCP servers、skill |
| **环境定制** | 预设环境 | 可指定预装包、网络规则、挂载文件 |
| **适用场景** | 人类直接使用 Claude 完成任务 | 在自己的产品中内嵌 AI 智能体能力 |

### 一句话总结

Claude Code web Sandbox 是 Anthropic 自己用 Managed Agents 技术构建的面向用户的产品；Managed Agents 是把同一套运行时开放出来，让开发者可以构建属于自己的"Claude Code"。

---

## 当前状态

- Beta 阶段，所有 API 账户默认开启访问权限
- 需携带 `managed-agents-2026-04-01` beta header
- Outcomes、Multi-agent coordination、Persistent memory 三项功能处于研究预览阶段，需单独申请
