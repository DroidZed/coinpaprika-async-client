from coinpaprika_async_client.api.networking_layer.http_models import ApiError
from .models import MarketData
from ..coinpaprika_api import CoinpaprikaAPI


class MarketEndpoint(CoinpaprikaAPI):
    async def get_market_info(self) -> ApiError | MarketData:
        res = await self.internal.call_api("global")

        if res.Error:
            return res.Error

        return MarketData(**res.Data)
