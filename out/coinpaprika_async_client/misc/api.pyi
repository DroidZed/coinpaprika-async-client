from .models import *
from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError

class MiscellaneousEndpoints:
    def __init__(self) -> None: ...
    async def people(self, person_id: str) -> ApiError | list[PeopleModel]: ...
    async def search(
        self,
        q: str,
        categories: str | None = None,
        modifier: str | None = None,
        limit: int | None = 6,
    ) -> ApiError | list[SearchResult]: ...
    async def price_converter(
        self,
        base_currency_id: str,
        quote_currency_id: str,
        amount: int | None = 0,
    ) -> ApiError | ConvertResult: ...
