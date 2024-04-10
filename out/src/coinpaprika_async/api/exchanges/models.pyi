from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Fiat:
    name: str
    symbol: str
    def __init__(self, name, symbol) -> None: ...

@dataclass
class Links:
    website: List[str]
    twitter: List[str]
    def __init__(self, website, twitter) -> None: ...

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
    def __init__(
        self,
        reported_volume_24_h,
        adjusted_volume_24_h,
        reported_volume_7_d,
        adjusted_volume_7_d,
        reported_volume_30_d,
        adjusted_volume_30_d,
        price,
        volume_24_h,
    ) -> None: ...

@dataclass
class Quotes:
    key: Key
    def __init__(self, key) -> None: ...

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
    sessions_per_month: int | None = ...
    def __init__(
        self,
        id,
        name,
        active,
        website_status,
        api_status,
        description,
        message,
        links,
        markets_data_fetched,
        adjusted_rank,
        reported_rank,
        currencies,
        markets,
        confidence_score,
        fiats,
        quotes,
        last_updated,
        sessions_per_month,
    ) -> None: ...

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
    def __init__(
        self,
        pair,
        base_currency_id,
        base_currency_name,
        quote_currency_id,
        quote_currency_name,
        market_url,
        category,
        fee_type,
        outlier,
        reported_volume_24_h_share,
        quotes,
        last_updated,
    ) -> None: ...
