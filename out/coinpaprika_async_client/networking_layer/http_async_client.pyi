from .http_models import ApiError as ApiError, Result as Result
from typing import Any, Dict

class HttpAsyncClient:
    async def send_request(
        self,
        method: str,
        url: str,
        headers: Dict[str, str] | None = None,
        url_params: Dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> Result: ...
    async def get(
        self,
        url: str,
        headers: Dict[str, str] | None = None,
        url_params: Dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> Result: ...
