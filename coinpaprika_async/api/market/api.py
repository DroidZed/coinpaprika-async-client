from .models import MarketData
from ..coinpaprika_api import CoinpaprikaAPI


class MarketEndpoint(CoinpaprikaAPI):
    async def getMarketInfo(self):
        res = await self.internal.call_api("global")

        if res.Error:
            return res.Error

        return MarketData(**res.Data)
