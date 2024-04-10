from ..coinpaprika_api import CoinpaprikaAPI as CoinpaprikaAPI
from .models import MarketData as MarketData

class MarketEndpoint(CoinpaprikaAPI):
    async def getMarketInfo(self): ...
