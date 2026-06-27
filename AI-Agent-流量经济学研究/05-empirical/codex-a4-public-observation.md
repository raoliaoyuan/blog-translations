# Codex-A4：Part 5B 公开流量观测

> 抓取日期：2026-06-27。目的：把 Part 5A 单用户 48,633 次 Claude Code API 调用得到的 162:1 上下行 usage token 比，放到公开观测语境中；同时标明 H1（BGP 流量方向反转）的当前数据状态。标注口径为「公开发表数据 / 行业共识 / 推断 / 未找到」。

## 1. Cloudflare

**公开发表数据。** Cloudflare Radar Bot Traffic 页面给出 bot/human、bot source、verified bots 视图，默认是近 7 天 HTTP requests；verified bots 是 Cloudflare 手工批准、通常透明且遵守指南的服务：[https://radar.cloudflare.com/bots#verified-bots](https://radar.cloudflare.com/bots#verified-bots)。本轮文本抓取未读到动态图静态数值。

**公开发表数据。** Cloudflare 2024-07-03 AI crawler blog 可静态引用：[https://blog.cloudflare.com/declaring-your-aindependence-block-ai-bots-scrapers-and-crawlers-with-a-single-click/](https://blog.cloudflare.com/declaring-your-aindependence-block-ai-bots-scrapers-and-crawlers-with-a-single-click/)。过去一年请求量前四为 Bytespider、Amazonbot、ClaudeBot、GPTBot；按访问 Cloudflare 站点覆盖率，Bytespider 40.40%、GPTBot 35.46%、ClaudeBot 11.17%、ImagesiftBot 8.75%、ChatGPT-User 1.84%、Claude-Web 0.04%、PerplexityBot 0.01%。2024 年 6 月，Cloudflare top 1M 站点中 38.73% 被 AI bots 访问，只有 2.98% 阻断或挑战。

**公开发表数据。** Cloudflare 2025-08-04 移除 Perplexity verified bot，理由是观察到其修改 user-agent、变更来源 ASN、忽略或不读取 robots.txt 以规避 no-crawl：[https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)。

**公开发表数据（二级报道 Cloudflare 2025 Top Internet Trends）。** 2025 年 Cloudflare 口径下，全球互联网流量增长 19%；AI bots 平均占 HTML requests 4.2%，Googlebot 单独占 4.5%，非 AI bots 约占 HTML page requests 一半：[https://www.techradar.com/pro/security/cloudflare-report-reveals-global-internet-internet-traffic-grew-19-percent-in-2025-but-a-lot-of-it-was-just-bots](https://www.techradar.com/pro/security/cloudflare-report-reveals-global-internet-internet-traffic-grew-19-percent-in-2025-but-a-lot-of-it-was-just-bots)。

**口径限定。** 这些是 web crawler / browser-agent / bot HTTP request，不是 LLM API 调用自身的 request/response body 字节。它们只能说明 AI 自动化访问进入 Web 观测面，不能直接证明 Part 5A 的 API 上下行字节结构。

## 2. IXP 与互联设施

**公开发表数据。** DE-CIX Frankfurt 官方页给 2 日、1 月、1 年、5 年总交换曲线：[https://www.de-cix.net/en/locations/frankfurt/statistics](https://www.de-cix.net/en/locations/frankfurt/statistics)。本次未从动态图读到静态数值；公开汇总显示 2025 年 12 月峰值 18.73 Tbit/s、日均约 12.17 Tbit/s：[https://en.wikipedia.org/wiki/DE-CIX](https://en.wikipedia.org/wiki/DE-CIX)。

**公开发表数据。** AMS-IX Amsterdam total stats 可静态读取：[https://www.ams-ix.net/ams/documentation/total-stats](https://www.ams-ix.net/ams/documentation/total-stats)。抓取时 current 约 10.101 Tb/s；平台 peak 15.034 Tb/s；daily peak in/out 13.308/13.281 Tb/s；daily average in/out 9.993/9.986 Tb/s；yearly average in/out 9.219/9.250 Tb/s。

**公开发表数据。** LINX 官方入口是动态 portal：[https://portal.linx.net/](https://portal.linx.net/)。本轮未从 HTML 抽取静态数值；公开汇总显示 peak 约 11.862 Tbps（2026），需复核：[https://en.wikipedia.org/wiki/London_Internet_Exchange](https://en.wikipedia.org/wiki/London_Internet_Exchange)。

**公开发表数据。** HKIX 官方图页：[https://www.hkix.net/hkix/stat/aggt/hkix-aggregate.html](https://www.hkix.net/hkix/stat/aggt/hkix-aggregate.html)。daily 图 2026-06-08 更新，max in/out 2.683/2.683 Tbit/s，average in/out 1.766/1.770 Tbit/s，current in/out 2.111/2.129 Tbit/s：[https://portal.hkix.net/customer/cgi-bin/mrtg-rrd-customer.cgi?log=hkix-aggregate&png=daily&u=](https://portal.hkix.net/customer/cgi-bin/mrtg-rrd-customer.cgi?log=hkix-aggregate&png=daily&u=)。公开汇总另列 peak in/out 3.202/3.201 Tbit/s、daily average in/out 2.894/2.895 Tbit/s：[https://en.wikipedia.org/wiki/Hong_Kong_Internet_Exchange](https://en.wikipedia.org/wiki/Hong_Kong_Internet_Exchange)。

**未找到。** Equinix IBX/Equinix Internet Exchange 未找到“AI 推理流量占比”披露；公开材料主要是互联增长和 AI-ready 数据中心叙事：[https://blog.equinix.com/blog/2021/05/27/equinix-internet-exchange-traffic-sustains-growth-across-regions/](https://blog.equinix.com/blog/2021/05/27/equinix-internet-exchange-traffic-sustains-growth-across-regions/)。

**结论。** IXP 公开统计不能识别 AI 推理流量信号：公开粒度通常是 total switched traffic、峰值、均值，看不到 SNI、HTTP path、payload、API domain 或 flow label；许多 hyperscaler AI 流量还可能走私有 PNI，不进入公开 IXP 图。

## 3. DPI 厂商

**未找到。** 本轮未找到可公开读取的 Sandvine Global Internet Phenomena Report 2024-2025 中 AI/LLM/Generative traffic 占比；入口：[https://www.sandvine.com/global-internet-phenomena-report](https://www.sandvine.com/global-internet-phenomena-report)。Nokia/Deepfield 公开报道强调 AI 网络压力，但属于调研，不是 DPI 占比：[https://www.techradar.com/pro/ai-is-too-big-for-the-european-internet-so-its-time-for-companies-to-work-together-nokia-says](https://www.techradar.com/pro/ai-is-too-big-for-the-european-internet-so-its-time-for-companies-to-work-together-nokia-says)。

**行业共识。** DPI 能看到 DNS/SNI、TLS/QUIC 指纹、证书、IP/ASN、flow duration、上下行字节、包长序列和应用签名；通常看不到 HTTPS 明文 prompt/output。AI 应用识别多依赖域名、客户端指纹和流量形态组合。

## 4. 端测与公共实验平台

**公开发表数据。** M-Lab NDT BigQuery 含 download/upload throughput，可自行计算上下行对称性；未找到官方维护的“AI 时代上/下行对称性趋势”汇总：[https://www.measurementlab.net/data/](https://www.measurementlab.net/data/)、[https://www.measurementlab.net/tests/ndt/](https://www.measurementlab.net/tests/ndt/)。

**公开发表数据。** RIPE Atlas 可做 ping、traceroute、DNS 等主动测量，适合观测到 AI API 域名的延迟/丢包；未找到 AI 推理流量 dashboard：[https://atlas.ripe.net/](https://atlas.ripe.net/)。

**公开发表数据。** APNIC Labs 公开 IPv6、DNS、BGP/RPKI 统计，但未找到 AI 应用分类：[https://stats.labs.apnic.net/](https://stats.labs.apnic.net/)。

**公开发表数据。** Netflix ISP Speed Index 仍是 Netflix 视频体验的 ISP 级指数入口，覆盖 Netflix 足量样本，不覆盖 LLM API 或 prompt 上行：[https://ispspeedindex.netflix.com/](https://ispspeedindex.netflix.com/)。

## 5. ASN / BGP 推断

**推断。** 推理服务商 ASN 实测方法：DNS 解析 API 域名 → traceroute/mtr → RDAP/WHOIS → RouteViews/RIS 查 BGP origin → RPKI 校验 → PeeringDB 查互联点 → CAIDA AS Rank 看互联度。入口：[http://www.routeviews.org/](http://www.routeviews.org/)、[https://ris.ripe.net/](https://ris.ripe.net/)、[https://stat.ripe.net/](https://stat.ripe.net/)、[https://www.peeringdb.com/](https://www.peeringdb.com/)、[https://asrank.caida.org/](https://asrank.caida.org/)。

**未找到。** 未找到稳定维护的 OpenAI / Anthropic / Google AI 推理域名 → ASN 公开映射。API 域名会经 CDN、云区、多 A/AAAA、GeoDNS 与私有互联漂移。CAIDA AS Rank 可看 hyperscaler ASN 互联度，但未找到把排名变化归因于 AI 推理的公开材料。

## 6. 学术论文

**公开发表数据。** 《Introducing Large Language Models as the Next Challenging Internet Traffic Source》给出远程 user-agent 交互 proof-of-concept，平均每 prompt query+response 7,593 bytes；不是生产 API usage 比：[https://arxiv.org/abs/2504.10688](https://arxiv.org/abs/2504.10688)。

**公开发表数据。** 《From Prompts to Packets》采集 ChatGPT、Copilot、Gemini Android app 文本/图像生成流量，含 60 小时泛化数据集和受控数据集，观察 TLS 1.3、QUIC、SNI 与上下行模式；最接近网络层 LLM app 测量，但不是 Claude Code 类 Agent usage token：[https://arxiv.org/abs/2510.11269](https://arxiv.org/abs/2510.11269)。

**公开发表数据。** 《Five Blind Men and the Internet》用 472 个 IXP 公开统计研究 2023-2024 总流量，覆盖约 300 Tbps 日峰值，估计两年增长 49.2%、年化 24.5%；不含 AI 应用分类：[https://arxiv.org/abs/2509.06515](https://arxiv.org/abs/2509.06515)。

**未找到。** 2024-2026 公开论文中未找到可直接对标 Part 5A 的真实生产 input:output usage token 数据集，尤其没有 Claude Code / Cursor / Copilot Agent 工具循环的跨用户 API usage 数据。

## 仍缺数据

Cloudflare Radar AI bots 动态图 API 数值；Sandvine/Nokia 2024-2025 AI/LLM DPI 占比；LINX、DE-CIX 机器可读当前峰值/平均值；M-Lab NDT 按年份、国家、ISP 的上/下行对称性汇总；OpenAI/Anthropic/Google AI API 域名到 ASN 的连续采样；真实生产 LLM API input:output 字节或 usage token 跨用户数据集。

## 可直接挂载到 Part 5B 的核心论断

公开观测目前只能证明“AI 相关自动化访问正在进入 Web 与网络观测面”，不能证明“LLM API 推理字节已经导致 BGP 层流量方向反转”。Cloudflare 的强信号是 crawler，不是 API；IXP 的强信号是总吞吐增长，不是应用分类；DPI 是最可能识别 AI 应用的公开来源，但本轮未找到 2024-2025 可引用占比；学术论文开始测 ChatGPT/Gemini 等 app 的 packets，却尚未给出 Agent workload 的生产 input:output 比例。因此 H1 当前状态应写为：**公开层面只有弱方向性证据，尚无可确证 BGP 流量方向反转的数据；Part 5A 的 162:1 是直接 usage-token 证据，但仍需 HTTP 字节抓包与 ASN/路径采样才能升级为网络层结论。**
