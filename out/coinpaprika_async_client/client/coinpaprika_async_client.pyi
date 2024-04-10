from ..networking_layer import (
    HttpAsyncClient as HttpAsyncClient,
    Result as Result,
)
from typing import Any

class CoinPaprikaAsyncClient:
    def __init__(
        self, http: HttpAsyncClient = ..., api_key: str | None = None
    ) -> None: ...
    async def call_api(self, path: str, **query_params: Any) -> Result: ...
