# 第二部分　国际 BGP 结算与互联底座

> 内部研究报告 · 草稿 v0.1 · 主要源材料：[Codex-A 资料笔记](codex-a-research-notes.md)
>
> 证据强度沿用 [Part 7.1 评级](../07-evidence/07-evidence.md#71-四级证据强度评级体系) 标记。

互联网真实物理形态是约 75,000 个自治域（AS）的 BGP 互联网络。AS 之间的钱与流量怎么走，是任何"AI Agent 流量打到了谁头上"问题的底座。本部分按"路由结算 → 计费工程 → 设施与容量批发 → 历史危机 → 价格史"五个层次拆解，每节后明示其对 AI Agent 流量结构问题的含义。

## 2.1 BGP 结算不是单一市场，而是三层叠加

【L4 推断】把"国际 BGP 结算"理解成一个市场，是简化误读。它是三层叠加：

| 层级 | 决定什么 | 计费方式 | 典型谈判周期 |
|---|---|---|---|
| **路由层** | 流量是否可达 | transit / peering / paid peering | 月度结算、年度合约 |
| **设施层** | 双方能否物理接到一起 | 机柜 / 电力 / cross-connect / IXP port | 一次性 + 月度 |
| **容量层** | 跨洋、跨大陆边际成本 | 海缆 IRU / landing / private interconnect | 5–25 年长锁定 |

对 AI Agent 流量经济学，**真正决定结算冲击点的不是"哪一段流量免费"，而是谁拥有足够的边缘节点、互联点、跨洋容量**——能把新增流量从"按 Mbps 计费的 transit"迁移到"固定成本高但边际成本极低的自有直连/海缆容量"。Google、Meta 已经走完这条路；OpenAI、Anthropic 还高度依赖公有云的网络（AWS、GCP），处于结构性弱势。

## 2.2 互联三种基本形态

【L2】DrPeering 给出权威定义（[DrPeering](https://drpeering.net/white-papers/Internet-Service-Providers-And-Peering.html)）：

- **IP Transit**：一家 ISP 出售到其路由表上**所有目的地**的可达性。计费按 Mbps、95th percentile，按 commit 量阶梯折扣。
- **Internet Peering**：双方相互提供到**彼此客户**的访问。Peering **非传递**——A–B、B–C 都对等不等于 A 经 B 可达 C。
- **Paid Peering**：当流量或价值不均衡时由一方付费维持直连；DrPeering 调研的 28 份 peering policy 中，3 份明确把 paid peering 列为"不满足 settlement-free 条件时的替代品"（[28 Policies](https://drpeering.net/white-papers/Peering-Policies/A-Study-of-28-Peering-Policies.html)）。

【L3】Settlement-Free Peering 的商业本质是 **bill-and-keep / sender-keeps-all**——各自收自己客户的钱，互联本身不结算（[Peering, Wikipedia](https://en.wikipedia.org/wiki/Peering)）。公开材料估计互联网上有正式合同的 peering 占比约 0.07%，其中带结算语义的更只占 0.02%；**绝大多数对等是"握手协议+技术配置"**。

【L2】Tier 1 / Tier 2 / Tier 3 的标准定义（[Tier 1](https://en.wikipedia.org/wiki/Tier_1_network)、[Tier 2](https://en.wikipedia.org/wiki/Tier_2_network)）：

- Tier 1：不买 transit，只靠 settlement-free peering 到达全网
- Tier 2：部分免费 peering + 仍要买 transit / paid peering 到达部分网络
- Tier 3：完全靠买 transit

**重要校正**：网上常见的"PeeringDB 的 Tier 1 列表"实际不存在。PeeringDB 公开的对象是 networks、IXPs、facilities、carriers、campuses，**没有 Tier1/Tier2 原生字段**（[PeeringDB Docs](https://docs.peeringdb.com/)）。任何关于 Tier 1 数量、变化趋势的论断，**只能基于 CAIDA AS Rank 或人工分类二次得出**。

### 2.2.1 Norton 框架与 traffic ratio 的来源

【L2】Bill Norton 的 peering 决策框架核心是先估算 **peerable traffic**：用流量采样 / NetFlow 找 Top 50 目的 AS，估计哪些流量能从付费 transit 迁移到直连对等。DrPeering 记录 2001 年只有约 1/20 的网络系统化做这种分析，2010 年多数 peering 组织已普及。

【L2】28 份 peering policy 样本中，**traffic volume 条款占 20/28（71%）、traffic ratio 条款占 9/28（32%）、interconnect capacity 条款占 19/28（68%）**（[28 Policies](https://drpeering.net/white-papers/Peering-Policies/A-Study-of-28-Peering-Policies.html)）。

**对 AI Agent 流量结构问题的含义**：

- traffic ratio 条款只在 1/3 的政策里被显式写入——意味着即使 AI Agent 让流量 ratio 严重偏离 1:1，**直接因 ratio 违约触发对等关系破裂的比例不会高**。
- 更可能的触发点是 traffic volume 条款（71% 政策里），即"当流量大到一定程度时启动重新议价"。
- **本研究核心论断**（[Part 8.1](../08-conclusion/08-conclusion.md)）：在本研究 L4 推算的 **5–50 Tbps 情景上界**下，AI Agent 流量仍不太可能触发主流对等政策的重新议价（**注**：5–50 Tbps 是本研究自底向上推算的情景上界，不等于已知"目前量级"）；增长曲线陡，但**具体拐点年份不下断言**——按 [Part 7.4 跟踪指标](../07-evidence/07-evidence.md#74-长期跟踪指标清单) 动态判断。

## 2.3 95th percentile 计费的工程细节

【L2】95th percentile burstable billing 的标准定义（[Burstable billing](https://en.wikipedia.org/wiki/Burstable_billing)）：

- 链路每 5 分钟采样一次速率
- 月底排序后**丢弃最高 5%**
- 剩下的最高值即当月计费速率
- 30 天 = 720 小时，5% ≈ **36 小时的突发不计费**

### 2.3.1 三种 in/out 口径

同源（Burstable billing）列出三种主流口径：

| 口径 | 算法 | 对 AI Agent 流量的影响 |
|---|---|---|
| **max(in, out) per interval** | 每 5 分钟取 in 和 out 中较大者，按此序列算 95th | 上下行不对称时，**只计高的那一侧** |
| **separate in/out 95th, 取较大者** | 分别算 in 和 out 的 95th，月底取大 | 与上类似，但容许两侧峰值不同步 |
| **sum(in, out) per interval** | 每 5 分钟取 in+out，按和序列算 95th | **AI Agent 上行 + 持续低下行最吃亏**——两边都计 |

**对 AI Agent 流量结构问题的含义**：

- 大多数 transit 合约采用 max 或 separate in/out 口径，**单方向流量过大不一定显著推高 95th**
- 真正受 AI Agent 流量冲击的是采用 sum 口径的合约——这种口径在 peering 合约里出现得更多
- 公开合同样本以 peering policy 为主，transit MSA 极少公开

### 2.3.2 公开样本（peering policy）

【L2】DrPeering 收录的具体合约样本（[Traffic Volume Clause](https://drpeering.net/white-papers/Peering-Policies/StudyOf28/Traffic-Volume-Peering-Policy-Clause.html)）：

- **InterNAP**：5 Mbps aggregate traffic, 95th percentile **in either direction**
- **TW Telecom**：public peering 要求 Ingress + Egress @ 95th percentile **至少 350 Mbps**；private peering 至少 500 Mbps
- **HopOne**：private peering 要求 20 Mb/s average 或 40 Mb/s 95th sustained over prior 3 months

【L2】Hurricane Electric 是少数公开 IP Transit 起价的服务商——"starting from $200 per month"，端口规格 1GE/10GE/40GE/100GE/400GE，edge capacity 超过 900 Tbps（[HE IP Transit](https://he.net/ip_transit.html)）。**commit tier 单价不公开**。

**仍缺数据**：三种 95th in/out 口径的真实 transit MSA 样本、运营商 commit tier 阶梯折扣表，公开渠道找不到（[Codex-A 笔记 §仍缺数据](codex-a-research-notes.md)）。

## 2.4 互联设施与容量批发

### 2.4.1 设施层成本结构

【L2】DrPeering 把互联设施成本归为 5 项：

- 机柜 / 电力
- Cross-connect（同站点光纤跳线）
- IXP port fee
- 远程手 (remote hands)
- "双方是否已有同站点 presence、能否用 cross-connect / switch fabric 在数小时到数日内建立 peering"是 IXP 选择的关键要点

【L3】**Equinix、Digital Realty 等商业数据中心运营商的 cross-connect 月费多为询价制**，官网未见统一公开价目。
【L2】非营利 IXP 更常公开端口费——TorIX 公开说明按端口速率收小额 port fee、不按流量处罚（[TorIX](https://en.wikipedia.org/wiki/Toronto_Internet_Exchange)）。

**对 AI Agent 流量结构问题的含义**：

- 推理服务商若要绕过公有云的网络中间层，必须在大型 IXP 和数据中心商部署"自有 cage + cross-connect + IXP port"——这是固定成本极高但边际成本极低的策略
- Google、Meta 已经走完这条路（参见 2.4.2 海缆）
- OpenAI、Anthropic 仍高度依赖 Microsoft Azure、AWS、Google Cloud 的网络层

### 2.4.2 跨洋容量层：海缆

【L2】海缆承载约 **99% 的跨洋数据**（[Submarine cable, Wikipedia](https://en.wikipedia.org/wiki/Submarine_communications_cable)）。代表性近年海缆：

| 海缆 | 容量 | 路线 | 投资方 | 状态 |
|---|---|---|---|---|
| **2Africa** | 180 Tbps | 环非洲，45,000 km，46 个 landing，33 国 | Meta 主导 + 多电信运营商 | 主系统按官方公告 2025 Q4 投产，至 2026 年中部分分支段状态需复核（[2Africa](https://www.2africacable.net/)） |
| **MAREA** | 200 Tbps（公开设计值） | 美国弗吉尼亚 → 西班牙毕尔巴鄂 | Microsoft + Meta，Telxius 建设运营 | 2017–2018 投产（[MAREA, Wikipedia](https://en.wikipedia.org/wiki/MAREA)） |

**对比中国运营商国际带宽（[Part 4.5.3](../04-china-structure/04-中国结算结构.md#453-三大运营商上市公司年报)）**：中国移动 2024 年报披露**总国际传输带宽 164 Tbps、330 POP**——已接近一条主要海缆的容量量级。这是中国运营商在 AI 跨境流量时代的独有"网络方+云方"双重身份的物理基础。
| **Blue & Raman** | 未公开 | 欧洲 → 中东 → 印度 | Google + 多方 | 在建（[Google announcement](https://cloud.google.com/blog/products/infrastructure/announcing-the-blue-and-raman-subsea-cable-systems)） |
| **PEACE** | 多 Tbps 量级 | 巴基斯坦 → 法国 / 巴基斯坦 → 南非 | 中国联通参与 | 已投产（[PEACE](https://www.peacecable.net/)） |

【L4 推断】**云 / AI 流量的底座已从"买 transit"扩展为长期锁量海缆容量**。这是 hyperscaler 们用资本与海缆 IRU 把跨洋成本从可变成本变成固定成本的策略。AI Agent 跨境调用的真实成本结构，越来越取决于推理服务商是否能踏入这一层。

**对中国语境的含义**：中国公有云无法独立投资海缆（受牌照与监管约束），只能通过 PEACE 等少数项目参与，或者从运营商采购跨境专线。这构成 [Part 4](../04-china-structure/04-中国结算结构.md#43-公有云与运营商的结算模式) 描述的根本约束。

## 2.5 历史结算危机：5 个对照案例

【L2】每一次"流量不对称"引发的结算危机都不是单一物理事实自动触发监管，而是**"末端 eyeball ISP 不可绕开" + "内容/CDN 侧流量高度集中"**两个条件同时成立时才升级。结果**多为私下商业解决**，公开数据稀缺。

### 2.5.1 Comcast vs BitTorrent（2007–2010）

最接近 AI Agent 上行驱动场景的对照。【L2】

- 2008 年 FCC 裁定 Comcast 阻塞 P2P 不当（[FCC-08-183](https://docs.fcc.gov/public/attachments/FCC-08-183A1.pdf)）
- 2010 年 D.C. Circuit 法院**撤销**该裁定，认为 FCC 未证明 ancillary authority 足以执法（[Comcast v. FCC](https://en.wikipedia.org/wiki/Comcast_Corp._v._FCC)）
- **教训**：上行驱动型流量第一次撞到 ISP 商业模型，监管介入最终被司法撤销，事情靠时间和带宽升级"自然消化"

### 2.5.2 Comcast vs Level 3 / Netflix（2010–2014）

【L2】

- 2010-11-11 Level 3 成为 Netflix 主要 CDN
- Comcast 要求 Level 3 为新增入向流量付费
- 2013-07-16 双方称解决，细节不披露
- 2015 又签长期互联协议
- [Wired 2010](https://www.wired.com/2010/11/comcast-tollbooth/)、[Level 3, Wikipedia](https://en.wikipedia.org/wiki/Level_3_Communications)

### 2.5.3 Cogent vs Verizon / Comcast（2013–2014）

【L2】

- 2013–2014 年 Cogent 到 eyeball networks（Comcast / Verizon）的互联点长期满载
- 纽约高峰吞吐曾一度低于 0.5 Mbps（[Wired](https://www.wired.com/story/jammed)）
- FCC 2014 索取 Netflix、Verizon、Comcast 互联协议（[Time](https://time.com/2871498/fcc-investigates-netflix-verizon-comcast/)）
- 最终私下解决

### 2.5.4 Free vs YouTube（2012–2013）

【L2】

- 法国 ARCEP 2013 关闭对 Free、Google 的 IP routing 调查，定性为高峰拥塞与互联安排问题，**非应用层封锁**（[ARCEP](https://www.arcep.fr/actualites/les-communiques-de-presse/detail/n/interconnexion-ip-1.html)、[GGC, Wikipedia](https://en.wikipedia.org/wiki/Google_Global_Cache)）
- 结果：Google 通过部署 GGC（Google Global Cache）到 ISP 网络内绕开互联点拥塞

### 2.5.5 SK Broadband vs Netflix（2018–2023）

【L2】最具量级参考价值的对照案例。

- SK Broadband 称 Netflix 流量从 **2018-05 的 50 Gbps 增至 2021-09 的 1,200 Gbps**——增长 24 倍
- SK 起诉要求 Netflix 分担网络成本（[SKB, Wikipedia](https://en.wikipedia.org/wiki/SK_Broadband)）
- 2023-09 双方私下合作结束争端，条款未公开（[Reuters 2023-09-18](https://www.reuters.com/technology/netflix-sk-broadband-end-all-disputes-partnership-south-korea-2023-09-18/)）

【L2】Twitch 2023-12-06 宣布 **2024-02-27 退出韩国**，明确称网络成本过高。此前 2022-09 限制画质到 720p、2023-02 关闭 VOD（[Twitch blog](https://blog.twitch.tv/en/2023/12/05/an-update-on-twitch-in-korea/)）。

**对 AI Agent 的含义**：韩国案例是**下行驱动业务**因网络成本被 ISP 倒逼出市场的清晰案例。如果未来出现"上行驱动"版本——比如某国 ISP 要求 OpenAI 为入境 prompt 付费——SK Broadband 案是最近的制度参照。

### 2.5.6 欧盟"公平贡献费"（2023–2024）

【L2】

- BEREC 2017 年 IP Interconnection 报告认定生态可通过 peering / CDN / transit 价格下降自我适应，**未见干预必要**（[BEREC Report](https://www.berec.europa.eu/en/document-categories/berec/reports/berec-report-on-ip-interconnection-practices-in-the-context-of-net-neutrality)）
- 欧盟 2023 继续就 "fair contribution" 咨询（[EC Consultation](https://digital-strategy.ec.europa.eu/en/consultations/future-electronic-communications-sector-and-its-infrastructure)）
- 截至本研究撰写时（2026 中），欧盟仍未引入强制公平贡献费

【L4 推断】AI Agent 流量进入欧盟监管视野的时间窗口与 BEREC 数据更新周期重叠。**如果**未来 BEREC 报告中出现"AI 流量在公开数据中可识别"信号，**则**公平贡献费议题可能首次具备实证基础——但这一可能性目前仅为推断。

## 2.6 TeleGeography IP Transit 价格史

【L2】TeleGeography 的 **Global Internet Geography** 与 **IP Transit Pricing Service** 是付费报告产品（[GIG](https://www2.telegeography.com/global-internet-geography)、[IP Transit Pricing Service](https://www2.telegeography.com/ip-transit-pricing-service)）。

**仍缺数据**：本研究**未能从公开渠道获取最近一年的 median price per Mbps 原始数据点**。Codex-A 明确承认这一数据缺口。

【L3】BEREC 2017 报告明确写到 transit / CDN 价格仍在下降、单位交付成本继续下降。【L4】AI 时代最确定的变化是 **"容量需求和私有互联 / 海缆锁量上移"——而非 transit median 出现上涨拐点**。当前公开价格曲线尚不足以证明 transit median 价格触底反弹。

**对 AI Agent 流量结构问题的含义**：

- 单一价格指标（transit median）可能不再反映真实成本结构变化——hyperscaler 已经把成本转移到长期容量层
- 后续研究应跟踪的指标不是 transit median，而是 IXP 端口费、cross-connect 月费、海缆 IRU 价格，但这些指标的公开程度都更低

## 2.7 本部分小结

- **结算结构**：BGP 互联是路由层 + 设施层 + 容量层三层叠加；AI Agent 流量经济学的真实战场在容量层（hyperscaler 的海缆战略）
- **95th percentile 计费**：三种 in/out 口径（max / 分别算 / sum），其中 sum 口径对 AI Agent 流量影响最大；具体合约采用比例**缺公开数据**（L4，沿用 Part 8 立场"可能具备，本研究没有结论"）
- **历史教训**：每一次结算危机都不是单一物理事实自动触发，而是"末端不可绕开 + 内容方集中"两个条件同时成立。AI Agent **可能**同时具备这两个特征——但是否构成可触发结算冲击点的程度本研究没有结论
- **5 个对照案例**：Comcast/BitTorrent（最接近上行驱动场景）、Comcast/Level3、Cogent/Verizon、Free/YouTube、SKB/Netflix——前 4 例私下解决，SKB/Netflix 引出韩国关于"网络使用费"的法案与政策争议（**注**：原稿"立法"措辞已撤回，韩国相关条款在咨询/争议阶段，未走完立法）
- **价格史数据缺口**：TeleGeography median price 未能挂载，需付费报告

**仍缺数据清单**（移交后续）：

1. PeeringDB 中按 CAIDA AS Rank 二次分类的 Tier 1 / Tier 2 历史趋势
2. Equinix / Digital Realty cross-connect 月费实际公开价目
3. 三种 95th in/out 口径的 transit MSA 真实样本
4. TeleGeography median price per Mbps 最近 5 年数据点
5. AS 级别的 OpenAI / Anthropic / Google AI 推理 ASN 的对等关系实测

---

**下一节衔接**：Part 3 在 Part 2 描述的底座之上，看公有云这一零售层如何把 BGP 结算成本与定价策略转化为客户面的"入向免费 + 出向阶梯"商业模型。
