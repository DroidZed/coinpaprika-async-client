from typing import Any, Optional

from . import Result, HttpAsyncClient


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
    ) -> None:
        self._http_client = http
        self._is_paid = api_key != None
        self._api_key = api_key

    async def call_api(self, path: str, **query_params: Any) -> Result:
        uri = self.__create_api_uri(path)
        headers = self.__create_headers()

        return await self._http_client.get(
            uri, headers=headers, url_params=query_params, timeout=20
        )

    def __create_api_uri(self, path: str) -> str:
        return (
            f"{self.__FREE_API_URL}/{path}"
            if not self._is_paid
            else f"{self.__PRO_API_URL}/{path}"
        )

    def __create_headers(self) -> dict[str, Any | str]:

        headers: dict[str, Any | str] = {
            "Accept": "application/json",
            "User-Agent": "coinpaprika_async-async/python",
        }

        if self._is_paid:
            headers["Authorization"] = self._api_key

        return headers
