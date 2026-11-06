from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TradeEvent(BaseModel):
    account_id: str
    order_id: str
    side: str
    price: float
    quantity: float
    event_time: datetime
    is_cancel: bool = False

class SuspiciousCase(BaseModel):
    case_id: str
    symbol: str
    start_time: datetime
    end_time: datetime
    accounts: List[str]
    events: List[TradeEvent]
    case_type: str = Field(description="spoofing / wash_trade / layering")

