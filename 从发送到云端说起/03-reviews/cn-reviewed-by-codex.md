# 中国侧 AI 产业四层格局核查稿

**发布日期：** 2026-06-04  
**核查口径：** 以 2026-06-01 前后的公开官网、交易所披露、公司投资者关系页、官方产品文档为准。  
**标注规则：** 本稿把可由官方链接支撑的内容写作“事实”；无法核到官方一手来源、但可由产业结构合理推出的判断，显式标注为“结构性推断”。术语首次出现采用“中文（English）”标注。

## 四层覆盖矩阵

| 主要玩家 | 芯片（Chip） | 云计算（Cloud） | 大语言模型（Large Language Model, LLM） | 智能体/运行时（Agent/Runtime） |
| :--- | :--- | :--- | :--- | :--- |
| 阿里巴巴 | [平头哥含光 800 人工智能推理芯片](https://www.t-head.cn/product/npu) | [阿里云](https://www.aliyun.com/) / [百炼 Model Studio](https://help.aliyun.com/zh/model-studio/what-is-model-studio) | [通义千问 Qwen 系列](https://github.com/QwenLM/Qwen3) | [百炼智能体应用](https://help.aliyun.com/zh/model-studio/single-agent-application) / [Qoder CN（原通义灵码）](https://help.aliyun.com/zh/lingma/) |
| 华为 | [昇腾 Ascend](https://www.hiascend.com/) | [华为云](https://www.huaweicloud.com/) / [ModelArts](https://www.huaweicloud.com/intl/zh-cn/product/modelarts) | [盘古大模型](https://www.huaweicloud.com/product/pangu) | [ModelArts Studio / 盘古 Agent 开发](https://support.huaweicloud.com/productdesc-pangulm/pangulm_01_0001.html) |
| 百度 | [昆仑芯](http://www.kunlunxin.com/) | [百度智能云](https://cloud.baidu.com/) | [ERNIE 4.5 / ERNIE X1](https://ernie.baidu.com/blog/zh/posts/ernie4.5/) | [千帆 AppBuilder](https://cloud.baidu.com/doc/AppBuilder/s/build-rag-workflow-app) / [Comate](https://comate.baidu.com/) |
| 腾讯 | [紫霄 AI 推理芯片（腾讯 2021 可持续社会价值报告披露）](https://static.www.tencent.com/attachments/ssv/2021/TencentSSVReport2021.pdf) | [腾讯云](https://cloud.tencent.com/) | [腾讯混元大模型](https://cloud.tencent.com/product/tclm) | [腾讯云智能体开发平台 ADP](https://adp.cloud.tencent.com/) / [CodeBuddy](https://cloud.tencent.com/product/acc) |
| 字节跳动 | — | [火山引擎](https://www.volcengine.com/) / [火山方舟](https://www.volcengine.com/product/ark) | [豆包大模型（火山方舟承载）](https://www.volcengine.com/docs/82379.?lang=zh) | [Trae](https://www.trae.cn/) / [火山方舟应用与工具调用](https://www.volcengine.com/docs/82379.?lang=zh) |
| DeepSeek | — | — | [DeepSeek API 模型](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) | [DeepSeek Chat](https://chat.deepseek.com/) / [DeepSeek Tool Calls](https://api-docs.deepseek.com/zh-cn/quick_start/pricing) |
| 智谱 AI / Z.ai | — | — | [GLM 系列模型](https://docs.bigmodel.cn/cn/guide/start/introduction) / [Z.ai GLM-5.1 文档](https://docs.z.ai/guides/overview/quick-start) | [智谱开放平台智能体](https://docs.bigmodel.cn/cn/guide/start/introduction) / [智谱清言 ChatGLM](https://chatglm.cn/) |
| 月之暗面 | — | — | [Moonshot AI / Kimi](https://www.moonshot.cn/) | [Kimi](https://kimi.moonshot.cn/) |
| MiniMax | — | — | [MiniMax 多模态模型与产品](https://ir.minimax.io/zh-HK) | [MiniMax Agent](https://ir.minimax.io/zh-HK) |
| 寒武纪 | [思元系列智能芯片](https://www.cambricon.com/) / [688256 上交所披露](https://static.sse.com.cn/stock/disclosure/announcement/c/202506/688256_20250604_5OJ3.pdf) | — | — | — |

## 第一层：芯片

**事实。** 阿里巴巴芯片侧能核到的公开产品是[平头哥含光 800](https://www.t-head.cn/product/npu)，其官方页面把含光 800 定义为数据中心人工智能推理芯片，并给出 12nm、170 亿晶体管、820 TOPS 峰值算力等历史发布口径。它与[阿里云百炼](https://help.aliyun.com/zh/model-studio/what-is-model-studio)和[通义千问 Qwen](https://github.com/QwenLM/Qwen3)的关系，官方口径更多体现为集团内“芯片、云、模型”同属阿里体系，而不是把含光 800 声称为当前 Qwen 训练主力。**结构性推断。** 阿里在云侧更强调模型服务、应用构建和开放模型生态，芯片侧对外产品叙事弱于华为昇腾和寒武纪。

**事实。** 华为芯片层以[昇腾 Ascend](https://www.hiascend.com/)为核心，云侧有[华为云 ModelArts](https://www.huaweicloud.com/intl/zh-cn/product/modelarts)，模型侧有[盘古大模型](https://www.huaweicloud.com/product/pangu)。[盘古大模型产品介绍](https://support.huaweicloud.com/productdesc-pangulm/pangulm_01_0001.html)把盘古服务描述为“模型能力 + 开发平台”的组合，并包含 Agent 开发能力。**结构性推断。** 华为的竞争优势不是单一芯片型号，而是“昇腾 + CANN 软件栈 + ModelArts + 盘古行业模型”的软硬一体供给；它在政企、能源、矿山等行业云场景中更容易形成闭环。

**事实。** 百度芯片层对应[昆仑芯](http://www.kunlunxin.com/)，云侧对应[百度智能云](https://cloud.baidu.com/)，模型侧对应[ERNIE 4.5 / ERNIE X1](https://ernie.baidu.com/blog/zh/posts/ernie4.5/)。[百度 2025 年一季度投资者关系公告](https://ir.baidu.com/news-releases/news-release-details/baidu-announces-first-quarter-2025-results)披露，百度在 2025 年 3 月发布 ERNIE 4.5 和 ERNIE X1，并在 4 月发布 Turbo 版本。**结构性推断。** 百度是中国少数同时具备搜索流量、AI 云、大模型和自研芯片历史积累的玩家，但公开材料没有支持“昆仑芯 M300 已成为 2026 主流训练芯片”这类具体断言。

**事实。** 腾讯在[2021 可持续社会价值报告](https://static.www.tencent.com/attachments/ssv/2021/TencentSSVReport2021.pdf)披露过自研 AI 推理芯片“紫霄”，云侧是[腾讯云](https://cloud.tencent.com/)，模型侧是[腾讯混元大模型](https://cloud.tencent.com/product/tclm)。**结构性推断。** 腾讯芯片层更像内部基础设施和特定场景优化，不宜把它写成对外 AI 芯片平台；腾讯对外竞争重心在混元模型、云服务、微信/企业微信生态和[腾讯云智能体开发平台 ADP](https://adp.cloud.tencent.com/)。

**事实。** 字节跳动对外可核验的是[火山引擎](https://www.volcengine.com/)、[火山方舟](https://www.volcengine.com/product/ark)、[豆包大模型](https://www.volcengine.com/docs/82379.?lang=zh)和[Trae](https://www.trae.cn/)。截至本稿核查，未找到字节官方发布“自研 AI 推理芯片产品”的可访问一手页面。**结构性推断。** 由于豆包、抖音、剪映、广告和推荐系统的推理负载巨大，字节有强烈算力优化动机；但这不能替代官方芯片产品事实。

**事实。** 寒武纪是上交所科创板上市公司，[上交所披露文件](https://static.sse.com.cn/stock/disclosure/announcement/c/202506/688256_20250604_5OJ3.pdf)和[寒武纪官网](https://www.cambricon.com/)可作为公司与产品线入口。**结构性推断。** 寒武纪与华为昇腾、百度昆仑芯、阿里平头哥的竞争关系，主要发生在国产 AI 加速卡、智算集群和大模型推理/训练适配上；它不是云厂商，也没有公开自研 LLM 或 Agent 入口。

## 第二层：云计算

**事实。** [阿里云百炼](https://help.aliyun.com/zh/model-studio/what-is-model-studio)是一站式大模型开发与应用平台，官方文档说明其集成千问及主流第三方模型，提供兼容 OpenAI 的 API、模型调优、部署、评测和可视化应用构建。[百炼智能体应用](https://help.aliyun.com/zh/model-studio/single-agent-application)支持把大模型连接外部工具和知识库。**投资关系。** 阿里参与外部模型公司融资的具体持股比例，本次未找到阿里或被投公司正式披露可核验比例；原稿“月之暗面约 36%、MiniMax 约 13%”不作为事实保留。**竞争关系。** 阿里云与华为云、百度智能云、腾讯云、火山引擎的竞争重点，是模型调用价格、推理稳定性、企业数据接入和智能体开发效率。

**事实。** [华为云盘古大模型服务](https://support.huaweicloud.com/productdesc-pangulm/pangulm_01_0001.html)把“盘古系列大模型”和“ModelArts Studio 大模型开发平台”作为核心组成，官方页面还明确包含数据工程、模型开发、Agent 开发等功能。**投资关系。** 华为云公开叙事以自研软硬一体为主，本稿未采用任何“华为持股某模型创业公司”的未经核实说法。**竞争关系。** 华为云相对阿里云和火山引擎，优势在昇腾适配、行业项目交付和私有化/混合云；短板是面向互联网开发者的开放模型生态声量相对弱。

**事实。** [百度智能云千帆 AppBuilder](https://cloud.baidu.com/doc/AppBuilder/s/build-rag-workflow-app)官方文档将其定义为企业级大模型应用开发管理平台，提供 RAG、Agent、工作流、UI Builder 等工具链。[百度投资者关系公告](https://ir.baidu.com/news-releases/news-release-details/baidu-announces-first-quarter-2025-results)披露百度 AI Cloud 在 2025 年一季度增长，并把 ERNIE 4.5、ERNIE X1 纳入企业用户和开发者的 AI 云能力。**投资关系。** 百度的云与模型主要是自研协同，本稿未发现可核验的“通过外部大模型股权形成生态控制”的官方材料。**竞争关系。** 百度与阿里、腾讯、火山引擎竞争企业 MaaS（Model as a Service，模型即服务）平台，与华为竞争全栈国产化项目。

**事实。** [腾讯云混元大模型](https://cloud.tencent.com/product/tclm)官方页把混元定义为通用与多模态大模型家族，覆盖文本、图像、视频、3D 等模态；[腾讯云智能体开发平台 ADP](https://adp.cloud.tencent.com/)面向企业构建智能体；[CodeBuddy](https://cloud.tencent.com/product/acc)面向研发团队提供 Craft 开发智能体、代码补全、单元测试、智能评审、MCP Server 等能力。**投资关系。** 原稿写腾讯持有智谱、MiniMax 的具体比例，本次未找到腾讯或相关公司官方披露支持，删除比例。**竞争关系。** 腾讯云的差异化在微信、QQ、企业微信、腾讯会议、腾讯文档等入口与 B 端协作场景，而不在对外芯片产品。

**事实。** [火山方舟](https://www.volcengine.com/product/ark)官方页提供模型推理、精调、评测、知识库和 AI 原生应用开发能力；[火山方舟文档](https://www.volcengine.com/docs/82379.?lang=zh)列出模型列表、工具调用、函数调用、云部署 MCP（Model Context Protocol，模型上下文协议）/Remote MCP 等功能。**投资关系。** 未找到字节官方披露“外部模型公司股权投资组合”的正式材料；原稿“基本不参与外部模型投资”也不宜写成绝对事实。**竞争关系。** 火山引擎依托字节内部高并发推荐、广告和内容生产经验，在低延迟推理、多模态生成、企业应用构建上与阿里云、百度智能云、腾讯云正面竞争。

## 第三层：大语言模型

**事实。** [Qwen3 GitHub 仓库](https://github.com/QwenLM/Qwen3)由 QwenLM 组织维护，介绍 Qwen3 系列包含稠密模型与混合专家（Mixture of Experts, MoE）模型，并强调推理、代码、工具调用和多语言能力。[阿里云百炼](https://help.aliyun.com/zh/model-studio/what-is-model-studio)提供千问 Max、Plus、Flash 等模型服务入口。**投资关系。** 阿里对外投资模型公司的精确持股未采用；事实层只保留 Qwen 与阿里云百炼的官方平台关系。**竞争关系。** Qwen 的核心竞争点是开源权重、百炼 API 商业化和阿里云生态；它与 DeepSeek、豆包、ERNIE、GLM、混元在模型效果、价格和开发者心智上竞争。

**事实。** [华为云盘古大模型](https://www.huaweicloud.com/product/pangu)覆盖 NLP、多模态、CV、预测、科学计算和行业场景；[盘古产品介绍](https://support.huaweicloud.com/productdesc-pangulm/pangulm_01_0001.html)把盘古与 ModelArts Studio 组成大模型服务闭环。**投资关系。** 华为模型层体现为自研与云服务交付，不写外部模型股权关系。**竞争关系。** 盘古更偏行业模型和政企交付，和面向公众聊天入口的豆包、Kimi、DeepSeek、智谱清言不完全同场，但在企业大模型项目中与阿里、百度、腾讯、火山引擎竞争。

**事实。** [ERNIE 官方博客](https://ernie.baidu.com/blog/zh/posts/ernie4.5/)发布 ERNIE 4.5 模型家族信息；[百度投资者关系公告](https://ir.baidu.com/news-releases/news-release-details/baidu-announces-first-quarter-2025-results)确认 ERNIE 4.5 与 ERNIE X1 在 2025 年 3 月发布，4 月推出 Turbo 版本。**投资关系。** 百度 LLM 层主要由自研模型和智能云承载。**竞争关系。** 百度的差异化来自搜索、知识增强、AI 云和文小言/文心入口，但 DeepSeek 的低价 API、阿里 Qwen 开源、字节豆包应用流量都压缩了文心的开发者心智空间。

**事实。** [腾讯混元大模型](https://cloud.tencent.com/product/tclm)官方页列出混元家族覆盖文本、图像、视频、3D，并提供企业级服务。[CodeBuddy](https://cloud.tencent.com/product/acc)官方页说明其基于腾讯混元代码模型，并提供 AI 对话、代码补全、Craft 开发智能体等能力。**投资关系。** 腾讯对外模型公司投资的具体比例未采用。**竞争关系。** 混元的竞争更依托腾讯云、微信生态和企业协作场景；模型开放生态声量需要对抗 Qwen、DeepSeek、豆包和 GLM。

**事实。** [火山方舟文档](https://www.volcengine.com/docs/82379.?lang=zh)把豆包及业界主流大模型列为平台模型能力来源，[火山方舟产品页](https://www.volcengine.com/product/ark)把豆包大模型、火山方舟和扣子列为相关能力。**投资关系。** 字节模型层以自研豆包与火山方舟承载为主，未采用任何“700 亿美元资本开支全部投向自研芯片与模型集群”的未经官方证实说法。**竞争关系。** 豆包兼具消费者应用、API 和企业云入口，和 Kimi、智谱清言、DeepSeek Chat 在 C 端心智竞争，也和阿里百炼、百度千帆、腾讯混元在 B 端模型调用竞争。

**事实。** [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)列出 deepseek-v4-flash 与 deepseek-v4-pro，并说明 legacy 名称 deepseek-chat 与 deepseek-reasoner 将分别对应 deepseek-v4-flash 的非思考和思考模式。**投资关系。** DeepSeek 未在官方 API 文档中披露云厂商股权关系。**竞争关系。** DeepSeek 的竞争力来自高性价比 API、推理模型形象和开源/开放生态带来的开发者扩散；它直接推动国内云厂商下调模型调用价格或引入 DeepSeek 兼容能力。

**事实。** [智谱开放平台](https://docs.bigmodel.cn/cn/guide/start/introduction)提供大模型 API、智能体开发、模型精调、推理、评测等能力；[Z.ai 开发文档](https://docs.z.ai/guides/overview/quick-start)列出 GLM-5.1、GLM-5、GLM-4.7、GLM-4.6、GLM-4.5 等语言模型入口；[智谱清言](https://chatglm.cn/)是面向用户的对话入口。**投资关系。** 智谱融资投资方和估值的具体数字，本稿不采纳无官方披露来源的媒体口径。**竞争关系。** GLM 与 Qwen、DeepSeek、豆包、ERNIE、混元竞争基础模型能力；智谱开放平台与百炼、千帆、火山方舟竞争开发者与企业调用。

**事实。** [Moonshot AI](https://www.moonshot.cn/)和[Kimi](https://kimi.moonshot.cn/)是月之暗面的公司与产品入口。**结构性推断。** Kimi 的竞争重点在长上下文、搜索增强和 C 端写作/研究入口；它没有公开芯片和云基础设施产品，需依赖外部云或自建算力资源。**投资关系。** 原稿关于阿里、腾讯在月之暗面的持股比例未采用，因为没有官方披露支持。

**事实。** [MiniMax 投资者关系页](https://ir.minimax.io/zh-HK)说明其自研多模态通用大模型，并列出 MiniMax Agent、海螺 AI、MiniMax Audio、星野等产品。**结构性推断。** MiniMax 与月之暗面、智谱类似，是模型与应用层纯玩家，不拥有公开云基础设施或芯片产品。**投资关系。** 原稿把 MiniMax 链到 minimaxir.com 且写具体股权比例，链接和比例均不保留；本稿只使用 MiniMax 官方投资者关系页。

## 第四层：智能体入口与运行时

**事实。** [百炼智能体应用](https://help.aliyun.com/zh/model-studio/single-agent-application)支持以零代码方式把大模型连接外部工具和知识库，并支持 API 调用和发布；[Qoder CN 系列](https://help.aliyun.com/zh/lingma/)是阿里云文档中承接原通义灵码的 AI 智能体产品系列，覆盖 IDE、插件、CLI 和办公场景。**结构性推断。** 阿里 Agent 战略是“百炼承载企业应用、Qoder/Lingma 承载研发入口”，与云 API 和 Qwen 开源生态互相强化。

**事实。** [盘古大模型产品介绍](https://support.huaweicloud.com/productdesc-pangulm/pangulm_01_0001.html)说明盘古大模型服务包含 ModelArts Studio，并提供 Agent 开发等功能。**结构性推断。** 华为 Agent 更可能从行业流程、数据治理、私有部署切入，而非先做大众聊天应用入口。

**事实。** [千帆 AppBuilder](https://cloud.baidu.com/doc/AppBuilder/s/build-rag-workflow-app)提供 RAG（Retrieval-Augmented Generation，检索增强生成）、Agent、工作流、UI Builder 等应用开发工具链；[Comate](https://comate.baidu.com/)是百度面向编码场景的 AI 辅助工具入口。**结构性推断。** 百度 Agent 的优势在搜索、知识库、企业应用和研发工具；挑战是需要把文心模型能力转化为开发者愿意持续使用的工程体验。

**事实。** [腾讯云 ADP](https://adp.cloud.tencent.com/)是腾讯云智能体开发平台；[CodeBuddy](https://cloud.tencent.com/product/acc)提供 Craft 开发智能体、AI 对话、代码补全、单元测试、智能评审、知识库、工程理解、MCP Server 等能力。**结构性推断。** 腾讯 Agent 的潜在壁垒是微信生态、企业微信、腾讯文档、腾讯会议和腾讯云客户关系，而非单独的模型排行榜。

**事实。** [火山方舟文档](https://www.volcengine.com/docs/82379.?lang=zh)列出工具调用、函数调用、云部署 MCP / Remote MCP、知识库搜索等开发能力；[Trae](https://www.trae.cn/)官方首页提供 TRAE SOLO 和 TRAE IDE 下载入口，并说明 SOLO 围绕真实工作流程升级。**结构性推断。** 字节 Agent 布局的核心是把豆包、火山方舟、扣子和 Trae 分别放在消费者、企业应用、低代码应用和编程入口。

**事实。** [DeepSeek API 文档](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)列出 Tool Calls、上下文缓存和思考模式等能力；[DeepSeek Chat](https://chat.deepseek.com/)是用户入口。**结构性推断。** DeepSeek 不是完整 Agent 平台，但会成为其他 Agent 平台的重要模型后端，尤其在价格敏感和推理任务中。

**事实。** [智谱开放平台](https://docs.bigmodel.cn/cn/guide/start/introduction)列出智能体开发平台、联网搜索、知识库、工具调用等能力；[智谱清言](https://chatglm.cn/)是用户端入口。**结构性推断。** 智谱与 MiniMax、月之暗面的关键竞争，不只在模型分数，也在能否把 Agent 应用、视频/图像生成和企业 API 商业化做成可持续收入。

## 关系网小结

**事实。** 全栈覆盖最完整的玩家是华为、阿里、百度、腾讯：它们均有公开可核验的云、模型和 Agent/开发平台入口，且华为、阿里、百度、腾讯均能找到某种芯片层公开材料。字节跳动具备[火山引擎](https://www.volcengine.com/)、[豆包大模型](https://www.volcengine.com/docs/82379.?lang=zh)和[Trae](https://www.trae.cn/)，但本次未核到官方芯片产品。DeepSeek、智谱、月之暗面、MiniMax偏模型与应用层，寒武纪偏芯片层。

**结构性推断。** 中国侧 AI 产业不是单一“模型公司胜出”的格局，而是四类能力的组合竞争：国产 AI 芯片决定算力安全边界，云平台决定模型调用和企业集成效率，LLM 决定能力上限，Agent 决定用户入口与业务闭环。大厂的优势是多层协同；纯玩家的优势是模型迭代速度、产品聚焦和开发者口碑。

**结构性推断。** 投资关系不应替代业务关系。阿里、腾讯等大厂被大量媒体报道参与月之暗面、MiniMax、智谱等融资，但若没有招股书、年报、公司公告或投资者关系材料披露具体比例，本稿不把“持股百分比”写成事实。更稳妥的写法是：大厂资本、云资源和模型平台可能共同影响创业模型公司的算力获取、API 分发和商业化路径。

## 核查变更记录

1. 删除原稿中 MiniMax 的错误链接 `https://www.minimaxir.com/`。该域名不是 MiniMax 官方投资者关系页；本稿改用[MiniMax 投资者关系页](https://ir.minimax.io/zh-HK)。
2. 删除原稿中寒武纪“2026 年 Q1 财报（模拟）”链接和“净利润突破 10 亿元”写法。本稿只保留[寒武纪官网](https://www.cambricon.com/)和[上交所披露文件](https://static.sse.com.cn/stock/disclosure/announcement/c/202506/688256_20250604_5OJ3.pdf)作为官方入口，不引用无法取得官方原始 PDF 的季度数字。
3. 删除“华为昇腾 910C/D/950PR、2026 Q1 首发自研 HBM、年产能突破 100 万片”等具体断言。核查中未找到华为官方页面支持这些 2026 细节。
4. 删除“壁仞科技 2026 年 1 月港交所上市、昆仑芯次日提交 IPO”的断言。核查中未找到港交所或公司官方文件支持。
5. 删除“字节 2026 年 3 月宣布自研 AI 推理芯片流片、日均 50 万亿 Token、700 亿美元 Capex 全投自研芯片与模型集群”的断言。核查中未找到字节或火山引擎官方披露。
6. 删除“平头哥独立融资上市、PPU 进驻三大运营商智算中心”的断言。核查中未找到阿里或平头哥官方公告支持。
7. 删除“阿里云 2026 年市场份额蝉联第一、Qwen 衍生模型超 18 万个、华为云政企渗透率近 60%”等具体市占率/数量。未找到官方或权威一手来源。
8. 将“Qwen 3.5、ERNIE 5.0、Hunyuan-T1、Seed 2.0、DeepSeek-R2、GLM-5”等原稿版本串改为可核验的官方产品家族或官方文档入口：如[Qwen3](https://github.com/QwenLM/Qwen3)、[ERNIE 4.5 / X1](https://ernie.baidu.com/blog/zh/posts/ernie4.5/)、[腾讯混元](https://cloud.tencent.com/product/tclm)、[火山方舟豆包模型](https://www.volcengine.com/docs/82379.?lang=zh)、[DeepSeek API 模型](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)、[GLM 文档](https://docs.bigmodel.cn/cn/guide/start/introduction)。
9. 删除“豆包 MAU 突破 2.2 亿”“Qwen HumanEval 与 Claude 3.7 持平”等应用月活和评测对比。核查中未找到公司官方一手来源支撑。
10. 删除“阿里持有月之暗面约 36%、MiniMax 约 13%；腾讯持有智谱 2-3%、MiniMax 2.37%”等持股比例。核查中未找到阿里、腾讯、月之暗面、MiniMax、智谱的官方披露支持这些比例。
11. 将“腾讯 CodeBuddy 2026 年 3 月上线 WorkBuddy 桌面端”改为可核验的[腾讯云 CodeBuddy](https://cloud.tencent.com/product/acc)和[腾讯云 ADP](https://adp.cloud.tencent.com/)事实，不保留未核实产品时间线。
12. 删除“2026 春晚独家 AI 技术支持、弹性调度万卡集群”等火山引擎宣传性断言。核查中未找到可引用的官方专项公告。
13. 删除原稿末尾笼统“2026 人工智能产业白皮书”“华为昇腾官方技术路线图（2025-2027）”“腾讯云 AI 战略升级白皮书”等未给出可访问具体文件的参考项。本稿改为逐条内嵌官方链接。
