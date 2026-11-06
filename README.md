# exchange-surveillance-llm
LLM workflow for exchange market surveillance, auto-generate investigation reports for suspicious trading cases including spoofing, wash trade and layering.

## Project Highlights
This pipeline decouples quantitative feature calculation and model-based report generation, with a dedicated numeric validation layer to mitigate numerical hallucination — all figures in the report must match pre-computed order-flow metrics.
This project uses self-built models and local order data, no external LLM API.

## 📁 Project Structure
```
├── src/
│   ├── schema.py           # Pydantic data schema for standardized trading case input
│   ├── features.py         # Order-flow feature calculator (cancel rate, notional, self-trade volume)
│   ├── prompt_builder.py   # System & user prompt template
│   ├── generator.py        # LLM caller + mock backend for offline demo
│   ├── validators.py       # Numeric hallucination checker (core module)
│   ├── render.py           # Save output to markdown report
│   └── pipeline.py         # End-to-end workflow entry
├── scripts/
│   └── gen_synthetic_cases.py  # Synthetic case generator (to be implemented)
├── data/samples/           # Manually curated JSON samples: spoofing / wash trade
├── examples/
│   ├── spoofing/           # Finished investigation reports for spoofing cases
│   └── wash_trade/         # Finished investigation reports for wash-trade cases
├── tests/                  # Unit tests for feature & validation logic
├── .gitignore
├── LICENSE
└── README.md
```


## 🧠 Workflow

Case JSON Input → Feature Calculation → Prompt Assembly → LLM Generate Report → Numeric Validation → Export Markdown Report

1. Load standardized suspicious trading case
2. Compute fixed quantitative indicators from raw order events
3. Inject only pre-calculated metrics into LLM prompt
4. Generate formal market-surveillance investigation report
5. Auto-validate all core numbers inside the report
6. If validation passes, save report; otherwise throw error

## 🚀 Quick Start
### Dependency
```bash
pip install pydantic

Note: This project uses self-built model logic, no external LLM / OpenAI API dependency.

from src.pipeline import run_pipeline
from src.schema import SuspiciousCase

# Load your case from data/samples
# run_pipeline(case, output_path="examples/spoofing/report.md")


解释：
1. 安装命令保留
2. Note 保留，说明**无外部大模型依赖，预留自研模型位置**
3. 下面放极简的调用示例代码（注释状态，告诉别人怎么启动）
4. generator.py 的完整代码**不要贴进README**！它是仓库里 src 下的文件，别人进仓库点开 src/generator.py 就能看到源码

✅ 区分清楚：
- README：告诉别人怎么装、怎么跑、项目是干嘛的
- generator.py：是仓库里的源码文件，放实现、TODO注释

顺带同步更新你的 Highlights，把这句加上，统一口径：
```markdown
✨ Project Highlights
This pipeline decouples quantitative feature calculation and model-based report generation, with a dedicated numeric validation layer to mitigate numerical hallucination — all figures appearing in the final investigation report must match pre-computed order-flow metrics.
Self-built model workflow, no external LLM API required.



