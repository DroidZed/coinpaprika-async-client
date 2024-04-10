from .models import *
from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError, Result as Result

class CoinsEndpoint:
    def __init__(self) -> None: ...
    async def get_all(self) -> ApiError | list[CoinItem]: ...
    async def coin_by_id(self, coin_id: str) -> Result: ...
    async def tweets_of_coin(
        self, coin_id: str
    ) -> ApiError | list[TwitterCoinItem]: ...
    async def events_of_coin(
        self, coin_id: str
    ) -> ApiError | list[EventCoinItem]: ...
    async def exchanges_of_coin(
        self, coin_id: str
    ) -> ApiError | list[ExchangeCoinItem]: ...
    async def markets_of_coin(
        self, coin_id: str, quotes: str = "USD"
    ) -> ApiError | list[MarketCoinItem]: ...
    async def latest_ohlcv(
        self, coin_id: str, quote: str = "usd"
    ) -> ApiError | list[CandleItem]: ...
    async def historical_ohlcv(
        self,
        coin_id: str,
        start: str,
        end: Optional[str] = None,
        limit: Optional[int] = None,
        interval: Optional[str] = None,
        quote: Optional[str] = None,
    ) -> ApiError | list[CandleItem]: ...
    async def ohlcv_of_today(
        self, coin_id: str, quote: str = "usd"
    ) -> ApiError | list[CandleItem]: ...
