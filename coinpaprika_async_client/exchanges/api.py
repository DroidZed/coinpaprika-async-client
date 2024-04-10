from typing import Any

from ..client import CoinPaprikaAsyncClient

from ..networking_layer import ApiError

from .models import *


class ExchangesEndpoint:
    def __init__(self) -> None:
        self.__internal = CoinPaprikaAsyncClient()

    async def exchange_list(self, **params: Any) -> ApiError | list[Exchange]:
        res = await self.__internal.call_api("exchanges", **params)

        if res.Error:
            return res.Error

        return [Exchange(**data) for data in res.Data]

    async def get_exchange(
        self, exchange_id: str, **params: Any
    ) -> ApiError | Exchange:
        res = await self.__internal.call_api(
            f"exchanges/{exchange_id}", **params
        )

        if res.Error:
            return res.Error

        return Exchange(**res.Data)

    async def exchange_markets(
        self, exchange_id: str, **params: Any
    ) -> ApiError | ExchangeMarket:
        res = await self.__internal.call_api(
            f"exchanges/{exchange_id}/markets", **params
        )

        if res.Error:
            return res.Error

        return ExchangeMarket(**res.Data)
