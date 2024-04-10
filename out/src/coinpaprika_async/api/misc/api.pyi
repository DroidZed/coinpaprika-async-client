from .models import *
from ..coinpaprika_api import CoinpaprikaAPI as CoinpaprikaAPI

class MiscellaneousEndpoints(CoinpaprikaAPI):
    async def people(self, person_id: str): ...
    async def search(
        self,
        q: str,
        categories: str | None = None,
        modifier: str | None = None,
        limit: int | None = 6,
    ): ...
    async def price_converter(
        self,
        base_currency_id: str,
        quote_currency_id: str,
        amount: int | None = 0,
    ): ...
