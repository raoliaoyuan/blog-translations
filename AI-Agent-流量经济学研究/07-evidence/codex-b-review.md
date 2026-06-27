# Codex-B 对抗审稿

核对源：[Anthropic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)、[OpenAI state](https://developers.openai.com/api/docs/guides/conversation-state)、[Bedrock regions](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)、[Cloudflare 2025](https://blog.cloudflare.com/radar-2025-year-in-review/)、[AS37963](https://bgp.tools/as/37963)、[AS132203](https://bgp.tools/as/132203)。Twitch 韩国退出日为 2024-02-27；本批正文未直接使用。

## 01-framework/01-问题重定位.md
- “96.1%……重复上传”｜证据错配｜高｜96.1% 只能标 usage token L1；“字节未减少”需抓包，列 L3/L4。
- “region 少于 10 个”｜事实错误｜高｜Bedrock Claude 已多区域；OpenAI direct API region/ASN 不公开。按 direct/Bedrock/Azure/Vertex 分写。
- “系统性低估”｜过度断言｜高｜改“本单用户样本高于若干 chatbot 成本模型假设，待扩样”。
- “BGP 多线 1Gbps/月 ¥40,000–80,000”｜来源不足｜中｜补公开报价，否则降为示意。

## 04-china-structure/04-中国结算结构.md
- “阿里云 AS37963、腾讯云 AS132203”｜需精确｜低｜AS 基本可核，但 AS37963 注册名非“阿里云”；注明注册名与 Aliyun 前缀。
- “30 余个直联点”｜漏源｜中｜需工信部具体公告，栏目页不足。
- “5–10×/百倍价差”｜不一致｜中｜按 ¥/GB、¥/Mbps·月、专线分口径。
- “强制本地化”｜过度断言｜高｜改“鼓励/引导境内部署”。

## 05-empirical/5A-本地实测.md
- “cache_read 字节仍走上行”｜证据错配｜高｜文档支持 prefix/输入 token 口径；字节需 HTTP body 实测。
- “token 比≈字节比”｜逻辑跳跃｜高｜降 L4；JSON/SSE/base64/token 字节差异会改比例。
- “无主流厂商提供”｜事实错误｜中｜OpenAI 已有 `previous_response_id`/conversation state；需限定 Anthropic 口径。

## 05-empirical/scan-summary.md
- “上传 token 总计”｜口径风险｜中｜改“API 输入 token”；非网络字节。

## 06-stakeholder-impact/06-stakeholder-impact.md
- “Anthropic 主要在 us-west-2/us-east-1”｜事实错误｜高｜与 Bedrock 多区域不符；可用区不等同物理推理位置。
- “40–400 TB/天” vs “50–500 PB/天”｜不一致｜高｜统一用户数、日流量、token→byte；当前差约 1000×。
- “全球 1500 Tbps，占 0.3%–3%”｜分母错配｜高｜无统一全球总带宽口径；不能与自估 PB/天直除。
- “OpenAI 的 AS54321”｜未核实｜高｜删除；需 DNS/traceroute/RPKI/PeeringDB 实测。

## 07-evidence/07-evidence.md
- “10:1–30:1……L3”｜评级错｜高｜未补原文和同口径前应为 L4。
- “token≈字节 | L3”｜评级错｜中｜降 L4，抓包后再升。
- “Cloudflare AI bot”｜口径错｜中｜它是 Web/HTML crawler/user-action bot，非 LLM API 字节。
- “工信部/信通院”｜漏源｜中｜补最近一期文章/PDF，不能只放首页。

## 08-conclusion/08-conclusion.md
- “已确证……系统性低估 5–16 倍”｜证据错配｜高｜确证只保留 48,633 次 token 统计；低估移入 H5。
- “高度集中、ISP 不可绕开”｜逻辑跳跃｜高｜改“可能具备”，补份额、ASN/region、流量占比。
- “2026–2028 拐点”｜依据不足｜中｜改情景条件，不作日期断言。
- “强制本地化”｜表述风险｜高｜改“鼓励本地化/区域化”。

## 全文一致性问题
1. token、上传 token、网络字节混用。
2. AI crawler 与 LLM API 流量混用。
3. Region、ASN、可用区、Anycast/CDN 混写。
4. 中国 BGP/跨境价格缺样本。
5. 拐点、本地化、2026–2028 均应为 L4。

## 核心论断最严格挑战
1. 162:1 是单用户 usage token，不是行业字节比。
2. cache_read 的“96% 字节可省”未实测。
3. 10:1–30:1 与 162:1 口径不同，不能直接推出系统性低估。
4. 0.3%–3% 缺同口径分子/分母，应撤出摘要。
5. 结算重写还需规模、集中度、不可绕开性和合约失败。
