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
    def __init__(
        self,
        market_cap_usd,
        volume_24h_usd,
        bitcoin_dominance_percentage,
        cryptocurrencies_number,
        market_cap_ath_value,
        market_cap_ath_date,
        volume_24h_ath_value,
        volume_24h_ath_date,
        market_cap_change_24h,
        volume_24h_change_24h,
        last_updated,
    ) -> None: ...
