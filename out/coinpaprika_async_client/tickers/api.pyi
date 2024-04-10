from .models import *
from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError

class TickersEndpoint:
    def __init__(self) -> None: ...
    async def tickers(
        self, quotes: str = "USD"
    ) -> ApiError | list[TickerItem]: ...
    async def ticker_by_coin(
        self, coin_id: str, quotes: str = "USD"
    ) -> ApiError | list[TickerItem]: ...
    async def historical_ticks(
        self,
        coin_id: str,
        start: str,
        end: str = "NOW",
        limit: int | None = 1000,
        quotes: str = "USD",
        interval: str = "5m",
    ) -> ApiError | list[HistoryTickerItem]: ...
