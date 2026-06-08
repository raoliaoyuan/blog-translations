# AI Agent 部署拓扑演化：第 3 轮回应

本文截至日期：2026-06-04。本轮目标不是重写首轮全文，而是逐条回应合著分析师对 `drafts/codex-r1.md` 的五个质疑，并修订需要收窄的 Thesis。结论先写在前面：我接受“Token 服务位置是主矛盾”的重心调整，也接受“单人/低利用率本地推理不能默认更便宜”的批评；我仍坚持 Agent 位置有独立意义，但它更像控制平面、权限边界和动作位置，而不是主要成本中心。

## 质疑 1：Token 经济学是否结构性利好云，本地只剩隐私/低延迟/离线/合规

**判断：接受主要批评，修正 Thesis 2。**

我把首轮 Thesis 2 写成“本地 Token 会先吃掉高频、低风险、够用子任务”，其中“高频”表述过宽。更准确的版本应是：**本地 Token 先吃掉低风险、低延迟、隐私敏感、可离线、质量够用、且本地硬件已被充分利用的子任务；成本只有在高利用率和质量可替代同时成立时才是优势。**

理由如下。

第一，云端确实有结构性成本优势。大规模推理服务能通过连续批处理、KV cache/prefix cache、请求调度和高利用率摊薄 GPU 成本。vLLM 官方说明其核心是 PagedAttention、continuous batching 和高吞吐服务能力，[vLLM 官方页](https://vllm.ai/)与 NVIDIA vLLM 文档也强调 PagedAttention 可降低 KV cache 浪费、支持更大 batch、提升吞吐，[NVIDIA vLLM overview](https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/overview.html)。NVIDIA NIM 也把 LLM 推理定位为低延迟、高吞吐的优化微服务，可跑在云、数据中心、工作站和边缘，[NVIDIA NIM 官方页](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/)。这些机制对单人本地机器并不天然成立，因为个人负载很难把硬件持续打满。

第二，云厂商有批处理和缓存价格杠杆。OpenAI 官方价格页列出 Batch API 可对输入和输出节省 50%，并列出 cached input 价格；例如 2026-06-04 页面上 GPT-5.4 mini 标准价格是 input $0.75 / 1M、cached input $0.075 / 1M、output $4.50 / 1M，Batch 进一步降到 input $0.375 / 1M、output $2.25 / 1M，[OpenAI API pricing](https://developers.openai.com/api/docs/pricing)。这直接削弱了“高频一定本地更便宜”的说法。

第三，用 DGX Spark 做单人推理的成本不能轻率判优。NVIDIA 官方商城列出的 DGX Spark 价格是 **$4,699**，[NVIDIA Marketplace](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)；官方硬件文档列出 128GB 统一内存、最高 1 PFLOP FP4、240W 电源、GB10 SoC TDP 140W，[DGX Spark hardware guide](https://docs.nvidia.com/dgx/dgx-spark/hardware.html)。即便只按 36 个月折旧，硬件也约 $130/月，另加电费、维护、闲置、模型更新和机会成本。若拿云端 mini 模型的批处理 output $2.25 / 1M tokens 对比，单月仅折旧就相当于约 58M output tokens；加入电费和运维后更高。这个粗算不是性能 benchmark，但足以说明：**单人本地成本优势没有被证明，尤其不能和云端批处理直接竞争。**

因此我收回“高频天然迁向本地”的强说法。本地真正稳定的护城河主要是你列的四项：**隐私、低延迟交互、离线、合规**。成本是第五项，但只在以下条件下成立：负载稳定、硬件利用率高、可接受较小/较旧/开源模型、已有运维能力、或本地硬件本来就为其他任务沉没投入。企业数据中心或边缘中心比个人 PC 更可能满足这些条件。

## 质疑 2：PCC/可验证私有云是否吃掉本地化/私有化隐私论证

**判断：部分接受，并修订 Thesis 4/5。**

我同意 PCC 代表的“可验证私有云”会成为第三条路，不能把强合规需求简单二分为“公有云 API”与“企业自建气隙”。Apple PCC 的关键不是“云端私有化营销”，而是把 stateless computation、端到端加密、软件透明度、远程证明和外部研究者验证组合起来。Apple PCC 安全指南明确把“stateless computation on personal user data”和“verifiable transparency”列为安全目标，[Apple PCC Security Guide](https://security.apple.com/documentation/private-cloud-compute)；Apple 的 PCC 研究博客也强调用户数据对 Apple 不可访问，[Private Cloud Compute: A new frontier for AI privacy in the cloud](https://security.apple.com/com/blog/private-cloud-compute/)。

这会分走一部分“既要隐私又要 frontier 能力”的需求。更广义地看，AWS Nitro Enclaves 可创建隔离执行环境处理敏感数据，[AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/)；Google Confidential VM 提供 memory encryption / encryption-in-use，[Google Confidential VM docs](https://docs.cloud.google.com/compute/docs/about-confidential-vm)；Azure Confidential Computing 官方说明其用硬件证明的 TEE 保护 data in use，[Azure Confidential Computing overview](https://learn.microsoft.com/en-us/azure/confidential-computing/overview)。主权云也在走同一方向：Microsoft Sovereign Cloud 强调数据驻留、运营监督和客户控制加密，[Microsoft Sovereign Public Cloud](https://learn.microsoft.com/en-us/industry/sovereign-cloud/sovereign-public-cloud/overview-sovereign-public-cloud)；AWS European Sovereign Cloud 强调 EU 内数据驻留和运营自治，[AWS European Sovereign Cloud](https://aws.eu/european-sovereign-cloud/)。

但我不认为它会完全吃掉企业私有化和气隙部署，原因有三点。

第一，PCC 目前是 Apple 生态内的 Apple Intelligence 架构，不是通用企业 LLM 托管标准。它证明了方向，不等于所有企业 Agent 负载都已有等价产品。

第二，confidential computing 主要降低“云运营商/宿主机看到 data in use”的风险，但没有自动解决所有问题：控制平面、司法辖区、供应链、模型权重可控性、日志与审计、离线连续性、内网工具访问、监管现场检查仍然存在。

第三，气隙不是只为隐私，也是为运营隔离、国家安全、涉密网络、故障域隔离和供应链主权。NVIDIA NIM 的 LLM 文档提供 air-gap deployment，[NIM air-gap deployment](https://docs.nvidia.com/nim/large-language-models/latest/deployment/air-gap-deployment.html)；Red Hat OpenShift AI 也有 disconnected environment 安装文档，[Red Hat OpenShift AI disconnected environment](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.4/html/installing_and_uninstalling_openshift_ai_self-managed_in_a_disconnected_environment/deploying-openshift-ai-in-a-disconnected-environment_install)。这些不是 PCC 的替代品，而是另一类强隔离需求。

中美会分化。美国和欧洲的受监管企业更可能接受“托管私有云 / confidential AI / sovereign cloud”，因为它保留云端规模、模型更新和运维能力。中国则会更偏向国内专有云、企业私有云、一体机或本地托管，原因是数据出境规则、重要数据治理、信创/国产化、政企采购习惯共同作用。网信办《促进和规范数据跨境流动规定》和《数据出境安全评估办法》仍是中国侧边界条件，[规定原文](https://www.cac.gov.cn/2024-03/22/c_1712776612187994.htm)、[评估办法](https://www.cac.gov.cn/2022-07/07/c_1658811536396503.htm)。修订后的 Thesis 4 应加入：**强合规需求会分流到三类方案：自建/气隙、托管私有云/主权云、可验证 confidential cloud；不同国家和行业的比例不同。**

## 质疑 3：2025“一体机元年”是结构性需求还是 DeepSeek + 信创采购脉冲

**判断：部分接受，且对首轮中国一体机判断降温。**

我同意：2025 年的一体机热潮里有明显的 DeepSeek 出圈和信创/国产化采购脉冲。首轮把“供给侧成熟”和“采购品类形成”写得偏积极，但没有证明可持续复购/扩容。

支持结构性需求的证据主要是“使用门槛和合规场景”而不是“普遍经济性”。中国信通院《大模型一体机应用研究报告（2025 年）》认为，一体机通过软硬一体封装模型加载、推理加速、知识集成和接口调度，降低使用门槛、缩短部署到见效周期；报告还指出，推理一体机是当前落地主导形态，政务、金融、医疗、制造等行业在数据安全、私有化部署、低延迟和行业知识适配上有明确选型需求，[中国信通院报告 PDF](https://www.caict.ac.cn/kxyj/qwfb/ztbg/202510/P020251031405764520571.pdf)。政府采购网也能看到真实采购项目，例如电子科技大学“AI 大模型训练与推理一体机等”中标金额 618 万元，[中国政府采购网](https://www.ccgp.gov.cn/cggg/zygg/zbgg/202504/t20250411_24429839.htm)；中国科学院软件研究所 2026 年“大模型服务器采购项目”中标金额 410 万元，[中国政府采购网](https://www.ccgp.gov.cn/cggg/zygg/zbgg/202603/t20260306_26237417.htm)。医疗侧也有联想为爱尔眼科本地部署 DeepSeek 的官方案例，[联想案例](https://brand.lenovo.com.cn/brand/ppn03261.html?brandType=&innerKey=&key=%E8%81%94%E6%83%B3&page=1&source=fromwww&type=brand&years=)。

但反证也很强。中国信通院同一报告明确提醒：本地化部署提高初始采购成本和后期运维成本，包括硬件购置、机房改造、电力供应和专业运维团队；在超大规模训练和海量高并发服务中存在瓶颈，更适用于数据隐私要求极高、业务规模相对稳定、且具备资金与技术支持能力的行业用户。另据中国电信天翼智库在 C114 的跟踪文章，2025 年一体机舆情热度从高点回落，截至 2025 年 9 月全国大模型一体机合计中标金额仅 2752 万元，按时序预估全年 3669 万元，远低于年初乐观预测，[C114/天翼智库](https://www.c114.com.cn/news/117/a1300068.html)。这说明“厂商供给和概念热”不等于“客户持续复购”。

所以我的修订判断是：**2025 的通用大模型一体机热潮包含明显一次性脉冲；可持续部分不是“买一台盒子跑 DeepSeek”，而是行业化、可运维、可扩容的私有 AI 平台。**中小企业若没有强合规、固定高并发、内网数据闭环或本地低延迟要求，真实经济性通常不如公有云 API/MaaS/托管私有云。运维复杂度会让相当一部分客户回流到公有云或托管方案。

## 质疑 4：能力鸿沟持续拉大，“本地够用”是否长期追不上

**判断：部分接受。分流边界不是稳定边界，而是动态边界。**

我同意 frontier 能力还在快速提高，本地“够用”的边界会被不断重新定义。Stanford HAI 2026 AI Index 写到，frontier models 在 Humanity's Last Exam 上一年提升 30 个百分点；同时截至 2026 年 3 月，最强闭源模型领先最强开源模型 3.3%，高于 2024 年 8 月的 0.5%；Agent 在结构化 benchmark 上仍约三分之一失败，[Stanford AI Index 2026 Technical Performance](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance)。Epoch AI 的模型数据库持续跟踪训练 compute、参数、训练成本等，并把 frontier model 定义为发布时训练 compute 处在前 10 的模型，[Epoch AI Models](https://epoch.ai/data/ai-models)。这些数据都支持“前沿线仍在移动”。

但这不是单向“向云回摆”。更准确的动态是两条前沿同时移动：

1. **能力前沿向云/大集群移动。**复杂代码、长上下文法律/医疗、深度研究、多模态推理、高可靠 Agent、需要最新 benchmark 能力的任务，会继续向公有云或大型私有云 Token 服务集中。

2. **效率前沿向端侧/边缘扩散。**已经过时一代的 frontier 能力会通过蒸馏、量化、小模型、MoE、推理引擎优化扩散到本地。NVIDIA DGX Spark 官方称单机可测试和推理最高 200B 参数模型，[DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)；Apple 公开了约 3B 参数端侧模型和更大的服务器模型分工，[Apple Foundation Models](https://machinelearning.apple.com/research/introducing-apple-foundation-models)；DeepSeek-R1 提供 1.5B 到 70B 的蒸馏模型，[DeepSeek-R1 GitHub](https://github.com/deepseek-ai/DeepSeek-R1)；Qwen3 覆盖 0.6B 到 235B，[Qwen3 blog](https://qwenlm.github.io/blog/qwen3/)。

因此边界会“分层摆动”：最难任务向云和大型私有云回摆；低风险、短上下文、私密、低延迟、离线、工具参数化、RAG 前处理、草稿和过滤任务向本地扩散。我的修订 Thesis 2 是：**本地 Token 的份额会在请求数量上增长，但在最高价值/最高难度 tokens 上不一定增长；它更像 Agent 系统的第一跳、过滤器和动作闭环，而不是 frontier model 替代品。**

## 质疑 5：真正的问题是“贵的 Token 放哪”，Agent 位置应跟随数据和工具

**判断：接受框架重心调整，但保留 Agent 位置的独立决定性。**

我同意把决策顺序从“六个格子并列”改为：

1. **先定 Token 服务位置。**核心变量是模型能力、单位 token 成本、合规/数据驻留、可验证隐私、利用率、弹性和供应链。
2. **再定 Agent 执行位置。**核心变量是数据与工具在哪里、动作权限在哪里、审计与密钥在哪里、是否需要低延迟/离线/always-on。

OpenAI Agents SDK 把 agent 定义为带 instructions、tools、handoffs、guardrails 和 structured outputs 的 LLM 配置，[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/agents/)；LangChain 文档也把 agents 描述为把语言模型和工具结合起来、决定使用哪些工具并迭代完成任务的系统，[LangChain agents](https://docs.langchain.com/oss/python/langchain/agents)。这说明 Agent 编排层本身通常不是主要算力成本中心，真正贵的是反复调用模型生成/推理 tokens。

但 Agent 位置仍有独立决定性，尤其在以下场景：

- **权限与动作边界。**能否操作本地文件、IDE、浏览器、数据库、内网系统、OT 设备，不取决于 Token 在哪，而取决于 Agent runtime 在哪、拥有什么凭据和执行沙箱。
- **数据引力与工具延迟。**大量业务数据、日志、代码仓库、设计文件、医疗/工控系统在内网或设备侧，Agent 留在数据旁边可以减少数据搬运和权限暴露。
- **审计和安全责任。**企业通常需要记录谁授权、Agent 调了什么工具、读写了什么数据、失败后如何回滚。这是控制平面问题，不只是模型推理问题。
- **离线和 always-on。**云端 Agent 适合长任务和并行，边缘 Agent 适合门店/工厂/医院科室的连续运行，本地 Agent 适合桌面动作闭环。

因此六格框架仍有用，但它应降级为“部署诊断矩阵”，不应被读成六类同等重要的市场。新框架应是：**Token 是成本与能力中心，Agent 是控制平面与动作边界；两者解耦，但 Token 位置优先决策。**

## 修订后的 Thesis

**Thesis 1（保留但重写）：Agent 与 Token 解耦仍是核心前提；但决策顺序应先定 Token 服务位置，再让 Agent 位置跟随数据、工具、权限和动作延迟。**

**Thesis 2（明显修正）：本地 Token 不会因“高频”天然胜出。它会先承担低风险、低延迟、隐私敏感、离线、质量够用且本地硬件利用率足够的子任务；单人本地推理默认不是成本赢家。**

**Thesis 3（保留）：边缘中心 Token 仍是家庭、门店、工厂、医院、园区的中间态，但成立条件是多设备共享、局域网低延迟、数据不出场域和可运维。**

**Thesis 4（修正）：强合规行业不会只走企业自建私有云，还会分流到可验证私有云、confidential cloud、托管私有云和主权云。气隙/自建仍存在，但不是唯一答案。HPE 链接修正为 [NVIDIA AI Computing by HPE](https://www.hpe.com/us/en/solutions/artificial-intelligence/nvidia-collaboration.html)，该页继续覆盖 HPE 与 NVIDIA 的 AI factory、Private Cloud AI 和 Sovereign AI factory。**

**Thesis 5（降温）：中国市场的本地化部署拉力仍强于美国，但 2025 一体机热潮包含 DeepSeek + 信创采购脉冲。可持续需求会集中在政务、金融、医疗、制造、能源等强合规/强数据闭环行业，以及能提供行业应用、运维和扩容路径的厂商；通用一体机不应被视为普遍经济性成立。**

## 我仍坚持

- Agent 执行位置与 Token 服务位置必须解耦分析。
- 未来不会收敛到单一拓扑，而是按能力、成本、合规、数据和动作边界分流。
- 本地/边缘 Token 会增长，但主要增长在第一跳、前处理、过滤、低延迟动作闭环和隐私敏感任务。
- 中国市场相对美国会有更强的私有化、本地化、国产化拉力。
- 企业买的不是“模型”本身，而是模型服务、Agent runtime、权限、审计、RAG、数据治理和运维的组合。

## 我已修正

- 不再把“高频”本身视为本地成本优势；高频也可能正是云端批处理最有优势的区间。
- 不再把强合规场景默认判给“企业自建私有云/气隙”；新增可验证私有云、confidential cloud、托管私有云、主权云作为第三条路。
- 不再把 2025 一体机热潮直接等同于长期可持续需求；目前复购/扩容证据不足，通用一体机可能是采购脉冲。
- 不再把“小模型够用”描述成稳定边界；边界会随 frontier 能力提高而动态移动。
- 六格框架降级为诊断矩阵；文章主线改为“先定 Token 放哪，再定 Agent 跑哪”。
