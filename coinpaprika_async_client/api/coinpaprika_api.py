from typing import Optional
from .networking_layer import CoinPaprikaAsyncClient


class CoinpaprikaAPI:
    def __init__(self) -> None:
        self.internal = CoinPaprikaAsyncClient()
