import re
from typing import Dict

def extract_numbers_from_report(report_text: str) -> list[float]:
    """从生成的报告文本里抓取所有数字"""
    raw_nums = re.findall(r"\d+\.?\d*", report_text)
    return [float(x) for x in raw_nums]

def validate_report(report_text: str, feature_dict: dict, tolerance: float = 1e-4) -> tuple[bool, str]:
    """
    校验：报告中出现的关键指标数字，必须和特征计算结果一致
    返回 (是否通过, 消息)
    """
    report_nums = extract_numbers_from_report(report_text)
    # 只校验我们算出的核心指标
    expected = {
        "cancel_rate": feature_dict["cancel_rate"],
        "total_notional": feature_dict["total_notional"]
    }
    for key, true_val in expected.items():
        if true_val == 0:
            continue
        matched = any(abs(n - true_val) < tolerance for n in report_nums)
        if not matched:
            return False, f"校验失败：指标 {key} 真值 {true_val} 在报告中找不到匹配数字，存在幻觉风险"
    return True, "PASS：所有核心数值校验通过"

