from .models import *
from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError
from typing import Any

class ExchangesEndpoint:
    def __init__(self) -> None: ...
    async def exchange_list(
        self, **params: Any
    ) -> ApiError | list[Exchange]: ...
    async def get_exchange(
        self, exchange_id: str, **params: Any
    ) -> ApiError | Exchange: ...
    async def exchange_markets(
        self, exchange_id: str, **params: Any
    ) -> ApiError | ExchangeMarket: ...
