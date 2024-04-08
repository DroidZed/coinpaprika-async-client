from typing import Optional, Any

from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class ExchangesEndpoint(CoinpaprikaAPI):
    async def exchange_list(self, **params):
        res = await self.internal.call_api("exchanges", **params)

        if res.Error:
            return res.Error

        return [Exchange(**data) for data in res.Data]

    async def exchange(self, exchange_id: str, **params):
        res = await self.internal.call_api(f"exchanges/{exchange_id}", **params)

        if res.Error:
            return res.Error

        return Exchange(**res.Data)

    async def exchange_markets(self, exchange_id: str, **params):
        res = await self.internal.call_api(
            f"exchanges/{exchange_id}/markets", **params
        )

        if res.Error:
            return res.Error

        return ExchangeMarket(**res.Data)
