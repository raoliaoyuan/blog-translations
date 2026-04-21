> **原文**：https://github.com/NousResearch/hermes-agent/security
> **译者**：Claude / 翻译日期：2026-04-21

---

# Hermes Agent 安全策略

本文档概述了 Hermes Agent 项目的安全协议、信任模型和部署加固指南。

## 1. 漏洞报告

Hermes Agent 不设立漏洞赏金计划（bug bounty program）。安全问题应通过 GitHub Security Advisories（GHSA）或发送邮件至 security@nousresearch.com 进行报告，请勿为安全漏洞开 public issue。

### 提交所需信息

- **标题与严重级别**：简明描述及 CVSS 评分/评级
- **受影响组件**：精确的文件路径和行号范围（如 `tools/approval.py:120-145`）
- **环境信息**：`hermes version` 输出、commit SHA、操作系统及 Python 版本
- **复现步骤**：针对 `main` 分支或最新发布版本的逐步概念验证（Proof-of-Concept，PoC）
- **影响说明**：解释哪条信任边界（trust boundary）被突破

## 2. 信任模型

核心假设是：Hermes 是一个供单一受信任运营者使用的个人 Agent。

### 运营者与会话信任

- **单租户（Single Tenant）**：系统保护运营者免受 LLM 行为的危害，而非防范恶意共同租户。多用户隔离须在操作系统/宿主机层面实现。
- **网关安全**：已授权的调用方（Telegram、Discord、Slack 等）享有同等信任级别。会话 key 仅用于路由，不作为授权边界。
- **执行环境**：默认使用 `terminal.backend: local`（直接在宿主机执行）。容器隔离（Docker、Modal、Daytona）需主动开启以启用沙箱。

### 危险命令审批

审批系统（`tools/approval.py`）是核心安全边界。终端命令、文件操作及其他潜在破坏性操作在执行前均需通过显式用户确认。审批模式可通过 `config.yaml` 中的 `approvals.mode` 配置：

- `"on"`（默认）— 提示用户审批危险命令
- `"auto"` — 经过可配置的延迟后自动审批
- `"off"` — 完全禁用审批（应急操作（break-glass）；见第 3 节）

### 输出脱敏

`agent/redact.py` 会在所有显示输出到达终端或网关平台之前，去除其中类似密钥的模式（API key、token、凭证），防止凭证在聊天记录、工具预览和响应文本中意外泄露。脱敏仅作用于显示层——底层数值在 Agent 内部操作中保持完整。

### 技能（Skill）与 MCP 服务器

- **已安装的技能**：高信任级别，等同于宿主机本地代码；技能可读取环境变量并运行任意命令。
- **MCP 服务器**：较低信任级别。MCP 子进程接收经过过滤的环境（`tools/mcp_tool.py` 中的 `_build_safe_env()`）——仅有安全基线变量（`PATH`、`HOME`、`XDG_*`）以及服务器 `env` 配置块中显式声明的变量会被传递，宿主机凭证默认被过滤。此外，通过 `npx`/`uvx` 调用的包在启动前会针对 OSV 恶意软件数据库进行检查。

### 代码执行沙箱

`execute_code` 工具（`tools/code_execution_tool.py`）在子进程中运行 LLM 生成的 Python 脚本，并过滤掉环境中的 API key 和 token，以防止凭证泄露。只有已加载技能显式声明（通过 `env_passthrough`）或用户在 `config.yaml` 中配置（`terminal.env_passthrough`）的环境变量才会被传递。子进程通过 RPC 访问 Hermes 工具，而非直接调用 API。

### 子 Agent

- **禁止递归委托**：子 Agent 的 `delegate_task` 工具处于禁用状态。
- **深度限制**：`MAX_DEPTH = 2`——父 Agent（深度 0）可以启动子 Agent（深度 1），孙代 Agent 会被拒绝。
- **内存隔离**：子 Agent 以 `skip_memory=True` 运行，无法访问父 Agent 的持久化内存提供者。父 Agent 仅接收任务提示和最终响应作为观察结果。

## 3. 不在范围内（非漏洞场景）

以下场景不被视为安全漏洞：

- **提示注入**：除非导致审批系统、工具集限制或容器沙箱被实际绕过。
- **公网暴露**：在没有外部认证或网络防护的情况下将网关部署至公网。
- **受信任状态访问**：需要预先拥有 `~/.hermes/`、`.env` 或 `config.yaml` 写权限的报告（这些属于运营者管控的文件）。
- **默认行为**：`terminal.backend` 设为 `local` 时的宿主机级命令执行——这是有文档记录的默认行为，不属于漏洞。
- **配置权衡**：刻意设置的应急配置，如生产环境中的 `approvals.mode: "off"` 或 `terminal.backend: local`。
- **工具级读取/访问限制**：Agent 通过 `terminal` 工具享有不受限制的 shell 访问权，这是设计如此。如果某个特定工具（如 `read_file`）能访问某资源，而同样的访问可通过 `terminal` 实现，此类报告不构成漏洞。工具级拒绝列表只有在 `terminal` 侧有等效限制时才构成有意义的安全边界（如写操作，其中 `WRITE_DENIED_PATHS` 与危险命令审批系统配合使用）。

## 4. 部署加固与最佳实践

### 文件系统与网络

- **生产沙箱**：对不受信任的工作负载使用容器后端（docker、modal、daytona），而非 `local`。
- **文件权限**：以非 root 用户运行（Docker 镜像使用 UID 10000）；本地安装时使用 `chmod 600 ~/.hermes/.env` 保护凭证。
- **网络暴露**：不在没有 VPN、Tailscale 或防火墙保护的情况下将网关或 API 服务器暴露至公网。所有网关平台适配器（Telegram、Discord、Slack、Matrix、Mattermost 等）默认启用 SSRF（服务端请求伪造，Server-Side Request Forgery）防护，并进行重定向校验。注意：本地 `terminal` 后端不应用 SSRF 过滤，因为它在受信任的运营者环境中运行。

### 技能与供应链

- **技能安装**：安装第三方技能前请审查 Skills Guard 报告（`tools/skills_guard.py`）。审计日志 `~/.hermes/skills/.hub/audit.log` 记录每次安装和移除操作。
- **MCP 安全**：MCP 服务器进程启动前，`npx`/`uvx` 包会自动进行 OSV 恶意软件检查。
- **CI/CD**：GitHub Actions 固定至完整的 commit SHA。`supply-chain-audit.yml` 工作流会阻止包含 `.pth` 文件或可疑的 base64+exec 模式的 PR。

### 凭证存储

- API key 和 token 只存放于 `~/.hermes/.env`，绝不写入 `config.yaml` 或提交至版本控制。
- 凭证池系统（`agent/credential_pool.py`）负责处理 key 轮换和回退。凭证从环境变量解析，不以明文存储在数据库中。

## 5. 披露流程

- **协调披露（Coordinated Disclosure）**：90 天窗口期，或修复发布为止，以先到者为准。
- **沟通渠道**：所有更新通过 GHSA 线程或与 security@nousresearch.com 的邮件往来进行。
- **致谢**：除非报告者要求匿名，否则将在发布说明中致谢。

---

*目前尚无已发布的安全公告。*
