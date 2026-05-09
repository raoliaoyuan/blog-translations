# 在 Claude Code 时代，垂直领域 Agent 还有机会吗？——一个 SRE Agent 的护城河推演

> 写给和我有同样困惑的人：当通用 Agent 越来越强，我们还要不要做、能不能做出有独立价值的垂直 Agent？

## 一、问题的起点

最近我在重度使用 Claude Code，越用越发现一件事：它已经远远超出了"写代码"的范畴。我用它做：

- 本地电脑性能调优、软件部署
- 云环境安全审计
- 数据统计分析
- 写汇报材料、做洞察分析

它强大到一个程度，让我开始怀疑：**是不是 Claude Code 已经可以做所有 Agent 该做的事？那我们还有必要构建其他 AI Agent 吗？**

这个问题不是我一个人的困惑。Anthropic 自己在博客里也承认这个趋势——他们把 Claude Code 定位为"通用 agent harness"，团队内部用它做研究、运营、法务、财务等非编码任务。换句话说，**通用 CLI Agent + 文件系统 + Bash + MCP** 正在构成一个极强的"原子能力底座"。

但深入思考之后，我得到的结论是：**仍然有必要构建垂直 Agent，但 Claude Code 的崛起重新定义了"垂直 Agent"应该长什么样**。

这篇文章把我的推演过程完整记录下来，希望对有同样思考的人有借鉴。

---

## 二、"能做"和"应该用它做"是两回事

通用性强，不等于在所有场景都是最优解。这是软件工程里的经典权衡：**通用性（generality）vs 适配性（fitness for purpose）**。

Claude Code 的通用性极强，但有四个维度上专用 Agent 仍有不可替代的价值：

### 1. 交付形态与用户群体

Claude Code 假设用户是有 CLI 能力、能读懂 diff、能处理权限提示的开发者。但企业里 80% 的最终用户不是开发者。销售要查 CRM、HR 要筛简历、财务要做对账——他们需要的是嵌入工作流的 Agent，而不是终端。

Anthropic 自己用 Claude API + Agent SDK（而不是 Claude Code）构建消费级 Agent 产品，就是最好的例证。

### 2. 领域深度 vs 通用广度

Anthropic 的工程博客《Building Effective Agents》里有一句话我反复琢磨：

> 最成功的 Agent 实现往往不是复杂的框架，而是针对特定任务做了精心约束的简单系统。

具体例子：

- **Cursor / Windsurf**：在编辑器内做实时补全和小步重构，延迟、UI 集成、上下文窗口策略都为 IDE 场景专门优化。
- **Devin / SWE-agent**：针对长时间自主运行的软件工程任务，有自己的 sandbox、记忆、回滚机制。
- **Perplexity**：搜索 + 引用是核心，UI 和检索管线高度专用。
- **领域 Agent**（医疗诊断、法律审查、芯片设计）：需要专有数据、合规审计、领域评估集——这些不是套个 Claude Code 就能解决。

### 3. 信任边界与权限模型

这一点最关键：**Claude Code 的能力越强，"它能做所有事"反而成了它的限制**。

让一个能 `rm -rf` 的 Agent 去帮 HR 处理简历，从风险管理角度不可接受。专用 Agent 的价值之一是**通过缩小能力边界来获得可部署性**。

### 4. 成本与延迟

Claude Code 每次会话都加载完整的 system prompt、工具定义、CLAUDE.md，对于"查个订单状态"这种轻任务是巨大浪费。专用 Agent 可以用更小的模型、更紧凑的上下文，达到 10-100 倍的成本/延迟优势。

---

## 三、垂直 Agent 价值的分层框架

我尝试用一个分层框架来理解 Agent 生态：

| Layer | 定位 | 例子 | 价值 |
|---|---|---|---|
| **L1 原子能力层** | 通用 coding/general agent | Claude Code、Cursor | 放大个体生产力 |
| **L2 领域 Agent** | 垂直领域深度适配 | 法律、医疗、金融、客服 Agent | 重构某个职能的工作方式 |
| **L3 嵌入式 Agent** | 嵌入既有 SaaS 产品 | Notion AI、Salesforce Agentforce | 让现有工具更智能 |
| **L4 多 Agent 编排** | 复杂协作系统 | Anthropic Research 多 Agent | 完成单 Agent 无法完成的任务 |

Claude Code 强势的是 L1，并且它的 SDK/API 让它能成为 L2-L4 的**构建底座**——但这恰恰说明上层 Agent 仍要被构建。

**一个反直觉的结论**：Claude Code 越强大，对其他 Agent 的需求反而越多，不是越少。原因是当通用 Agent 成本降低、能力增强，构建专用 Agent 的边际成本也大幅下降——就像数据库通用化没有消灭 SaaS，反而让 SaaS 爆发。**通用底座的强大解放了上层创新，而不是吞噬上层创新**。

---

## 四、什么样的 Agent 容易被 Skill 化吃掉？

这是构建垂直 Agent 之前必须先回答的问题。一个 Agent 如果同时满足以下条件，它**高度可能**被一个加载了 Skills/Plugins 的 Claude Code 替代：

1. 核心价值是"知识 + 提示词工程"
2. 目标用户本身是开发者或技术人员
3. 没有专有数据、专有模型、专有集成
4. 交付形态是 CLI 或 chat
5. 任务是"一次性"的而非"持续运行"的

**如果你的 Agent 命中 4 条以上，你大概率会被 Skill 替代。** 这不是悲观，是现实。

---

## 五、构建"不可替代性"的六个维度

要避免被替代，至少要在以下维度建立 2-3 个护城河：

### 维度 1：专有数据与数据飞轮

最强的护城河。如果 Agent 依赖**用户私有数据 + 持续积累的反馈数据**，Skill 无法替代。

例：医疗 Agent 接入医院 EHR + 几十万条标注病例；法律 Agent 接入律所历史案件库。

### 维度 2：非开发者用户群体

Claude Code 的 CLI 形态对 95% 的非技术人员不可用。但仅靠"用户群体不同"会随消费级界面演进而变薄，不够。

### 维度 3：深度工作流嵌入

让"使用 Agent"和"完成工作"是同一件事。Cursor 把 AI 嵌入"写代码"、Granola 嵌入"开会"、Linear 嵌入"管 issue"——用户不会切换工作流去 CLI 处理。

### 维度 4：长期运行状态与记忆

Claude Code 是 session-based 的。需要 7×24 监控、长期记忆、多用户协作、事件驱动响应的 Agent 必须有专门基础设施。

### 维度 5：专有评估集与质量护城河

被严重低估。即使别人拿到了你的 SKILL.md，**也复现不出你的质量**——就像同样的食材，米其林大厨和家庭厨师做出来天差地别。

### 维度 6：合规、安全、责任承担

医疗、金融、法律、政府等领域有 HIPAA、SOC 2、GDPR、行业牌照等要求。**Claude Code 是工具，不承担业务责任**；垂直 Agent 产品要承担——这反而是它的价值。客户付钱不只是买功能，而是买"出了问题有人负责"。

---

## 六、边界划分的"三层切割法"

回到实际问题：**怎么划边界**？

**第一层：Claude Code 做不了什么？（绝对边界）**
- 没有持续运行能力
- 没有专有数据访问
- 没有非 CLI 用户界面
- 没有多用户协作和权限模型
- 没有合规认证和审计日志

→ 这些必须由你的 Agent 提供，否则你就是 Claude Code 的子集。

**第二层：Claude Code 能做但做得不够好的？（差异化区）**
- 特定领域的深度知识和判断
- 特定工作流的 UI/UX 优化
- 特定任务的成本/延迟优化
- 特定团队/角色的协作模式

→ 这是产品打磨的重点。

**第三层：Claude Code 已经做得很好的？（不要重做）**
- 通用代码生成、文件操作、shell 命令、问答写作

→ 直接复用，甚至直接调用 Claude Agent SDK 作为底层引擎。

**关键架构建议**：用 Claude Agent SDK 构建你的 Agent，而不是和 Claude Code 竞争。这就像"基于 Postgres 构建 SaaS"——你不和 Postgres 竞争，你站在 Postgres 之上。

---

## 七、案例推演：SRE Agent 的护城河应该建在哪？

抽象框架讨论到这里就够了。下面用一个具体方向——**SRE Agent**——来落地这套方法论。

### 7.1 为什么 SRE 是个好方向？

SRE 是一个**有真实痛点、有付费意愿、有数据飞轮、且通用 Agent 难以直接覆盖**的领域。理解护城河之前，先认清它的特殊性：

- **数据高维、实时、跨系统**：metrics、logs、traces、events、CMDB、告警、变更——量大、有时序、跨系统，CLI 一次性 grep 解决不了。
- **决策需要拓扑感知**：回答"为什么 checkout 延迟变高"，要知道依赖、上下游、最近发布、数据库分片位置——这是一张**持续维护的图**，不是一次性查出来的。
- **时间敏感且有责任承担**：P0 事故每分钟都在烧钱，重大故障在金融/电商行业每分钟成本可达数万到数十万美元。
- **行动是高风险的**：重启、回滚、failover 错一步就是把小事故变成大事故。Claude Code 的"Y/N 确认"模式凌晨三点战时不实用。

### 7.2 四个护城河维度（按重要性排序）

#### 维度 1：专有运行时数据 + 拓扑知识图谱（最核心）

一个真正能用的 SRE Agent 必须持续摄入和维护：

- **实时遥测数据**：metrics/logs/traces 的索引和向量化
- **服务拓扑图**：从 service mesh、APM、CMDB 持续构建的依赖图
- **变更历史**：所有 deploy、config、infra change 的时间线
- **历史事故库**：过去所有 incident 的 timeline、根因、修复动作

**Claude Code + Skill 为什么做不到？** 它是 session-based 的，每次启动都是"白纸"，没有持续运行的数据摄入管线、跨 session 状态、实时索引、多用户共享视图。**像让一个新员工每天上班都失忆——能干活，但永远成不了 senior SRE。**

类比：Datadog 的护城河不是 dashboard，而是**它已经摄入了你所有的数据**。SRE Agent 同理。

#### 维度 2：闭环执行能力 + 安全边界（最难做但最值钱）

SRE 的最高价值是**自动修复**，不是"告诉我发生了什么"。两个层面：

**(a) 行动深度**：自动 scale、回滚、切换 traffic、重启、触发 runbook、创建 incident、通知 on-call、更新 status page——需要和 K8s、CI/CD、PagerDuty、Slack 的深度集成，处理 idempotency、回滚、审计、限速、并发等工程细节。

**(b) 安全边界精细度**：Claude Code 的权限模型是粗粒度"问还是不问"。SRE 场景需要**多维策略引擎**：

- **环境维度**：dev/staging 自动，prod 必须人审
- **影响范围维度**：<1% 流量自动，>10% 必须 P0 oncall 批准
- **时间维度**：变更冻结期一律拒绝
- **服务维度**：tier-1（支付）所有写操作双人确认
- **动作类型维度**：读取自由、scale up 自动、scale down 限流、删除禁止
- **可逆性维度**：可逆宽松，不可逆严格

这套策略引擎本身就是值钱的产品——它**把"AI 能做什么"和"AI 被允许做什么"解耦**，是企业敢于授权的前提。

业界已有 PagerDuty AIOps、Resolve AI、Cleric 等专做 SRE Agent 的公司，核心差异都不在"AI 多聪明"，而在**"如何让企业敢用"**。

#### 维度 3：事件驱动的持续运行架构

SRE 工作的触发方式是事件驱动：告警、异常检测、部署 webhook、定时任务、用户报障——要求 7×24 在线响应。

完整后端应有：事件接入、任务调度、长期运行 worker、状态持久化、Multi-agent 编排。

Claude Code 是 CLI 工具不是服务器。让它处理 PagerDuty webhook、维护跑了 3 小时的 incident response、协调 5 个并行调查 agent——不是它的设计目标。

这一条对应"L4 多 Agent 编排系统"层级，正好是 SRE 的天然战场。Anthropic 的 multi-agent research system 中提到的并行调查、subagent 分工模式，几乎可以原样应用到 incident investigation。

#### 维度 4：领域评估集 + 事故复盘飞轮（长期质量护城河）

SRE 领域的"质量"非常难衡量：根因对不对要事后才知道、修复有没有副作用可能几天后才暴露、建议好不好依赖具体业务上下文。

构建评估集需要：
- 收集大量真实 incident（数据本身稀缺）
- 标注根因、关键证据、最佳处置路径
- 设计反事实测试
- 持续把新事故加入回归测试集

这是 **3-5 年才能建立的资产**。客户每经历一次事故就贡献一次训练数据；Agent 每帮一次客户就有一次评估反馈。**这个飞轮 Claude Code 没有**，因为它的使用是分散的、私密的、不沉淀的。

### 7.3 看起来像护城河但不是的陷阱

- ❌ "我懂 K8s/Prometheus/Istio 命令"——Skill 五分钟能写
- ❌ "我有更好的 prompt"——模型升级会让优势缩水
- ❌ "我集成了 50 个 MCP server"——集成深度才是护城河，不是数量
- ❌ "我的 UI 更漂亮"——UI 容易抄，除非嵌入工作流关键节点

### 7.4 产品形态建议

综合四个维度，我建议构建的 SRE Agent **不是一个 chat 工具**，而是：

**一个常驻在客户基础设施旁边的 AI SRE 同事**：

- 持续摄入并理解客户系统拓扑和健康状态（维度 1）
- 自动响应告警，发起调查、关联证据、提出 hypothesis（维度 3）
- 在严格策略边界内执行修复，重大决策推给 human-in-the-loop（维度 2）
- 每次事故后自动生成 postmortem，learning 反馈到决策模型（维度 4）
- 通过 Slack/Web/PagerDuty 集成存在于 SRE 已有工作流中

这个产品 Claude Code 做不出来——它需要完整的后端服务、状态系统、安全引擎、事件管线。

---

## 八、构建之前的反向自检清单

不管做什么垂直 Agent，构建之前问自己五个问题：

1. **如果 Anthropic 明天发布一个官方 Skill 完全覆盖我的领域，我还剩下什么？** 如果答案是"什么都不剩"，说明你只在做提示词工程，不是产品。
2. **我的用户为什么愿意为我付费而不是自己写个 SKILL.md？** 答案应该是数据、工作流、合规、品质保证之一，而不是"方便"。
3. **我的 Agent 跑一年后，比刚发布时强多少？** 如果没有数据飞轮，强不了多少，护城河浅。
4. **我的目标用户日常会打开 Claude Code 吗？** 如果会，被替代风险高；如果不会，有用户群体护城河。
5. **我的 Agent 的失败成本由谁承担？** 公司承担（合规、责任、SLA）= 真产品；用户自担 = Claude Code 也可以。

把 SRE Agent 拿这五个问题过一遍，全部站得住——这是个真正可防御的方向。

---

## 九、写在最后

回到开头的问题：**Claude Code 这么强，还要不要做垂直 Agent？**

我的答案是：**要做，但要做得对**。

做得对的核心，是不要和 Claude Code 比"通用能力"，而要在以下维度上构建它做不到的事：

- **它是 session-based 的，你做持续运行**
- **它是单用户的，你做多用户协作**
- **它没有领域数据，你积累专有数据飞轮**
- **它没有合规认证，你承担业务责任**
- **它没有事件驱动后端，你做 7×24 服务**
- **它的安全是粗粒度的，你做精细策略引擎**

最后送一句我自己反复提醒自己的话：

> **不要构建一个 Skill 化的 Claude Code 能替代的 Agent。要构建一个 Skill 化的 Claude Code 跑过来求着集成的 Agent。**

如果你也在思考垂直 Agent 的方向，希望这套推演框架对你有用。

---

## 关键引用与参考

### Anthropic 官方资料

- Anthropic, *Building Effective Agents* — Agent 设计的方法论奠基性文章  
  https://www.anthropic.com/engineering/building-effective-agents

- Anthropic, *How Anthropic teams use Claude Code* — Claude Code 作为通用 agent harness 的官方定位  
  https://www.anthropic.com/news/how-anthropic-teams-use-claude-code

- Anthropic, *How we built our multi-agent research system* — 多 Agent 编排模式，可直接应用于 incident investigation  
  https://www.anthropic.com/engineering/built-multi-agent-research-system

- Anthropic, *Building agents with the Claude Agent SDK* — 用 SDK 构建 Agent 的工程指南  
  https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk

- Anthropic, *Claude Agent SDK Overview* — 官方 Agent SDK 文档  
  https://docs.claude.com/en/api/agent-sdk/overview

### 领域参考

- Google, *Site Reliability Engineering Book* — SRE 领域知识的奠基性著作  
  https://sre.google/sre-book/table-of-contents/

### 业界对标产品（SRE Agent 方向）

- PagerDuty AIOps — https://www.pagerduty.com/platform/aiops/
- Resolve AI — https://resolve.ai
- Cleric — https://cleric.io
- Incident.io — https://incident.io

---

*本文是与 Claude 的一次深度讨论的整理记录，希望对有同样思考的人有借鉴价值。如有不同观点欢迎交流。*
