from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError
from .models import (
    APIUsage as APIUsage,
    CurrentMonthUsage as CurrentMonthUsage,
    KeyInfo as KeyInfo,
)

class KeyEndpoint:
    def __init__(self) -> None: ...
    async def get_key_info(self) -> ApiError | KeyInfo: ...
