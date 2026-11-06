from openai import OpenAI
from typing import List, Dict, Optional

class ReportGenerator:
    def __init__(self, api_key: str, base_url: Optional[str] = None, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def generate_report_markdown(self, messages: List[Dict]) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.1  # low temperature for stable, factual output
        )
        return resp.choices[0].message.content.strip()


# Mock 后端，没有API key的时候也能演示跑通流程（面试demo非常好用）
class MockGenerator:
    def generate_report_markdown(self, messages: List[Dict]) -> str:
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

