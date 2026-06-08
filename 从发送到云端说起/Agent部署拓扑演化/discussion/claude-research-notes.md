# Claude 自研核验笔记（用于与 Codex 辩论 + 最终综合）

口径：2026-06 前后；链接均经 WebSearch 返回为官方/权威结果。

## 端侧硬件（本地 Token 服务）
- **NVIDIA DGX Spark**（原 Project DIGITS）：GB10 Grace Blackwell 超芯片、128GB 统一内存、本地可跑至 2000 亿参数、1 petaFLOP FP4；CES 2025 以 Project DIGITS 亮相、GTC 2025-03 改名、2025 年底出货；Founder's Edition 2026-02 价格 $4,699；ASUS/Dell/HP/Lenovo 代工。官方："Build and run autonomous AI agents securely and locally"。
  - 官方：https://www.nvidia.com/en-us/products/workstations/dgx-spark/
  - 官方新闻：https://nvidianews.nvidia.com/news/nvidia-announces-dgx-spark-and-dgx-station-personal-ai-computers
- **Apple 端侧 ~3B 模型 + Private Cloud Compute**：端侧 ~30 亿参数模型、2-bit 量化、KV-cache 共享省 37.5% 内存；PCC 为可验证隐私的服务器端推理（端到端加密、可审计）。
  - PCC 官方：https://security.apple.com/blog/private-cloud-compute/
  - 基础模型官方：https://machinelearning.apple.com/research/introducing-apple-foundation-models
  - 2025 更新：https://machinelearning.apple.com/research/apple-foundation-models-2025-updates

## 中国侧（私有化/一体机/信创）
- **大模型一体机**："2025 一体机元年"；2025-02 起 20+ 国产芯片厂商（华为昇腾、百度昆仑芯、海光、沐曦、摩尔线程）适配 DeepSeek；信创栈（鲲鹏+昇腾、银河麒麟 V10）、国密、政务/金融/军工/能源私有化刚需。
  - 报道口径：新浪财经《2025 一体机元年》https://finance.sina.com.cn/roll/2025-03-03/doc-ineniywi2543923.shtml
  - 报道口径：量子位 零一万物模型一体机搭载华为 GPU https://www.qbitai.com/2025/03/264900.html
  - 报道口径：雷峰网 一体机落地调研 https://m.leiphone.com/category/industrynews/rjHHq7gP8NqXlrY5.html
  - 注：上述多为媒体口径，文中须标注"报道口径"；尽量再找官方招标/厂商官网佐证。

## 我的反方论点（用于质疑 Codex，避免"本地必胜"过度乐观）
1. **Token 经济学反而利好云**：前沿模型推理靠大批量、高利用率摊薄成本；个人/单机本地算力大多时间闲置，单位 Token 成本通常高于云。DGX Spark 4 千美元服务单人，经济性对多数任务不如云。→ 本地是"隐私/低延迟/离线/合规"的利基，不是默认。
2. **能力鸿沟持续拉大**：前沿模型规模仍在增长，本地能跑 3B–200B，但与云端最强模型差距长期存在。"小模型够用"高度依赖具体任务。
3. **Apple PCC 重构了隐私论证**：它证明"云规模 + 可验证隐私"可同时成立，反而削弱了"为隐私必须上本地/私有化"的论点——第三条路可能吃掉两端。
4. **中国一体机热是否可持续**：很大程度由 DeepSeek 时刻 + 信创采购驱动（政务/军工刚需），而非纯经济性；需追问是结构性需求还是 2025 脉冲。
5. **两轴可解耦**：Agent 编排轻、Token 服务重；真正的分流问题是"推理放哪"，而 Agent 位置主要跟随"到工具/数据的延迟"和"数据引力"。
