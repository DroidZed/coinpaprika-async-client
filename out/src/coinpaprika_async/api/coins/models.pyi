from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class CoinItem:
    id: str
    name: str
    symbol: str
    rank: int
    is_new: bool
    is_active: bool
    type: str
    def __init__(
        self, id, name, symbol, rank, is_new, is_active, type
    ) -> None: ...

@dataclass
class Contract:
    contract: str
    platform: str
    type: str
    def __init__(self, contract, platform, type) -> None: ...

@dataclass
class Links:
    explorer: List[str]
    facebook: List[str]
    reddit: List[str]
    source_code: List[str]
    website: List[str]
    youtube: List[str]
    medium: None
    def __init__(
        self, explorer, facebook, reddit, source_code, website, youtube, medium
    ) -> None: ...

@dataclass
class Stats:
    subscribers: int | None
    contributors: int | None
    stars: int | None
    def __init__(self, subscribers, contributors, stars) -> None: ...

@dataclass
class LinksExtended:
    url: str
    type: str
    stats: Stats | None
    def __init__(self, url, type, stats) -> None: ...

@dataclass
class Parent:
    id: str
    name: str
    symbol: str
    def __init__(self, id, name, symbol) -> None: ...

@dataclass
class Tag:
    id: str
    name: str
    coin_counter: int
    ico_counter: int
    def __init__(self, id, name, coin_counter, ico_counter) -> None: ...

@dataclass
class Team:
    id: str
    name: str
    position: str
    def __init__(self, id, name, position) -> None: ...

@dataclass
class Whitepaper:
    link: str
    thumbnail: str
    def __init__(self, link, thumbnail) -> None: ...

@dataclass
class Coin:
    id: str
    name: str
    symbol: str
    parent: Parent
    rank: int
    is_new: bool
    is_active: bool
    type: str
    logo: str
    tags: List[Tag]
    team: List[Team]
    description: str
    message: str
    open_source: bool
    hardware_wallet: bool
    started_at: datetime
    development_status: str
    proof_type: str
    org_structure: str
    hash_algorithm: str
    contract: str
    platform: str
    contracts: List[Contract]
    links: Links
    links_extended: List[LinksExtended]
    whitepaper: Whitepaper
    first_data_at: datetime
    last_data_at: datetime
    def __init__(
        self,
        id,
        name,
        symbol,
        parent,
        rank,
        is_new,
        is_active,
        type,
        logo,
        tags,
        team,
        description,
        message,
        open_source,
        hardware_wallet,
        started_at,
        development_status,
        proof_type,
        org_structure,
        hash_algorithm,
        contract,
        platform,
        contracts,
        links,
        links_extended,
        whitepaper,
        first_data_at,
        last_data_at,
    ) -> None: ...

@dataclass
class TwitterCoinItem:
    date: datetime
    user_name: str
    user_image_link: str
    status: str
    is_retweet: bool
    retweet_count: int
    like_count: int
    status_link: str
    status_id: str
    media_link: str
    youtube_link: str
    def __init__(
        self,
        date,
        user_name,
        user_image_link,
        status,
        is_retweet,
        retweet_count,
        like_count,
        status_link,
        status_id,
        media_link,
        youtube_link,
    ) -> None: ...

@dataclass
class EventCointItem:
    id: str
    date: datetime
    date_to: str
    name: str
    description: str
    is_conference: bool
    link: str
    proof_image_link: str
    def __init__(
        self,
        id,
        date,
        date_to,
        name,
        description,
        is_conference,
        link,
        proof_image_link,
    ) -> None: ...

@dataclass
class Fiat:
    name: str
    symbol: str
    def __init__(self, name, symbol) -> None: ...

@dataclass
class ExchangeCoinItem:
    id: str
    name: str
    fiats: List[Fiat]
    adjusted_volume_24h_share: float
    def __init__(self, id, name, fiats, adjusted_volume_24h_share) -> None: ...

@dataclass
class Key:
    price: float
    volume_24h: float
    def __init__(self, price, volume_24h) -> None: ...

@dataclass
class MarketCoinItem:
    exchange_id: str
    exchange_name: str
    pair: str
    base_currency_id: str
    base_currency_name: str
    quote_currency_id: str
    quote_currency_name: str
    market_url: str
    category: str
    fee_type: str
    outlier: bool
    adjusted_volume_24h_share: float
    quotes: Dict[str, Key]
    last_updated: datetime
    def __init__(
        self,
        exchange_id,
        exchange_name,
        pair,
        base_currency_id,
        base_currency_name,
        quote_currency_id,
        quote_currency_name,
        market_url,
        category,
        fee_type,
        outlier,
        adjusted_volume_24h_share,
        quotes,
        last_updated,
    ) -> None: ...

@dataclass
class CandleItem:
    time_open: datetime
    time_close: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    market_cap: int
    def __init__(
        self, time_open, time_close, open, high, low, close, volume, market_cap
    ) -> None: ...
