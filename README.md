# exchange-surveillance-llm
LLM workflow for exchange market surveillance, auto-generate investigation reports for suspicious trading cases including spoofing, wash trade and layering.

✨ Project Highlights
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

Note: This project uses self-built model logic, no external LLM API / OpenAI dependency required.

意思：本项目使用自研模型逻辑，不需要外部大模型API、不依赖OpenAI。

### ② 新版 src/generator.py（移除OpenAI，留给你后续放自己训练的模型）
```python
from typing import List, Dict

class ReportGenerator:
    """Self-built model generator, replace with your trained model later"""
    def __init__(self):
        pass

    def generate_report_markdown(self, messages: List[Dict]) -> str:
        # TODO: Here you will load your trained model, feed case features, output report text
        # 后续在这里加载你自己训练好的模型，输入案件特征，输出报告
        return """
# Suspicious Trading Investigation Report
## Case Overview
This case is classified as spoofing activity. Multiple accounts submitted large orders with high cancellation rate to mislead market participants.

## Behaviour Analysis
The cancel rate of the involved orders is very high, which is a typical characteristic of spoofing. Traders place visible orders and cancel them rapidly before execution, without the intention to complete real trades.

## Evidence Summary
- High cancel rate
- Large quoted size with no intention of fill
- Orders are withdrawn in a very short time window

## Risk Assessment
High risk: This behaviour distorts market depth and misleads other market participants.

## Recommendation
Restrict trading permissions of the involved accounts and issue a formal warning.
"""

# MockGenerator 和上面合并，现在 Generator 本身就是预留的自研模型入口
MockGenerator = ReportGenerator

