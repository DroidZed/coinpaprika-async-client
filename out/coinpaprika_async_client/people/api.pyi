from .models import *
from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError

class PeopleEndpoint:
    def __init__(self) -> None: ...
    async def people(self, person_id: str) -> ApiError | list[PeopleItem]: ...
