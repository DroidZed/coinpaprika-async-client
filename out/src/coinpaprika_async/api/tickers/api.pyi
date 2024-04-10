from .models import *
from ..coinpaprika_api import CoinpaprikaAPI as CoinpaprikaAPI

class TickersEndpoint(CoinpaprikaAPI):
    async def tickers(self, quotes: str = "USD"): ...
    async def ticker_by_coin(self, coin_id: str, quotes: str = "USD"): ...
    async def historical_ticks(
        self,
        coin_id: str,
        start: str,
        end: str = "NOW",
        limit: int | None = 1000,
        quotes: str = "USD",
        interval: str = "5m",
    ): ...
