from .models import *
from ..coinpaprika_api import CoinpaprikaAPI as CoinpaprikaAPI

class PeopleEndpoint(CoinpaprikaAPI):
    async def people(self, person_id: str): ...
