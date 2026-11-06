from src.schema import SuspiciousCase

def calc_cancel_rate(case: SuspiciousCase) -> float:
    """计算撤单率：撤单订单数 / 总报单数"""
    total_orders = 0
    cancel_count = 0
    for evt in case.events:
        if not evt.is_cancel:
            total_orders += 1
        else:
            cancel_count +=1
    if total_orders == 0:
        return 0.0
    return cancel_count / total_orders

def calc_self_trade_volume(case: SuspiciousCase) -> float:
    """简易对敲识别：同一组账户之间互相成交的名义量"""
    vol = 0.0
    # 这里是预留接口，后面再完善匹配逻辑
    return vol

def get_total_notional(case: SuspiciousCase) -> float:
    """计算涉案总名义金额"""
    notional = 0.0
    for evt in case.events:
        if not evt.is_cancel:
            notional += evt.price * evt.quantity
    return notional

def extract_all_features(case: SuspiciousCase) -> dict:
    return {
        "case_id": case.case_id,
        "case_type": case.case_type,
        "cancel_rate": calc_cancel_rate(case),
        "total_notional": get_total_notional(case),
        "self_trade_volume": calc_self_trade_volume(case),
        "account_list": case.accounts
    }

