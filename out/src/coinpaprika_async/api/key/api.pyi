from ..coinpaprika_api import CoinpaprikaAPI as CoinpaprikaAPI
from .models import (
    APIUsage as APIUsage,
    CurrentMonthUsage as CurrentMonthUsage,
    KeyInfo as KeyInfo,
)

class KeyEndpoint(CoinpaprikaAPI):
    async def get_key_info(self): ...
