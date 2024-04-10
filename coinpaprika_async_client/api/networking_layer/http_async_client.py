from typing import Dict, Optional, Any
from httpx import AsyncClient, HTTPStatusError

from .http_models import Result, ApiError


class HttpAsyncClient:
    """### Asynchronous HTTP client for making requests.

    Attributes:
        - client: The underlying AsyncClient instance for making requests.
    """

    async def send_request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Result:
        """Make an HTTP request using the specified method.

        Args:
            method: The HTTP method to use (e.g., "get", "post").
            url: The URL to send the request to.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.
            timeout: Optional number to indicate the timeout limit for the query.

        Returns:
            A Result instance representing either the JSON response body as a dictionary or list,
            or a RequestError if there was an error.

        Raises:
            RequestError: If there was an error in the request.
        """
        try:
            async with AsyncClient() as client:
                request_method = getattr(client, method)
                if method in {"get", "delete"}:
                    response = await request_method(
                        url, headers=headers, params=url_params
                    )
                else:
                    response = await request_method(
                        url, headers=headers, params=url_params, timeout=timeout
                    )
                response.raise_for_status()
                return Result(Data=response.json(), Error=None)
        except HTTPStatusError as exec:
            return Result(Error=ApiError(**exec.response.json()), Data=None)

    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        url_params: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Result:
        """Make an HTTP GET request.

        Args:
            url: The URL to send the request to.
            headers: Optional headers to include in the request.
            url_params: Optional URL parameters to include in the request.
            timeout: Optional number to indicate the timeout limit for the query.

        Returns:
            The JSON response body as a dictionary or list, or a RequestError if there was an error.
        """
        return await self.send_request(
            "get", url, headers=headers, url_params=url_params, timeout=timeout
        )
