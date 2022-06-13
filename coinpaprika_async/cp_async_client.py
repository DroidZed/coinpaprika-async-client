from httpx import AsyncClient, Response, HTTPError

from coinpaprika_async.api_exception import ApiException
from coinpaprika_async.response_object import ResponseObject


class Client:

    """
    An **async** client for interacting with Coinpaprika's API backend.
    """

    __API_URL = "https://api.coinpaprika.com/v1"

    def __init__(self):

        self.__async_client: AsyncClient = AsyncClient(
            headers={"Accept": "application/json", "User-Agent": "coinpaprika_async-async/python"}, timeout=20
        )

    # Internal handlers

    @staticmethod
    def __handle_response(response: Response) -> ResponseObject:

        resp = ResponseObject(status_code=response.status_code)

        try:
            resp.data = response.json()
            response.raise_for_status()

        except HTTPError:
            raise ApiException(response)

        finally:
            return resp

    async def __request(self, path: str, query_params: dict = None) -> ResponseObject:

        async with self.__async_client:
            uri = self.__create_api_uri(path)

            response: Response = await self.__async_client.get(url=uri, params=query_params)

        return self.__handle_response(response)

    def __create_api_uri(self, path: str) -> str:

        return f"{self.__API_URL}/{path}"

    async def __request_api(self, path: str, params: dict = None) -> ResponseObject:

        return await self.__request(path, params)

    async def __call_api(self, path: str, params: dict = None) -> ResponseObject:

        return await self.__request_api(path, params)

    # API CALLS

    async def global_market(self) -> ResponseObject:

        return await self.__call_api("global")

    async def coins(self) -> ResponseObject:

        return await self.__call_api("coins")

    async def coin(self, coin_id: str) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}")

    async def twitter(self, coin_id: str) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}/twitter")

    async def events(self, coin_id: str) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}/events")

    async def exchanges(self, coin_id: str) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}/exchanges")

    async def markets(self, coin_id: str, params: dict) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}/markets", params)

    async def candle(self, coin_id: str, params: dict = None) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}/ohlcv/latest", params)

    async def candles(self, coin_id: str, params: dict = None) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}/ohlcv/historical", params)

    async def today(self, coin_id: str, params: dict = None) -> ResponseObject:

        return await self.__call_api(f"coins/{coin_id}/ohlcv/today", params)

    async def people(self, person_id: str = None):

        return await self.__call_api(f"people/{person_id}")

    async def tags(self, params: dict = None) -> ResponseObject:

        return await self.__call_api("tags", params)

    async def tag(self, tag_id: str, params: dict = None) -> ResponseObject:

        return await self.__call_api(f"tags/{tag_id}", params)

    async def tickers(self, params: dict = None) -> ResponseObject:

        return await self.__call_api("tickers", params)

    async def ticker(self, coin_id: str, params: dict = None) -> ResponseObject:

        return await self.__call_api(f"tickers/{coin_id}", params)

    async def historical(self, coin_id: str, params: dict) -> ResponseObject:

        return await self.__call_api(f"tickers/{coin_id}/historical", params)

    async def exchange_list(self, params: dict = None) -> ResponseObject:

        return await self.__call_api("exchanges", params)

    async def exchange(self, exchange_id: str, params: dict) -> ResponseObject:

        return await self.__call_api(f"exchanges/{exchange_id}", params)

    async def exchange_markets(self, exchange_id: str, params: dict = None) -> ResponseObject:

        return await self.__call_api(f"exchanges/{exchange_id}/markets", params)

    async def search(self, params: dict = None) -> ResponseObject:

        return await self.__call_api("search", params)

    async def price_converter(self, params: dict = None) -> ResponseObject:

        return await self.__call_api("price-converter", params)
