from .models import *
from ..client import CoinPaprikaAsyncClient as CoinPaprikaAsyncClient
from ..networking_layer import ApiError as ApiError

class TagsEndpoint:
    def __init__(self) -> None: ...
    async def tags(
        self, additional_fields: str | None = None
    ) -> ApiError | list[Tag]: ...
    async def tag(
        self, tag_id: str, additional_fields: str | None = None
    ) -> ApiError | Tag: ...
