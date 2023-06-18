from typing import Optional
from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class ExchangesEndpoint(CoinpaprikaAPI):
    async def exchange_list(self, params: Optional[dict] = None):
        return await self.internal.call_api("exchanges", params)

    async def exchange(self, exchange_id: str, params: Optional[dict]):
        return await self.internal.call_api(f"exchanges/{exchange_id}", params)

    async def exchange_markets(self, exchange_id: str, params: Optional[dict] = None):
        return await self.internal.call_api(f"exchanges/{exchange_id}/markets", params)
