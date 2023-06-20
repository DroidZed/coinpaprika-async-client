from typing import Optional
from ..coinpaprika_async_client import CoinPaprikaAsyncClient


class CoinpaprikaAPI:
    def __init__(self, client: CoinPaprikaAsyncClient = CoinPaprikaAsyncClient()):
        self.internal = client
