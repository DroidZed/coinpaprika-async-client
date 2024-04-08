from typing import Optional, Any

from .api.networking_layer import HttpAsyncClient


class CoinPaprikaAsyncClient:
    """
    ### An async client for interacting with Coinpaprika's API backend.

    """

    __FREE_API_URL = "https://api.coinpaprika.com/v1"

    __PRO_API_URL = "https://api-pro.coinpaprika.com/v1"

    def __init__(
        self,
        http: HttpAsyncClient = HttpAsyncClient(),
        api_key: Optional[str] = None,
    ):
        self._http_client = http
        self._is_paid = api_key != None
        self._api_key = api_key

    async def call_api(self, path: str, **query_params):
        uri = self.__create_api_uri(path)
        headers = self.__create_headers()

        return await self._http_client.get(
            uri, headers=headers, url_params=query_params, timeout=20
        )

    def __create_api_uri(self, path: str):
        return (
            f"{self.__FREE_API_URL}/{path}"
            if not self._is_paid
            else f"{self.__PRO_API_URL}/{path}"
        )

    def __create_headers(self):
        if self._is_paid:
            return {
                "Accept": "application/json",
                "User-Agent": "coinpaprika_async-async/python",
                "Authorization": self._api_key,
            }
        else:
            return {
                "Accept": "application/json",
                "User-Agent": "coinpaprika_async-async/python",
            }
