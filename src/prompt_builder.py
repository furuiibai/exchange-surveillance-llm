def build_system_prompt() -> str:
    return """
You are a market surveillance analyst for a crypto exchange.
You are required to write a formal suspicious trading investigation report.

Hard rules you MUST follow:
1. All numerical metrics (cancel rate, total notional, etc.) can ONLY use the feature values provided. DO NOT invent any numbers.
2. Clearly state the case type: spoofing / wash trade / layering.
3. Include: Case Overview, Trading Behaviour Analysis, Evidence Summary, Risk Assessment, Recommendation.
4. Output only Markdown report content, no extra chat explanation.
"""

def build_user_prompt(case_info: dict, features: dict) -> str:
    user_content = f"""
Case basic info:
case_id: {features['case_id']}
instrument: {case_info['symbol']}
time window: {case_info['start_time']} ~ {case_info['end_time']}
involved accounts: {features['account_list']}
case type: {features['case_type']}

Calculated quantitative features (ONLY use these numbers):
- Cancel rate: {features['cancel_rate']:.4f}
- Total notional value: {features['total_notional']:.2f}
- Self-trade volume: {features['self_trade_volume']:.2f}

Write a formal exchange investigation report in markdown.
"""
    return user_content


def build_full_messages(case_info: dict, features: dict) -> list[dict]:
    return [
        {"role": "system", "content": build_system_prompt()},
        {"role": "user", "content": build_user_prompt(case_info, features)}
    ]

