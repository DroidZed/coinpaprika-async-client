from typing import Optional, Dict
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Quote:
    price: float
    volume_24_h: float
    volume_24_h_change_24_h: float
    market_cap: int
    market_cap_change_24_h: float
    percent_change_15_m: int
    percent_change_30_m: int
    percent_change_1_h: int
    percent_change_6_h: int
    percent_change_12_h: float
    percent_change_24_h: float
    percent_change_7_d: float
    percent_change_30_d: float
    percent_change_1_y: float
    ath_price: Optional[int]
    ath_date: Optional[datetime]
    percent_from_price_ath: Optional[float]


@dataclass
class TickerItem:
    id: str
    name: str
    symbol: str
    rank: int
    circulating_supply: int
    total_supply: int
    max_supply: int
    beta_value: float
    first_data_at: datetime
    last_updated: datetime
    quotes: Dict[str, Quote]


@dataclass
class HistoryTickerItem:
    timestamp: datetime
    price: float
    volume_24_h: int
    market_cap: int
