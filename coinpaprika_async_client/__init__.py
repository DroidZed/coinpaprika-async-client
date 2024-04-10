from .__version__ import __title__, __description__, __version__

from .coins import *
from .exchanges import *
from .key import *
from .market import *
from .people import *
from .misc import *
from .tags import *
from .tickers import *


__all__ = [
    "__description__",
    "__title__",
    "__version__",
    "CoinsEndpoint",
    "ExchangesEndpoint",
    "KeyEndpoint",
    "MarketEndpoint",
    "MiscellaneousEndpoints",
    "PeopleEndpoint",
    "TagsEndpoint",
    "TickersEndpoint",
    "ApiError",
]
