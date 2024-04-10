from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Fiat:
    name: str
    symbol: str


@dataclass
class Links:
    website: List[str]
    twitter: List[str]


@dataclass
class Key:
    reported_volume_24_h: int
    adjusted_volume_24_h: int
    reported_volume_7_d: int
    adjusted_volume_7_d: int
    reported_volume_30_d: int
    adjusted_volume_30_d: int
    price: float
    volume_24_h: float


@dataclass
class Quotes:
    key: Key


@dataclass
class Exchange:
    id: str
    name: str
    active: bool
    website_status: bool
    api_status: bool
    description: str
    message: str
    links: Links
    markets_data_fetched: bool
    adjusted_rank: int
    reported_rank: int
    currencies: int
    markets: int
    confidence_score: float
    fiats: List[Fiat]
    quotes: Quotes
    last_updated: datetime
    sessions_per_month: Optional[int] = None


@dataclass
class ExchangeMarket:
    pair: str
    base_currency_id: str
    base_currency_name: str
    quote_currency_id: str
    quote_currency_name: str
    market_url: str
    category: str
    fee_type: str
    outlier: bool
    reported_volume_24_h_share: float
    quotes: Quotes
    last_updated: datetime
