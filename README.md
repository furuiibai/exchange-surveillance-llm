# exchange-surveillance-llm
LLM workflow for exchange market surveillance, auto-generate investigation reports for suspicious trading cases including spoofing, wash trade and layering.

## ✨ Project Highlights
This pipeline decouples quantitative feature calculation and LLM text generation, with a dedicated numeric validation layer to **mitigate LLM numerical hallucination** — all figures appearing in the final investigation report must match pre-computed order-flow metrics.
> In compliance scenarios, fabricated numbers are far more harmful than incomplete reports.

## 📁 Project Structure

"""
── src/
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
"""

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
pip install pydantic openai
