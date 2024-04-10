from .__version__ import __title__, __description__, __version__

from .api import (
    CoinPaprikaAsyncClient,
    CoinpaprikaAPI,
    CoinsEndpoint,
    ExchangesEndpoint,
    KeyEndpoint,
    MarketEndpoint,
    MiscellaneousEndpoints,
    PeopleEndpoint,
    TagsEndpoint,
    TickersEndpoint,
    ApiError,
    Result,
)

__all__ = [
    "__description__",
    "__title__",
    "__version__",
    "CoinPaprikaAsyncClient",
    "CoinpaprikaAPI",
    "CoinsEndpoint",
    "ExchangesEndpoint",
    "KeyEndpoint",
    "MarketEndpoint",
    "MiscellaneousEndpoints",
    "PeopleEndpoint",
    "TagsEndpoint",
    "TickersEndpoint",
    "ApiError",
    "Result",
]
