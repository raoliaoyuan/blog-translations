# Part 3 资料笔记：公有云出向定价史

日期：2026-06-27。标注规则：**公开发表数据**=法规、厂商价目/公告、学术论文或可公开访问媒体；**行业共识**=多家行业评论反复采用但缺少审计口径；**推断**=基于公开价格与网络成本常识的解释；**仍缺数据**=本轮未找到可挂报告的原始材料。

## 3A 入向免费 + 出向阶梯计费的起源

- **公开发表数据**：AWS S3 于 2006-03-14 发布；发布稿定位是可按量购买的互联网对象存储服务，早期收费项已经拆成存储、请求、数据传输，而不是传统托管带宽包。[Amazon press release](https://press.aboutamazon.com/2006/3/amazon-web-services-launches-amazon-s3)
- **公开发表数据**：Garfinkel 对 EC2/S3/SQS 的早期评估记录了 2006-2007 年 AWS 的“低固定成本 + 用量计费”模型，是补 2006-2009 定价档案的重要学术入口。[Harvard TR-08-07 PDF](https://dash.harvard.edu/bitstream/handle/1/24829568/tr-08-07.pdf?sequence=1)
- **公开发表数据/考古入口**：AWS 早期价目需要从 Wayback 抓 `aws.amazon.com/s3` 与 `aws.amazon.com/ec2` 的 2006-2009 快照，重点看 pricing 区块是否已拆分 Data Transfer In/Out。[S3 Wayback index](https://web.archive.org/web/*/http://aws.amazon.com/s3*)；[EC2 Wayback index](https://web.archive.org/web/*/http://aws.amazon.com/ec2*)
- **公开发表数据/仍需复核**：本轮能定位到的最早“入向免费”候选，是 AWS S3 三周年特别价格，公开索引显示 2009-03-31 的 “Celebrating S3's Third Birthday With Special Anniversary Pricing”。需用 Internet Archive 复核全文是否为临时促销还是长期规则。[AWS blog URL](https://aws.amazon.com/blogs/aws/celebrating-s3s-third-birthday-with-special-anniversary-pricing/)
- **公开发表数据**：当前成熟形态在 AWS S3/EC2 价目中非常明确：互联网入向免费，互联网出向前 100GB/月免费，之后按出向阶梯计费；AWS 还说明 100GB 免费额度跨多项 AWS 服务和区域汇总，中国区与 GovCloud 例外。[AWS EC2 pricing](https://aws.amazon.com/ec2/pricing/on-demand/)；[AWS S3 pricing](https://aws.amazon.com/s3/pricing/)
- **推断**：GCP/Azure 基本继承了“入向免费 + 出向阶梯”的经济结构，但没有完全复制 AWS：GCP 另分 Premium/Standard Network Service Tiers；Azure 另分 Microsoft Premium Global Network 与 Routing Preference transit ISP。[GCP network pricing](https://cloud.google.com/vpc/network-pricing)；[Azure bandwidth pricing](https://azure.microsoft.com/en-us/pricing/details/bandwidth/)

## 3B 海外三巨头出向带宽定价变迁

- **AWS 当前公开价**：入向免费；互联网出向前 100GB/月免费；超过 500TB/月需联系销售；EU 客户可按 Data Act 申请降低特定用例费率；搬离 AWS 时可申请免费互联网出向信用。[AWS EC2 pricing](https://aws.amazon.com/ec2/pricing/on-demand/)；[AWS EC2 FAQ](https://aws.amazon.com/ec2/faqs/)
- **AWS 首档价格**：常见公开对比仍引用 AWS S3 美国西部出向 $0.09/GB；本轮未抓到 AWS 静态表格，只能作为第三方公开价格对比，需用 AWS Price List API 复核。[Backblaze comparison](https://www.backblaze.com/cloud-storage/pricing)
- **仍缺数据**：AWS 2017、2020 互联网出向重大调价的官方公告 URL 未在本轮稳定找到；建议下一轮按 AWS “price reduction data transfer out 2017 2020” 与 AWS Price List API 历史快照补证。
- **GCP 当前公开价**：入向免费；Premium Tier 到北美/欧洲/多数亚洲目的地前 1GiB/月免费，1GiB-1TiB 为 $0.12/GiB，1-10TiB 为 $0.11/GiB，10TiB 以上北美 $0.08/GiB、欧洲/多数亚洲 $0.085/GiB；中国目的地首档 $0.23/GiB。页面还注明 2024-02-01 起部分 Premium Tier 互联网出向 SKU 涨价。[GCP network pricing](https://cloud.google.com/vpc/network-pricing)
- **Azure 当前公开价**：Data Transfer In 免费；Premium Global Network 互联网出向前 100GB/月免费，北美/欧洲到任意目的地下一级 10TB 为 $0.087/GB，随后 $0.083/$0.07/$0.05；Routing Preference transit ISP 更低，北美/欧洲下一 10TB 为 $0.08/GB。[Azure bandwidth pricing](https://azure.microsoft.com/en-us/pricing/details/bandwidth/)
- **仍缺数据**：GCP/Azure 与 AWS 2017、2020 同期的官方降价公告未形成完整时间线；当前只确认 GCP 2024 部分 SKU 涨价与三家 2024-2025 Data Act/迁云信用政策。

## 3C 2024 EU Data Act 与 egress fee 下调

- **公开发表数据**：Data Act 将 data egress charges 定义为客户把数据从云商 ICT 基础设施经网络取出到另一云或本地时的数据传输费；switching charges 包含 data egress charges。[Regulation (EU) 2023/2854](https://data.europa.eu/eli/reg/2023/2854/oj)
- **公开发表数据**：Data Act recital 88 直指过高 egress fee 会抑制迁移、限制数据自由流动并造成锁定；规则要求 switching charges 在法规生效三年后取消，过渡期内只能降低收取。[Regulation (EU) 2023/2854](https://data.europa.eu/eli/reg/2023/2854/oj)
- **公开发表数据**：Google 2024-01-12 宣布，停止使用 Google Cloud 并迁往其他云或本地的客户可免费网络数据转出，全球适用；退出页要求提交 Exit Notice，最终发票给出数据转移成本信用。[Google Cloud blog](https://cloud.google.com/blog/products/networking/eliminating-data-transfer-fees-when-migrating-off-google-cloud)；[Google Cloud exit page](https://cloud.google.com/exit-cloud)
- **公开发表数据**：AWS 要求客户在搬离前联系 Support 申请 “free data transfer to move off AWS”；批准后给临时信用，通常 90 天内完成迁出，并要求搬离 AWS 或特定 AWS 服务的全部数据。[AWS EC2 FAQ](https://aws.amazon.com/ec2/faqs/)
- **公开发表数据**：Azure 价目 FAQ 称，客户为切换到另一云或本地数据中心而离开 Azure 时可申请超过每月 100GB 免费额度的出向信用。[Azure bandwidth pricing](https://azure.microsoft.com/en-us/pricing/details/bandwidth/)
- **公开发表数据**：Google 另推出 Data Transfer Essentials，用于同一组织跨云平台的服务间公网传输；文档称初期按指引使用不收费，若未来收费会提前通知。[Google Data Transfer Essentials](https://docs.cloud.google.com/data-transfer-essentials/docs/overview)
- **仍缺数据**：没有找到可引用的真实客户账单前后对比。当前厂商规则多以“信用/申请/批准”为路径，不等同于全量客户自动降价。

## 3D 零出向挑战者

- **公开发表数据**：Cloudflare R2 Standard 为 $0.015/GB-month，Class A $4.50/百万次，Class B $0.36/百万次，所有存储类直接出向到互联网免费；免费层含 10GB-month、100 万 Class A、1000 万 Class B。[Cloudflare R2 pricing](https://developers.cloudflare.com/r2/pricing/)
- **公开发表数据**：Backblaze B2 起价 $6.95/TB/月，免费出向最高为平均月存储量 3 倍，超过后 $0.01/GB；B2 Overdrive 标注 unlimited free egress。[Backblaze B2 pricing](https://www.backblaze.com/cloud-storage/pricing)
- **公开发表数据**：Wasabi Pay-as-you-go 起价 $6.99/TB/月，2026-07-01 调至 $7.99/TB/月；页面明确无 egress 或 API 请求费。[Wasabi pricing](https://wasabi.com/pricing/)
- **行业共识/仍缺数据**：对象存储挑战者用“零出向”攻击 hyperscaler 定价，但公开市场份额通常只统计整体 IaaS/PaaS 云。媒体引用 Synergy Q1 2025 份额为 AWS 32%、Azure 23%、Google Cloud 10%；Cloudflare R2/Backblaze/Wasabi 的对象存储收入份额未见可审计公开口径。[TechRadar report](https://www.techradar.com/pro/google-slashes-uk-and-eu-cloud-data-transfer-fees-ahead-of-eu-data-act)

## 3E 中国公有云出向定价现状

- **公开发表数据**：腾讯云 CVM 公网网络明确提供多线 BGP ISP 接入；计费方式包括按带宽与按流量，按流量按公网出方向流量逐小时计费，按带宽按公网传输速率计费。[Tencent Cloud public network billing](https://intl.cloud.tencent.com/document/product/213/10578)
- **公开发表数据/仍需复核单价**：阿里云 ECS/EIP 公网带宽公开文档区分按固定带宽与按使用流量，实际 RMB 单价随地域、线路、EIP/CLB/CDT 等产品变化；需使用阿里云价格计算器或中国站区域价格页复核。[Alibaba Cloud public bandwidth doc](https://help.aliyun.com/zh/ecs/user-guide/public-bandwidth)
- **公开发表数据/仍需复核单价**：华为云 EIP/带宽按需计费通常分按带宽、按流量，线路可见全动态 BGP/静态 BGP 等差异；具体单价需按区域价格页确认。[Huawei Cloud EIP pricing docs](https://support.huaweicloud.com/intl/en-us/price-eip/eip_price_0001.html)
- **推断**：中国云的“优质 BGP / BGP Pro / 三网通 / 多线 BGP”本质是对跨运营商路由质量与覆盖的分层，不是简单的互联网出向 GB 价；同一云商可能在 ECS、EIP、CDN、全球加速、云数据传输等产品下给出不同带宽/流量口径。

## 3F 出向带宽真实毛利率

- **公开发表数据**：高能物理云突发实验论文指出，对数据密集型应用，egress networking costs can exceed compute costs，并讨论用 Internet2 Cloud Connect 等专线降低三大云出向费用。[arXiv 2104.06913](https://arxiv.org/abs/2104.06913)
- **公开发表数据**：网络带宽分配论文从云提供商角度称带宽成本是 operating cost 的 major component，但它研究的是优化问题，不披露 hyperscaler COGS。[arXiv 2203.06725](https://arxiv.org/abs/2203.06725)
- **行业共识**：a16z 的云成本文章把云账单视为可观的软件毛利压力，但重点是整体云成本与 repatriation，并非 egress 毛利拆解。[a16z](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/)
- **仍缺数据**：未找到 AWS/Azure/GCP 披露“互联网出向”单项毛利率或网络成本结构。可比较的是零售 egress 价与批发 transit/peering 成本的数量级差异，但这仍是推断，不能写成审计毛利率。

## 3G 历史争议

- **行业共识**：“出向带宽是 hyperscaler 利润中心”主要来自挑战者宣传、开发者账单争议和监管评论；可信度中等，因为零售价格长期稳定、挑战者可做到零/低出向，但缺少 hyperscaler 分项成本审计。[Cloudflare R2 pricing](https://developers.cloudflare.com/r2/pricing/)；[Backblaze comparison](https://www.backblaze.com/cloud-storage/pricing)
- **公开发表数据**：Data Act 是最强监管证据，它不直接说 egress 是利润中心，但明确认为过高或不合理的出向/迁移费用会形成锁定、限制竞争。[Regulation (EU) 2023/2854](https://data.europa.eu/eli/reg/2023/2854/oj)
- **仍缺数据**：本轮未找到 CNCF 或 FinOps Foundation 对 egress fee 毛利率的正式量化立场。可继续检索 FinOps 关于 data transfer cost allocation/FOCUS 的材料，以及 CNCF 对云商锁定、OCI registry 出向成本的公开评论。
