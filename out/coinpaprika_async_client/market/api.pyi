from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError
from .models import MarketData as MarketData

class MarketEndpoint:
    def __init__(self) -> None: ...
    async def get_market_info(self) -> ApiError | MarketData: ...
