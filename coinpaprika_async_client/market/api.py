from ..client import CoinPaprikaAsyncClient

from ..networking_layer import ApiError

from .models import MarketData


class MarketEndpoint:
    def __init__(self) -> None:
        self.__internal = CoinPaprikaAsyncClient()

    async def get_market_info(self) -> ApiError | MarketData:
        res = await self.__internal.call_api("global")

        if res.Error:
            return res.Error

        return MarketData(**res.Data)
