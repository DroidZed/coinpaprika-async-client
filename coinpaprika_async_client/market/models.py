from dataclasses import dataclass


@dataclass
class MarketData:
    market_cap_usd: int
    volume_24h_usd: int
    bitcoin_dominance_percentage: float
    cryptocurrencies_number: int
    market_cap_ath_value: int
    market_cap_ath_date: str
    volume_24h_ath_value: int
    volume_24h_ath_date: str
    market_cap_change_24h: float
    volume_24h_change_24h: float
    last_updated: int
