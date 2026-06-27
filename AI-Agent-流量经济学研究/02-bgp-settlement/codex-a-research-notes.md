# Part 2 资料笔记：国际 BGP 结算与互联底座

> 标注口径：【公开发表数据】可直接挂源；【行业共识】多源一致但非官方统计；【推断】由公开材料外推。未找到原始价目/合同的，不补数。

## 可挂载结论摘要

【推断】BGP 结算不是单一“谁向谁付费”的线性市场，而是三层叠加：路由层用 transit/peering 决定可达性，设施层用机柜、电力、cross-connect、IXP port 决定入场成本，长期容量层用海缆/landing/IRU/private interconnect 锁定边际成本。对 AI Agent 流量经济学而言，关键不是“流量是否免费”，而是谁拥有足够多的边缘节点、互联点和跨洋容量，能把新增流量从按 Mbps 计费的 transit 迁移到固定成本更高但边际成本更低的直连或自有批发容量。【行业共识】历史争议显示，流量不对称本身并不自动产生监管结论；Comcast/Level 3、Cogent/Verizon、Free/YouTube、SKB/Netflix 都是在“末端 eyeball 网络不可绕开”和“内容/CDN 侧流量高度集中”之间谈判，结果多为私下商业解决，公开数据反而稀缺。【公开发表数据】BEREC 的基线判断仍是 IP interconnection 生态能靠 peering、CDN 与 transit 降价自我适应，因此若报告讨论“AI 是否带来公平贡献费拐点”，需要把它写成待验证假设，而不是既成事实（[BEREC](https://www.berec.europa.eu/en/document-categories/berec/reports/berec-report-on-ip-interconnection-practices-in-the-context-of-net-neutrality)）。

## 2A 互联三种基本形态

【公开发表数据】DrPeering 定义 Internet Transit 为“一个 ISP 出售到其路由表全部目的地的可达性”，通常按 Mbps 和 95th percentile 计费，并按 commit 量给折扣；Internet Peering 则是“公司相互提供到彼此客户的访问”，且 peering 非传递：A-B、B-C 互联不等于 A 可经 B 到 C（[DrPeering](https://drpeering.net/white-papers/Internet-Service-Providers-And-Peering.html)）。【行业共识】Settlement-Free Peering 是 bill-and-keep/sender-keeps-all；公开材料称 peering 中正式合同约 0.07%，带结算语义的“peering”约 0.02%（[Peering](https://en.wikipedia.org/wiki/Peering)）。Paid Peering 是当流量/价值不均衡时由一方向另一方付费维持直连；DrPeering 28 份 peering policy 样本中 3/28 提到 paid peering 作为不满足免费互联条件的替代产品（[28 Policies](https://drpeering.net/white-papers/Peering-Policies/A-Study-of-28-Peering-Policies.html)）。

【公开发表数据】Tier 1 常规定义是“不买 IP transit、只靠 settlement-free peering 到达全网”；Tier 2 是“部分免费 peering，但仍买 transit/paid peering 到达部分互联网”（[Tier 1](https://en.wikipedia.org/wiki/Tier_1_network)，[Tier 2](https://en.wikipedia.org/wiki/Tier_2_network)）。PeeringDB 公开 API 和历史 dump，但对象是 networks、IXPs、facilities、carriers、campuses，并无 Tier1/Tier2 字段；文档只说明可用 `/api/net` 列网络，历史 MySQL dump 覆盖 2010-07-29 至 2016-03-14（[PeeringDB Docs](https://docs.peeringdb.com/)）。因此“PeeringDB Tier1/Tier2 数量与趋势”不是原生公开统计，只能二次分类。

【公开发表数据】Norton 框架的核心是先算 peerable traffic：用流量采样/NetFlow 找 Top 50 目的 AS，估计能从付费 transit 迁移到直连的流量；DrPeering 记录 2001 年约仅 1/20 做系统流量分析，2010 年多数 peering 组织已做分析（[DrPeering](https://drpeering.net/white-papers/Internet-Service-Providers-And-Peering.html)）。28 份 policy 中，traffic volume 条款 20/28，traffic ratio 条款 9/28，interconnect capacity 条款 19/28（[28 Policies](https://drpeering.net/white-papers/Peering-Policies/A-Study-of-28-Peering-Policies.html)）。

## 2B 95th percentile 计费工程细节

【公开发表数据】95th 算法通常每 5 分钟采样，月底排序，丢弃最高 5%，剩下最高值为当月计费速率；30 天 720 小时，5% 约等于 36 小时突发不计入（[Burstable billing](https://en.wikipedia.org/wiki/Burstable_billing)）。同源列出三种 in/out 口径：逐 interval 取 `max(in,out)`；分别算 inbound/outbound 的 95th 后取较大值；逐 interval 取 `sum(in,out)`（[Burstable billing](https://en.wikipedia.org/wiki/Burstable_billing)）。

【公开发表数据】公开合同样本多见于 peering policy 而非 transit MSA：InterNAP 写“5 Mbps aggregate traffic, 95th percentile in either direction”；TW Telecom 写 public peering “Ingress + Egress @ 95th percentile” 至少 350 Mbps、private 至少 500 Mbps；HopOne 写 private peering 要 20 Mb/s average 或 40 Mb/s 95th sustained over prior 3 months（[Traffic Volume Clause](https://drpeering.net/white-papers/Peering-Policies/StudyOf28/Traffic-Volume-Peering-Policy-Clause.html)）。【公开发表数据】Hurricane Electric 仅公开 IP Transit “starting from $200 per month”、端口到 400GE/100GE/40GE/10GE/1GE、edge capacity 超过 900 Tbps，但无 commit tier 单价（[HE IP Transit](https://he.net/ip_transit.html)）。

## 2C 互联设施与容量批发

【公开发表数据】设施成本包括机柜、电力、cross-connect、IXP port、远程手；DrPeering 把“双方是否已有同站点 presence、能否用 cross-connect/switch fabric 数小时到数日建立 peering”列为 IXP 选择要点（[DrPeering](https://drpeering.net/white-papers/Internet-Service-Providers-And-Peering.html)）。Equinix/Digital Realty 官网未见公开 cross-connect 月费价目，多数为询价；IXP 侧更常公开端口费，TorIX 公开说明其非营利、按端口速率收小额 port fee、不按流量处罚（[TorIX](https://en.wikipedia.org/wiki/Toronto_Internet_Exchange)）。

【公开发表数据】TeleGeography 的 Submarine Cable Map 是海缆项目索引入口（[Submarine Cable Map](https://www.submarinecablemap.com/)）。现代海缆承载约 99% 跨洋数据（[Submarine cable](https://en.wikipedia.org/wiki/Submarine_communications_cable)）。2Africa 设计容量 180 Tbps、约 45,000 km、46 个 landing stations/33 国，预计 2025 Q4 投产（[2Africa](https://www.2africacable.net/)，[summary](https://en.wikipedia.org/wiki/2Africa)）；MAREA 由 Microsoft/Facebook 出资、Telxius 建设运营，2019 年公开设计容量 200 Tbps（[MAREA](https://en.wikipedia.org/wiki/MAREA)）。Google 的 Blue-Raman 连接欧洲、中东、印度（[Google](https://cloud.google.com/blog/products/infrastructure/announcing-the-blue-and-raman-subsea-cable-systems)）；中国联通参与 PEACE cable（[PEACE](https://www.peacecable.net/)）。【推断】云/AI 流量的底座已从“买 transit”扩展为海缆、landing、metro fiber、IXP/private interconnect 的长期锁量。

## 2D 历史案例

【公开发表数据】Comcast/BitTorrent：FCC 2008 年 FCC-08-183 要求 Comcast 停止特定 P2P 干扰；D.C. Circuit 2010 年撤销，认为 FCC 未证明 ancillary authority 足以执法（[FCC PDF](https://docs.fcc.gov/public/attachments/FCC-08-183A1.pdf)，[case](https://en.wikipedia.org/wiki/Comcast_Corp._v._FCC)）。Level 3/Comcast/Netflix：Level 3 2010-11-11 成为 Netflix 主要 CDN 后，Comcast 要求为新增入向流量付费；双方 2013-07-16 称解决但细节不披露，2015 又签长期互联协议（[Level 3](https://en.wikipedia.org/wiki/Level_3_Communications)，[Wired](https://www.wired.com/2010/11/comcast-tollbooth/)）。Cogent/Verizon：2013-2014 年 Cogent 到 Comcast/Verizon 等 eyeball networks 的互联点被报道长期满载，纽约高峰吞吐一度低于 0.5 Mbps；FCC 2014 年索取 Netflix、Verizon、Comcast 互联协议调查（[Wired](https://www.wired.com/story/jammed)，[Time](https://time.com/2871498/fcc-investigates-netflix-verizon-comcast/)）。

【公开发表数据】Free/YouTube：ARCEP 2013 年关闭涉及 Free/Google 等的 IP routing 调查，指向高峰拥塞与互联安排，而非单纯应用封锁（[GGC](https://en.wikipedia.org/wiki/Google_Global_Cache)，[ARCEP](https://www.arcep.fr/actualites/les-communiques-de-presse/detail/n/interconnexion-ip-1.html)）。SK Broadband/Netflix：SK 称 Netflix 流量从 2018-05 的 50 Gbps 增至 2021-09 的 1,200 Gbps，增长 24 倍，并起诉要求分担网络成本；2023 年双方以合作结束争端，条款未公开（[SKB](https://en.wikipedia.org/wiki/SK_Broadband)，[Reuters](https://www.reuters.com/technology/netflix-sk-broadband-end-all-disputes-partnership-south-korea-2023-09-18/)）。Twitch 2023-12-06 宣布 2024-02-27 退出韩国，称网络成本过高；此前 2022-09 限制到 720p、2023-02 关 VOD（[Twitch](https://blog.twitch.tv/en/2023/12/05/an-update-on-twitch-in-korea/)）。BEREC 2017 报告称生态可通过 peering/CDN/transit 价格下降适应流量增长，未见干预必要（[BEREC](https://www.berec.europa.eu/en/document-categories/berec/reports/berec-report-on-ip-interconnection-practices-in-the-context-of-net-neutrality)）；欧盟 2023 继续就“fair contribution”咨询（[EC](https://digital-strategy.ec.europa.eu/en/consultations/future-electronic-communications-sector-and-its-infrastructure)）。

## 2E TeleGeography 全球 IP Transit 价格史

【公开发表数据】TeleGeography 的 Global Internet Geography / IP Transit Pricing 是付费数据产品入口，覆盖国际互联网容量、价格与趋势（[GIG](https://www2.telegeography.com/global-internet-geography)，[IP Transit Pricing](https://www2.telegeography.com/ip-transit-pricing-service)）。本轮未找到可直接摘录的最近 median price per Mbps 原始数值。【行业共识】BEREC 2017 明确写到 transit/CDN 价格仍在下降、单位交付成本继续下降（[BEREC](https://www.berec.europa.eu/en/document-categories/berec/reports/berec-report-on-ip-interconnection-practices-in-the-context-of-net-neutrality)）。【推断】AI 时代更确定的变化是容量需求和私有互联/海缆锁量上移；公开价格曲线尚不足以证明 transit median 出现上涨拐点。

## 仍缺数据

- PeeringDB 无 Tier1/Tier2 原生字段；需用 `/api/net`、CAIDA AS Rank、transit 关系自建分类（[PeeringDB](https://docs.peeringdb.com/)）。
- Equinix/Digital Realty cross-connect 月费、运营商 commit tier 折扣表、三种 95th in/out 付费 transit MSA 样本，本轮未找到可公开挂载原件。
- TeleGeography 最近 median price per Mbps 与历年下降斜率需付费报告或公开博客原文；当前只可挂产品入口和 BEREC 趋势描述。
