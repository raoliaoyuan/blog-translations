# Codex-A5：利益方当前动作（2025-2026，近 12 个月）

口径：2025-06 至 2026-06；A=已宣布并执行，B=已宣布未执行/建设中，C=媒体报道/推断。重点看 AI Agent/LLM 带来的云出向、跨云、推理容量、海缆、IXP 与监管动作。

## A. 公有云三巨头

**AWS。** 2026-06，AWS 将 EC2 Capacity Blocks for ML 预留 GPU 价格再上调约 20%，此前 2026-01 已涨约 15%；它不是 egress 费，但说明 AI 流量的瓶颈正在从“按 GB 出口”转向“可保证 GPU 容量”，状态 A，URL：[Business Insider](https://www.businessinsider.com/amazon-raises-ai-cloud-prices-memory-chip-costs-soar-2026-6)。2025-12，AWS 与 Google Cloud 发布 AWS Interconnect - multicloud + Cross-Cloud Interconnect 跨云私网互联和开放互操作规格，服务跨云数据湖、RAG 和推理回源，状态 A/B，URL：[ITPro](https://www.itpro.com/cloud/aws-and-google-announce-multicloud-collaboration)、[Times of India](https://timesofindia.indiatimes.com/technology/tech-news/aws-and-google-cloud-launch-private-links-for-faster-multicloud-networking/articleshow/125688218.cms)。未找到：2025-2026 AWS 针对 Bedrock/AI 流量的专项 egress 降价、AI 专线产品或新海缆公告；Direct Connect/PrivateLink 未见与 AI 流量直接绑定的价格动作。

判断：AWS 的公开动作不是把 AI 流量单列计费，而是把稀缺性体现在 GPU 容量预约、跨云私网互联和既有网络产品组合上。对互联网商业体系的含义是，AI Agent 产生的检索、工具调用和多云数据回源会被企业网络化、私有化，公网 egress 反而可能被绕开。

**GCP。** 2025-09，Google Cloud 推出 EU/UK Data Transfer Essentials，对同一组织跨多个云并行处理的数据传输免 Google Cloud outbound transfer fee，是对 EU Data Act 的主动竞争性响应，状态 A，URL：[ITPro](https://www.itpro.com/cloud/cloud-computing/google-cloud-introduces-no-cost-data-transfers-for-uk-eu-businesses)、[TechRadar](https://www.techradar.com/pro/google-slashes-uk-and-eu-cloud-data-transfer-fees-ahead-of-eu-data-act)。2025-12，GCP 与 AWS 的跨云私网互联同上，状态 A/B。2026-05，Google “America-India Connect” 公布三条新海缆路径和四条陆缆/光纤路由，连接美国、印度、澳大利亚、南非、新加坡，并绑定 Visakhapatnam AI hub，状态 B，URL：[TechRadar](https://www.techradar.com/pro/googles-america-india-connect-is-filling-in-the-last-gaps-for-a-truly-global-subsea-cable-network)。Vertex AI 未找到“AI 网络层专项降价”；Ironwood TPU/AI Hypercomputer 属于集群内网络与低时延推理优化，状态 A/B，URL：[Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deploys-new-axion-cpus-and-seventh-gen-ironwood-tpu-training-and-inferencing-pods-beat-nvidia-gb300-and-shape-ai-hypercomputer-model)。

判断：GCP 是三家里最明确把监管、跨云和海缆连起来的一方。其策略不是只降价，而是用 Data Act 合规叙事争夺多云入口，用 Cross-Cloud Interconnect 降低企业跨云搬运摩擦，再用印度和南半球线路补齐 AI 数据流的长途路径。

**Azure。** 2025-09，红海 SEA-ME-WE-4、IMEWE 等海缆中断后，Azure 公告中东路径流量更高时延并绕路，显示云骨干对海缆故障的调度动作，状态 A，URL：[Tom's Hardware](https://www.tomshardware.com/tech-industry/red-sea-cable-cut-takes-azure-routes-down)、[TechRadar](https://www.techradar.com/pro/microsoft-azure-services-see-major-disruption-after-red-sea-cables-cut)。未找到：2025-2026 Azure AI egress 调价、ExpressRoute/Front Door 与 AI 流量绑定改价、OpenAI 网络层特别条款；Microsoft Atlas Submarine Cable 未找到本窗口可确认执行公告。

判断：Azure 在本窗口更像“被事件验证”的网络参与者。红海中断说明跨洲 AI 推理、搜索增强和企业 SaaS 同步都受海缆瓶颈影响，但 Microsoft 没有把这件事包装成 AI 流量专项产品，公开层面仍以全球骨干韧性和路由绕行呈现。

## B. 推理服务商

**OpenAI。** 2025-07，OpenAI 与 Oracle 宣布为 Stargate 追加 4.5GW 美国数据中心容量；2025-09，OpenAI、Oracle、SoftBank 又公布五个美国新站点，使 Stargate 计划容量接近 7GW、三年投资超 4000 亿美元，状态 B，URL：[OpenAI](https://openai.com/index/announcing-the-stargate-project/)、[WIRED](https://www.wired.com/story/openai-oracle-softbank-data-center-stargate-us)。2025-09，媒体披露 OpenAI 与 Oracle 签 3000 亿美元、五年算力合同，状态 C，URL：[Tom's Hardware](https://www.tomshardware.com/tech-industry/openai-signs-contract-to-buy-usd300-billion-worth-of-oracle-computing-power-over-the-next-five-years-company-needs-4-5-gigawatts-of-power-enough-to-power-four-million-homes)。API 层面，Responses API 的 `previous_response_id`、conversation state 与 prompt caching 让多轮 Agent 少传重复上下文，状态 A，URL：[conversation state](https://platform.openai.com/docs/guides/conversation-state)、[prompt caching](https://platform.openai.com/docs/guides/prompt-caching)。

判断：OpenAI 同时做两件事：上游用 Stargate/Oracle 把推理容量从单一 Azure 约束中拆出来，下游用 API 状态引用和缓存减少重复 token 与重复上下文传输。前者是资本密集型“容量护城河”，后者是协议层“流量压缩”。

**Anthropic。** 2025-10，Anthropic 与 Google Cloud 扩大 TPU 合作，目标 2026 年获得最高 100 万个 TPU、超过 1GW compute，状态 B，URL：[TechRadar](https://www.techradar.com/pro/anthropic-signs-multibillion-dollar-google-deal-that-gives-it-access-to-a-million-tpus)。2026-04，媒体称 Anthropic 扩大 Amazon 合作，十年支出超 1000 亿美元、最高 5GW compute，状态 C，URL：[Axios](https://www.axios.com/2026/04/21/anthropic-amazon-compute-wars)。Claude prompt caching 支持自动缓存、显式断点、5 分钟/1 小时 TTL，cache read 为基础输入价 0.1 倍，状态 A，URL：[Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)。未找到公开带宽成本金额。

判断：Anthropic 的公开策略更像“多云容量租赁 + API 缓存降本”，不是自建骨干。它把 AWS、Google 的底层网络能力转化为 Claude 的可用区和容量冗余，同时用 prompt caching 服务长上下文 Agent，降低重复前缀带来的算力和传输成本。

**Google AI / DeepMind。** 2025-06 后，Gemini Flash/Lite 与 Vertex AI 主打低时延、低成本推理；Google 自建 TPU、光交换和 AI Hypercomputer 是其 AI 流量内网化路径，状态 A/B。2025-06，Gemini Robotics On-Device 将部分推理下放到设备端，减少云回传，状态 A，URL：[DeepMind](https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)。

判断：Google AI 的网络动作不总以“网络产品”出现，而是嵌入模型形态：Flash/Lite 控制单位请求成本，端侧模型减少回云，TPU/AI Hypercomputer 把高频推理流量锁在 Google 自建网络和专用加速器内部。

## C. 网络层 / 海缆 / IXP

**海缆。** 2025，Google Blue-Raman 被公开资料标记为运营化，欧洲-印度绕开埃及瓶颈，设计容量约 218Tbps、未来可到 400Tbps，状态 A/B，URL：[Google](https://cloud.google.com/blog/products/infrastructure/announcing-blue-and-raman-subsea-cable-systems)、[资料](https://en.wikipedia.org/wiki/Blue-Raman_cable_system)。SEA-ME-WE 6 预计 2026 RFS，设计 126Tbps，状态 B，URL：[SEA-ME-WE 6](https://en.wikipedia.org/wiki/SEA-ME-WE_6)。2025-09 红海海缆中断使 Azure 等绕路，状态 A。中国参与的 PEACE 等未找到新 AI 流量专项公告。

判断：海缆层的核心不是“AI 专线”命名，而是绕开地缘瓶颈、提高跨洲冗余。AI Agent 把跨区检索、企业数据调用和模型服务调用变成持续流量后，印度洋、红海、地中海和太平洋路径的重要性上升。

**IXP。** 未找到 DE-CIX、AMS-IX、LINX 的 AI 专用对等产品。可确认的是容量继续抬升：DE-CIX Frankfurt 2025-12 峰值约 18.73Tbps，AMS-IX 2026 峰值约 15Tbps，状态 A，URL：[DE-CIX](https://en.wikipedia.org/wiki/DE-CIX)、[AMS-IX](https://en.wikipedia.org/wiki/Amsterdam_Internet_Exchange)。2026-05，Equinix 扩展 Fabric Geo Zones，在网络层按地理边界阻断非合规路径，服务主权云/多云，状态 A/B，URL：[ITPro](https://www.itpro.com/infrastructure/data-centres/equinix-expands-fabric-geo-zones-in-data-sovereignty-drive)。

判断：IXP 没有公开把 AI 流量单独产品化，说明 AI 流量仍混在云、视频、软件更新和企业互联里统计。但 Equinix 的 Geo Zones 代表另一条路线：不是按 AI 分类，而是在网络层控制数据主权和跨境路径。

**ISP/运营商。** 美国/欧洲 ISP 未找到 AI 流量专项对等产品；2025-2026 主要是数据中心接入、波分、专线与公平贡献费游说。欧盟公平贡献费仍未形成硬性网络费，状态 C/未执行。

## D. 中国侧

**三大运营商。** 2025-07 后，媒体称中国拟把东数西算中低利用率数据中心纳入统一算力平台，由移动/电信/联通参与调度，难点是远端时延和异构硬件，状态 C，URL：[Tom's Hardware/Reuters](https://www.tomshardware.com/desktops/servers/china-is-developing-nation-spanning-network-to-sell-surplus-data-center-compute-power-latency-disparate-hardware-are-key-hurdles)。2026-06，媒体称中国拟投约 2 万亿元建设全国 AI 数据中心网格，移动和电信运营大部分设施，目标 2028 年联成单一计算网格，状态 C，URL：[Tom's Hardware/Bloomberg](https://www.tomshardware.com/tech-industry/china-drafts-295-billion-plan-to-build-a-national-ai-data-center-grid-running-on-80-percent-domestic-chips)。未找到跨境 AI 推理流量专门价格产品。

判断：中国侧更强调“算力网络”和“全国调度”，而非云厂商单独的 egress 产品。其难点是西部低成本算力与东部低时延需求之间的矛盾；如果 Agent 类应用需要实时工具调用，远距离调度未必能替代本地推理。

**中国公有云/推理商。** 阿里云、腾讯云、华为云、火山引擎的动作集中在模型 API、推理实例、专属资源池和边缘节点；未找到“AI egress 包月/跨云 AI 流量专线”。DeepSeek、智谱、月之暗面、豆包公开信息更多是模型和价格战，未找到自建跨境骨干或合作 PoP 的可确认公告。

判断：国内推理服务商目前更多通过模型蒸馏、低价 API、私有化部署和云市场接入来消化流量压力。公开信息不足以支持“已自建跨境骨干”结论，跨境调用仍可能依赖云厂商、运营商国际专线或第三方 PoP。

## E. 监管层

**EU。** EU Data Act 于 2025-09-12 一般适用，云切换、数据可携带和出向收费透明化直接推动 GCP 等改价，状态 A，URL：[EUR-Lex](https://data.europa.eu/eli/reg/2023/2854/oj)。公平贡献费 2025-2026 仍停留在咨询/博弈，未落地为网络费。

判断：EU 的影响不是直接规定 AI 流量费，而是削弱云锁定和迁移惩罚。若多云推理成为常态，Data Act 会压低“从某云搬出数据”的制度摩擦，间接改变 hyperscaler 的 egress 定价空间。

**美国。** 2025-07，FCC 提议更新美国海缆许可规则：一边放宽高安全申请以“加速 AI 基础设施”，一边限制中国等 foreign adversary 技术、容量租赁和设备进入美国海缆，状态 B，URL：[Tom's Hardware](https://www.tomshardware.com/tech-industry/cyber-security/the-fcc-wants-to-ban-chinese-tech-from-the-undersea-cables-that-connect-the-u-s-to-the-rest-of-the-world-proposed-new-rules-would-secure-cables-against-foreign-adversaries)、[TechRadar](https://www.techradar.com/pro/security/us-government-wants-to-ban-chinese-technology-in-submarine-cables)。DoJ/FTC 对云 egress pricing 的专项执法未找到。

判断：美国监管的显性动作集中在海缆安全和 AI 基础设施，而不是云出向价格。其政策逻辑是把海缆、数据中心、电力和可信供应链视为 AI 竞争底座。

**中国。** 工信部/发改委/网信办公开方向仍是算力网络、东数西算、国产芯片占比、数据跨境合规；未找到单独针对 AI Agent 流量计费或入口分发的监管文件。信通院表述集中在算网融合和智能算力调度，未见公平贡献费式政策。

## 总观察

过去 12 个月的共同特征是：各方没有普遍推出名为“AI 流量费”的新计费项，而是把压力分散到四层。第一层是容量价格，AWS 的 ML Capacity Blocks 涨价和 OpenAI/Anthropic 的 GW 级算力合同都说明，推理服务商最先争夺的是稳定 GPU/TPU 供给。第二层是跨云私网，AWS-GCP 互联和 GCP Data Transfer Essentials 都在降低企业把数据放在多云之间流动的摩擦。第三层是协议降本，OpenAI 与 Anthropic 的缓存机制把长上下文 Agent 的重复传输和重复预填充压缩掉。第四层是底层路由，Google 海缆、Equinix 主权网络和 FCC 海缆许可说明，AI 竞争已下沉到海缆、IXP、数据中心和监管安全边界。最少公开动作的是 ISP/IXP 的“AI 专用对等”，目前更多仍是通用容量扩张。

因此，Part 9 可把“流量经济学”的结论写成：价格动作少于容量动作，公开产品少于私有互联，网络成本正被重新包装为容量、时延、主权、合规和可靠性成本，并持续向基础设施层沉降演进中。

## F. 矩阵与密度

| 利益方 | 价格调整 | 带宽扩张 | 协议变更 | 容量投资 | 其他 |
|---|---|---|---|---|---|
| AWS | A：ML 容量涨价 | A/B：AWS-GCP 私网 | B：互操作规格 | 未找到 | 成本转向保证容量 |
| GCP | A：EU/UK 出向免费 | B：海缆+CCI | B：互操作规格 | A/B：TPU | Data Act 响应 |
| Azure | 未找到 | A：海缆故障绕路 | 未找到 | 未找到 | 骨干韧性事件 |
| OpenAI | A：缓存降 token | 未找到 | A：Responses/缓存 | B/C：Stargate | 多云算力 |
| Anthropic | A：cache read 0.1x | 未找到 | A：自动缓存/TTL | B/C：Google/AWS | 云伙伴依赖 |
| Google AI | A：Flash/Lite | A/B：AI Hypercomputer | B：端侧推理 | A/B：TPU | 设备端降回云 |
| IXP/Equinix | 未找到 | A：峰值扩张 | A/B：Geo Zones | A/B：互联设施 | 主权网络 |
| 中国侧 | 未找到 | C：算力网格 | 未找到 | C：AI DC 网格 | 国产化 |
| 监管层 | A：EU 切换约束 | B：美国海缆许可 | A/B：互操作/安全 | 间接推动 | 公平贡献费未落地 |

过去 12 个月动作密度排名：1 OpenAI/Stargate；2 Google/GCP；3 Anthropic；4 美国/EU 监管；5 AWS；6 Azure/Microsoft；7 中国侧；8 IXP/ISP。
