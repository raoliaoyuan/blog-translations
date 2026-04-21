> **原文**：https://hermes-agent.nousresearch.com/docs/user-guide/security
> **译者**：Claude / 翻译日期：2026-04-21

---

# 安全

Hermes Agent 采用纵深防御（defense-in-depth）安全模型。本页涵盖所有安全边界——从命令审批、容器隔离，到消息平台的用户授权。

## 概述

安全模型共有七层：

1. **用户授权（User authorization）** — 控制谁可以与 Agent 交互（允许列表（allowlist）、私信配对）
2. **危险命令审批** — 针对破坏性操作引入人工介入（human-in-the-loop）
3. **容器隔离** — 使用 Docker/Singularity/Modal 沙箱并进行强化配置
4. **MCP 凭证过滤** — 对 MCP 子进程进行环境变量隔离
5. **上下文文件扫描** — 检测项目文件中的提示注入（prompt injection）
6. **跨会话隔离** — 各会话之间无法访问彼此的数据或状态；cron 任务的存储路径已针对路径遍历攻击进行了强化
7. **输入净化** — 终端工具后端的工作目录参数会通过允许列表校验，以防止 shell 注入

## 危险命令审批

在执行任何命令之前，Hermes 会将其与一组精选的危险模式进行匹配。若匹配成功，用户必须明确审批。

### 审批模式

审批系统支持三种模式，通过 `~/.hermes/config.yaml` 中的 `approvals.mode` 配置：

```yaml
approvals:
  mode: manual    # manual | smart | off
  timeout: 60     # 等待用户响应的秒数（默认：60）
```

| 模式 | 行为 |
|------|------|
| manual（默认） | 始终提示用户手动审批危险命令 |
| smart | 使用辅助 LLM 评估风险。低风险命令（如 `python -c "print('hello')"`）自动放行；明确危险的命令自动拒绝；不确定的情况升级为手动提示 |
| off | 禁用所有审批检查——等同于使用 `--yolo` 运行，所有命令无提示直接执行 |

> **警告**：将 `approvals.mode` 设为 `off` 会禁用所有安全提示，仅在受信任的环境（CI/CD、容器等）中使用。

### YOLO 模式

YOLO 模式会在当前会话中绕过所有危险命令审批提示，可通过以下三种方式启用：

- **CLI 参数**：使用 `hermes --yolo` 或 `hermes chat --yolo` 启动会话
- **斜杠命令**：在会话中输入 `/yolo` 以切换开关
- **环境变量**：设置 `HERMES_YOLO_MODE=1`

`/yolo` 命令是一个开关——每次使用都会切换模式：

```
> /yolo
  ⚡ YOLO mode ON — all commands auto-approved. Use with caution.

> /yolo
  ⚠ YOLO mode OFF — dangerous commands will require approval.
```

YOLO 模式在 CLI 和网关会话中均可使用。其内部实现是设置 `HERMES_YOLO_MODE` 环境变量，该变量在每次命令执行前都会被检查。

> **危险**：YOLO 模式会在当前会话中禁用所有危险命令安全检查，仅在完全信任所生成命令的场景下使用（例如，在一次性环境中运行经过充分测试的自动化脚本）。

### 审批超时

当出现危险命令提示时，用户有一段可配置的时间来响应。若在超时时间内未收到响应，命令默认被拒绝（fail-closed，即默认失败安全）。

在 `~/.hermes/config.yaml` 中配置超时：

```yaml
approvals:
  timeout: 60  # 秒（默认：60）
```

### 触发审批的模式

以下模式会触发审批提示（定义于 `tools/approval.py`）：

| 模式 | 描述 |
|------|------|
| `rm -r` / `rm --recursive` | 递归删除 |
| `rm ... /` | 删除根路径下的内容 |
| `chmod 777/666` / `o+w` / `a+w` | 全局/其他用户可写权限 |
| `chmod --recursive` 配合不安全权限 | 递归设置全局/其他用户可写（长参数形式） |
| `chown -R root` / `chown --recursive root` | 递归 chown 为 root |
| `mkfs` | 格式化文件系统 |
| `dd if=` | 磁盘复制 |
| `> /dev/sd` | 写入块设备 |
| `DROP TABLE/DATABASE` | SQL DROP |
| `DELETE FROM`（不带 WHERE） | 无条件 SQL DELETE |
| `TRUNCATE TABLE` | SQL TRUNCATE |
| `> /etc/` | 覆写系统配置 |
| `systemctl stop/disable/mask` | 停止/禁用系统服务 |
| `kill -9 -1` | 杀死所有进程 |
| `pkill -9` | 强制杀死进程 |
| Fork 炸弹模式 | Fork bomb |
| `bash -c` / `sh -c` / `zsh -c` / `ksh -c` | 通过 `-c` 参数执行 shell 命令（包括 `-lc` 等组合参数） |
| `python -e` / `perl -e` / `ruby -e` / `node -c` | 通过 `-e`/`-c` 参数执行脚本 |
| `curl ... \| sh` / `wget ... \| sh` | 将远程内容通过管道传给 shell |
| `bash <(curl ...)` / `sh <(wget ...)` | 通过进程替换执行远程脚本 |
| `tee` 写入 `/etc/`、`~/.ssh/`、`~/.hermes/.env` | 通过 tee 覆写敏感文件 |
| `>` / `>>` 写入 `/etc/`、`~/.ssh/`、`~/.hermes/.env` | 通过重定向覆写敏感文件 |
| `xargs rm` | xargs 配合 rm |
| `find -exec rm` / `find -delete` | find 配合破坏性操作 |
| `cp`/`mv`/`install` 到 `/etc/` | 将文件复制/移动至系统配置目录 |
| `sed -i` / `sed --in-place` 作用于 `/etc/` | 原地编辑系统配置 |
| `pkill/killall hermes/gateway` | 防止自我终止 |
| `gateway run` 配合 `&`/`disown`/`nohup`/`setsid` | 防止在服务管理器之外启动网关 |

> **提示**：容器绕过：在 docker、singularity、modal 或 daytona 后端中运行时，危险命令检查会被跳过，因为容器本身就是安全边界。容器内的破坏性命令不会影响宿主机。

### 审批流程（CLI）

在交互式 CLI 中，危险命令会显示内联审批提示：

```
  ⚠️  DANGEROUS COMMAND: recursive delete
      rm -rf /tmp/old-project

      [o]nce  |  [s]ession  |  [a]lways  |  [d]eny

      Choice [o/s/a/D]:
```

四个选项说明：

- **once** — 仅允许本次执行
- **session** — 在本次会话剩余时间内允许该模式
- **always** — 加入永久允许列表（保存至 `config.yaml`）
- **deny**（默认）— 阻止该命令

### 审批流程（网关/消息平台）

在消息平台上，Agent 会将危险命令详情发送至聊天，并等待用户回复：

- 回复 `yes`、`y`、`approve`、`ok` 或 `go` 以审批
- 回复 `no`、`n`、`deny` 或 `cancel` 以拒绝

当运行网关时，`HERMES_EXEC_ASK=1` 环境变量会自动设置。

### 永久允许列表

通过「always」审批的命令会保存到 `~/.hermes/config.yaml`：

```yaml
# 永久允许的危险命令模式
command_allowlist:
  - rm
  - systemctl
```

这些模式在启动时加载，并在所有未来会话中静默放行。

> **提示**：使用 `hermes config edit` 查看或移除永久允许列表中的模式。

## 用户授权（网关）

运行消息网关时，Hermes 通过分层授权系统控制哪些用户可以与机器人交互。

### 授权检查顺序

`_is_user_authorized()` 方法按以下顺序检查：

1. 平台级全量放行标志（如 `DISCORD_ALLOW_ALL_USERS=true`）
2. 私信配对审批列表（通过配对码审批的用户）
3. 平台级允许列表（如 `TELEGRAM_ALLOWED_USERS=12345,67890`）
4. 全局允许列表（`GATEWAY_ALLOWED_USERS=12345,67890`）
5. 全局全量放行（`GATEWAY_ALLOW_ALL_USERS=true`）
6. 默认：拒绝

### 平台允许列表

在 `~/.hermes/.env` 中以逗号分隔的方式设置允许的用户 ID：

```bash
# 平台级允许列表
TELEGRAM_ALLOWED_USERS=123456789,987654321
DISCORD_ALLOWED_USERS=111222333444555666
WHATSAPP_ALLOWED_USERS=15551234567
SLACK_ALLOWED_USERS=U01ABC123

# 跨平台允许列表（对所有平台生效）
GATEWAY_ALLOWED_USERS=123456789

# 平台级全量放行（谨慎使用）
DISCORD_ALLOW_ALL_USERS=true

# 全局全量放行（极度谨慎使用）
GATEWAY_ALLOW_ALL_USERS=true
```

> **警告**：若未配置任何允许列表且未设置 `GATEWAY_ALLOW_ALL_USERS`，所有用户将被拒绝。网关启动时会记录警告：
> ```
> No user allowlists configured. All unauthorized users will be denied.
> Set GATEWAY_ALLOW_ALL_USERS=true in ~/.hermes/.env to allow open access,
> or configure platform allowlists (e.g., TELEGRAM_ALLOWED_USERS=your_id).
> ```

### 私信配对系统

为实现更灵活的授权，Hermes 内置了基于配对码的配对系统（DM Pairing System）。无需预先获取用户 ID，未知用户会收到一次性配对码，由机器人所有者通过 CLI 审批。

工作流程：

1. 未知用户向机器人发送私信
2. 机器人回复一个 8 位配对码
3. 机器人所有者在 CLI 运行 `hermes pairing approve <platform> <code>`
4. 该用户在对应平台上永久获得授权

在 `~/.hermes/config.yaml` 中控制如何处理未授权的私信：

```yaml
unauthorized_dm_behavior: pair

whatsapp:
  unauthorized_dm_behavior: ignore
```

- `pair` 是默认值，未授权私信会收到配对码回复
- `ignore` 则静默丢弃未授权私信
- 平台级配置会覆盖全局默认值，因此可以对 Telegram 保持配对，同时让 WhatsApp 静默

安全特性（基于 OWASP + NIST SP 800-63-4 指南）：

| 特性 | 详情 |
|------|------|
| 码格式 | 8 位字符，取自 32 字符的无歧义字母表（去除 0/O/1/I） |
| 随机性 | 密码学安全（`secrets.choice()`） |
| 配对码有效期 | 1 小时 |
| 频率限制 | 每用户每 10 分钟最多请求 1 次 |
| 待审批上限 | 每平台最多 3 个待审批配对码 |
| 锁定机制 | 连续 5 次审批失败 → 锁定 1 小时 |
| 文件安全 | 所有配对数据文件设置 `chmod 0600` |
| 日志 | 配对码不会记录到 stdout |

配对 CLI 命令：

```bash
# 列出待审批和已审批用户
hermes pairing list

# 审批配对码
hermes pairing approve telegram ABC12DEF

# 撤销用户访问权限
hermes pairing revoke telegram 123456789

# 清除所有待审批配对码
hermes pairing clear-pending
```

存储：配对数据存储于 `~/.hermes/pairing/`，按平台分 JSON 文件：

- `{platform}-pending.json` — 待审批配对请求
- `{platform}-approved.json` — 已审批用户
- `_rate_limits.json` — 频率限制与锁定跟踪

## 容器隔离

使用 docker 终端后端时，Hermes 会对每个容器进行严格的安全强化。

### Docker 安全参数

每个容器均使用以下参数运行（定义于 `tools/environments/docker.py`）：

```python
_SECURITY_ARGS = [
    "--cap-drop", "ALL",                          # 移除所有 Linux capabilities
    "--cap-add", "DAC_OVERRIDE",                  # root 可写入绑定挂载目录
    "--cap-add", "CHOWN",                         # 包管理器需要文件所有权
    "--cap-add", "FOWNER",                        # 包管理器需要文件所有权
    "--security-opt", "no-new-privileges",         # 阻止权限提升
    "--pids-limit", "256",                         # 限制进程数
    "--tmpfs", "/tmp:rw,nosuid,size=512m",         # 限制大小的 /tmp
    "--tmpfs", "/var/tmp:rw,noexec,nosuid,size=256m",  # 禁止执行的 /var/tmp
    "--tmpfs", "/run:rw,noexec,nosuid,size=64m",   # 禁止执行的 /run
]
```

### 资源限制

容器资源可在 `~/.hermes/config.yaml` 中配置：

```yaml
terminal:
  backend: docker
  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"
  docker_forward_env: []  # 仅显式允许列表；为空则将密钥隔离在容器外
  container_cpu: 1        # CPU 核心数
  container_memory: 5120  # MB（默认 5GB）
  container_disk: 51200   # MB（默认 50GB，需要 XFS 上的 overlay2）
  container_persistent: true  # 跨会话持久化文件系统
```

### 文件系统持久化

- **持久模式**（`container_persistent: true`）：将 `/workspace` 和 `/root` 从 `~/.hermes/sandboxes/docker/<task_id>/` 绑定挂载
- **临时模式**（`container_persistent: false`）：工作区使用 tmpfs——清理后所有内容丢失

> **提示**：生产网关部署建议使用 docker、modal 或 daytona 后端，将 Agent 命令与宿主机隔离。这样可完全省去危险命令审批。

> **警告**：若在 `terminal.docker_forward_env` 中添加了变量名，这些变量会被有意注入容器供终端命令使用。这对任务专用凭证（如 `GITHUB_TOKEN`）很有用，但同时意味着容器内运行的代码可以读取并泄露这些凭证。

### 终端后端安全对比

| 后端 | 隔离级别 | 危险命令检查 | 适用场景 |
|------|----------|--------------|----------|
| local | 无——直接在宿主机运行 | ✅ 检查 | 开发环境、受信任用户 |
| ssh | 远程机器 | ✅ 检查 | 在独立服务器上运行 |
| docker | 容器 | ❌ 跳过（容器即边界） | 生产网关 |
| singularity | 容器 | ❌ 跳过 | HPC 环境 |
| modal | 云沙箱 | ❌ 跳过 | 可扩展的云隔离 |
| daytona | 云沙箱 | ❌ 跳过 | 持久云工作区 |

## 环境变量透传

`execute_code` 和 `terminal` 都会从子进程中过滤掉敏感环境变量，防止 LLM 生成的代码泄露凭证。但声明了 `required_environment_variables` 的技能（Skill）确实需要访问这些变量。

### 工作原理

两种机制允许特定变量绕过沙箱过滤：

**1. 技能级透传（自动）**

当技能通过 `skill_view` 或 `/skill` 命令加载，且声明了 `required_environment_variables` 时，环境中实际已设置的变量会自动注册为透传变量。未设置（仍处于 setup-needed 状态）的变量不会注册。

```yaml
# 在技能的 SKILL.md frontmatter 中
required_environment_variables:
  - name: TENOR_API_KEY
    prompt: Tenor API key
    help: Get a key from https://developers.google.com/tenor
```

加载该技能后，`TENOR_API_KEY` 会透传至 `execute_code`、`terminal`（local）及远程后端（Docker、Modal）——无需手动配置。

> **Docker & Modal**：在 v0.5.1 之前，Docker 的 `forward_env` 与技能透传是两套独立系统。现已合并——技能声明的环境变量会自动转发至 Docker 容器和 Modal 沙箱，无需手动添加至 `docker_forward_env`。

**2. 配置级透传（手动）**

对于未被任何技能声明的环境变量，可在 `config.yaml` 的 `terminal.env_passthrough` 中添加：

```yaml
terminal:
  env_passthrough:
    - MY_CUSTOM_KEY
    - ANOTHER_TOKEN
```

### 凭证文件透传（OAuth token 等）

部分技能需要在沙箱中访问文件（而非仅环境变量）——例如，Google Workspace 技能会将 OAuth token 存储为活跃 profile 的 `HERMES_HOME` 下的 `google_token.json`。技能在 frontmatter 中声明这些文件：

```yaml
required_credential_files:
  - path: google_token.json
    description: Google OAuth2 token (created by setup script)
  - path: google_client_secret.json
    description: Google OAuth2 client credentials
```

加载时，Hermes 会检查这些文件是否存在于活跃 profile 的 `HERMES_HOME`，并注册挂载：

- **Docker**：只读绑定挂载（`-v host:container:ro`）
- **Modal**：在沙箱创建时挂载，并在每次命令执行前同步（处理会话中途 OAuth 设置的场景）
- **Local**：无需操作（文件已可访问）

也可在 `config.yaml` 中手动列出凭证文件：

```yaml
terminal:
  credential_files:
    - google_token.json
    - my_custom_oauth_token.json
```

路径相对于 `~/.hermes/`，文件在容器内挂载至 `/root/.hermes/`。

### 各沙箱的过滤行为

| 沙箱 | 默认过滤 | 透传覆盖 |
|------|----------|----------|
| execute_code | 阻止名称中含 KEY、TOKEN、SECRET、PASSWORD、CREDENTIAL、PASSWD、AUTH 的变量；仅允许安全前缀的变量通过 | ✅ 透传变量绕过所有检查 |
| terminal（local） | 阻止 Hermes 基础设施专用变量（provider key、网关 token、工具 API key） | ✅ 透传变量绕过黑名单 |
| terminal（Docker） | 默认不传入任何宿主机环境变量 | ✅ 透传变量 + `docker_forward_env` 通过 `-e` 转发 |
| terminal（Modal） | 默认不传入宿主机环境变量/文件 | ✅ 凭证文件挂载；环境变量通过 sync 透传 |
| MCP | 阻止所有变量，仅保留安全的系统变量 + 显式配置的变量 | ❌ 不受透传影响（请使用 MCP env 配置） |

### 安全注意事项

- 透传仅影响你或你的技能明确声明的变量——任意 LLM 生成代码的默认安全策略不变
- 凭证文件以只读方式挂载至 Docker 容器
- Skills Guard 在安装前会扫描技能内容，检查可疑的环境变量访问模式
- 未设置/不存在的变量永远不会被注册（不存在的东西无法泄露）
- Hermes 基础设施密钥（provider API key、网关 token）不应加入 `env_passthrough`——它们有专属的处理机制

## MCP 凭证处理

MCP（Model Context Protocol）服务器子进程接收经过过滤的环境，以防止意外凭证泄露。

### 安全环境变量

只有以下变量会从宿主机传递给 MCP stdio 子进程：

```
PATH, HOME, USER, LANG, LC_ALL, TERM, SHELL, TMPDIR
```

以及所有 `XDG_*` 变量。其他所有环境变量（API key、token、secret）均被过滤。

在 MCP 服务器 `env` 配置中显式定义的变量会被传递：

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_..."  # 仅此变量被传递
```

### 凭证脱敏

MCP 工具的错误信息在返回给 LLM 之前会经过清洗，以下模式会被替换为 `[REDACTED]`：

- GitHub PAT（`ghp_...`）
- OpenAI 风格的 key（`sk-...`）
- Bearer token
- `token=`、`key=`、`API_KEY=`、`password=`、`secret=` 等参数

## 网站访问策略

你可以限制 Agent 通过 web 和浏览器工具访问哪些网站，以防止 Agent 访问内部服务、管理后台或其他敏感 URL。

```yaml
# 在 ~/.hermes/config.yaml 中
security:
  website_blocklist:
    enabled: true
    domains:
      - "*.internal.company.com"
      - "admin.example.com"
    shared_files:
      - "/etc/hermes/blocked-sites.txt"
```

当请求被封锁的 URL 时，工具会返回错误，说明该域名已被策略封锁。封锁列表在 `web_search`、`web_extract`、`browser_navigate` 及所有支持 URL 的工具中强制执行。

完整详情见配置指南中的「Website Blocklist」章节。

## SSRF 防护

所有支持 URL 的工具（web 搜索、web 提取、视觉、浏览器）在抓取前均会校验 URL，以防止服务端请求伪造（SSRF，Server-Side Request Forgery）攻击。封锁的地址包括：

- 私有网络（RFC 1918）：`10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`
- 回环地址：`127.0.0.0/8`、`::1`
- 链路本地地址：`169.254.0.0/16`（包括 `169.254.169.254` 云元数据端点）
- CGNAT / 共享地址空间（RFC 6598）：`100.64.0.0/10`（Tailscale、WireGuard VPN）
- 云元数据主机名：`metadata.google.internal`、`metadata.goog`
- 保留地址、组播地址及未指定地址

SSRF 防护始终开启，无法禁用。DNS 解析失败视为封锁（fail-closed）。重定向链会在每一跳重新校验，以防止基于重定向的绕过攻击。

## Tirith 预执行安全扫描

Hermes 集成了 tirith，在命令执行前进行内容级扫描。Tirith 能检测单纯模式匹配无法识别的威胁：

- 同形字 URL 欺骗（同形字欺骗，homograph spoofing，即利用国际化域名发动攻击）
- 管道解释器模式（`curl | bash`、`wget | sh`）
- 终端注入攻击

Tirith 首次使用时会从 GitHub Releases 自动安装，并进行 SHA-256 校验和验证（若 `cosign` 可用，还会进行来源验证）。

```yaml
# 在 ~/.hermes/config.yaml 中
security:
  tirith_enabled: true       # 启用/禁用 tirith 扫描（默认：true）
  tirith_path: "tirith"      # tirith 二进制路径（默认：PATH 查找）
  tirith_timeout: 5          # 子进程超时秒数
  tirith_fail_open: true     # tirith 不可用时允许执行（默认：true）
```

`tirith_fail_open` 为 `true`（默认）时，若 tirith 未安装或超时，命令照常执行。在高安全性环境中可设为 `false`，使 tirith 不可用时阻止命令执行。

Tirith 的判定结果与审批流程集成：安全命令直接放行；可疑和被封锁的命令则触发用户审批，并附上完整的 tirith 发现（严重级别、标题、描述、更安全的替代方案）。用户可以审批或拒绝——默认选择为拒绝，以确保无人值守场景的安全。

## 上下文文件注入防护

上下文文件（`AGENTS.md`、`.cursorrules`、`SOUL.md`）在被纳入系统提示前，会进行提示注入扫描。扫描器检查以下内容：

- 指示忽略/无视先前指令的内容
- 包含可疑关键词的隐藏 HTML 注释
- 尝试读取密钥（`.env`、凭证文件、`.netrc`）
- 通过 `curl` 泄露凭证
- 不可见 Unicode 字符（零宽空格、双向覆盖字符）

被封锁的文件会显示警告：

```
[BLOCKED: AGENTS.md contained potential prompt injection (prompt_injection). Content not loaded.]
```

## 生产环境部署最佳实践

### 网关部署检查清单

- **设置明确的允许列表** — 生产环境中绝不使用 `GATEWAY_ALLOW_ALL_USERS=true`
- **使用容器后端** — 在 `config.yaml` 中设置 `terminal.backend: docker`
- **限制资源** — 设置合理的 CPU、内存和磁盘限制
- **安全存储密钥** — 将 API key 保存在 `~/.hermes/.env` 并设置正确的文件权限
- **启用私信配对** — 尽可能使用配对码而非硬编码用户 ID
- **定期审查命令允许列表** — 定期审计 `config.yaml` 中的 `command_allowlist`
- **设置 `MESSAGING_CWD`** — 不要让 Agent 在敏感目录下运行
- **以非 root 用户运行** — 绝不以 root 身份运行网关
- **监控日志** — 检查 `~/.hermes/logs/` 中的未授权访问尝试
- **保持更新** — 定期运行 `hermes update` 以获取安全补丁

### 保护 API Key

```bash
# 设置 .env 文件的正确权限
chmod 600 ~/.hermes/.env

# 为不同服务使用不同的 key
# 绝不将 .env 文件提交至版本控制
```

### 网络隔离

为实现最高安全性，可在独立机器或虚拟机上运行网关：

```yaml
terminal:
  backend: ssh
  ssh_host: "agent-worker.local"
  ssh_user: "hermes"
  ssh_key: "~/.ssh/hermes_agent_key"
```

这样可将网关的消息连接与 Agent 的命令执行隔离开来。
