from typing import Optional, List, Dict, Any
from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class TickersEndpoint(CoinpaprikaAPI):
    async def tickers(self, params: Optional[dict] = None):
        return await self.internal.call_api("tickers", params)

    async def ticker(self, coin_id: str, params: Optional[dict] = None):
        return await self.internal.call_api(f"tickers/{coin_id}", params)

    async def historical(self, coin_id: str, params: Optional[dict]):
        return await self.internal.call_api(f"tickers/{coin_id}/historical", params)
