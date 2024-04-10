from dataclasses import dataclass
from datetime import datetime
from typing import Dict

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
    ath_price: int | None
    ath_date: datetime | None
    percent_from_price_ath: float | None
    def __init__(
        self,
        price,
        volume_24_h,
        volume_24_h_change_24_h,
        market_cap,
        market_cap_change_24_h,
        percent_change_15_m,
        percent_change_30_m,
        percent_change_1_h,
        percent_change_6_h,
        percent_change_12_h,
        percent_change_24_h,
        percent_change_7_d,
        percent_change_30_d,
        percent_change_1_y,
        ath_price,
        ath_date,
        percent_from_price_ath,
    ) -> None: ...

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
    def __init__(
        self,
        id,
        name,
        symbol,
        rank,
        circulating_supply,
        total_supply,
        max_supply,
        beta_value,
        first_data_at,
        last_updated,
        quotes,
    ) -> None: ...

@dataclass
class HistoryTickerItem:
    timestamp: datetime
    price: float
    volume_24_h: int
    market_cap: int
    def __init__(self, timestamp, price, volume_24_h, market_cap) -> None: ...
