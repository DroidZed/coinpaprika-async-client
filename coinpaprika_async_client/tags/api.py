from typing import Dict, List, Any, Optional

from ..client import CoinPaprikaAsyncClient

from ..networking_layer import ApiError

from .models import *


class TagsEndpoint:
    def __init__(self) -> None:
        self.__internal = CoinPaprikaAsyncClient()

    async def tags(
        self, additional_fields: Optional[str] = None
    ) -> ApiError | list[TagModel]:
        res = await self.__internal.call_api(
            "tags", additional_fields=additional_fields
        )

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [TagModel(**t) for t in data]

    async def tag(
        self, tag_id: str, additional_fields: Optional[str] = None
    ) -> ApiError | TagModel:
        res = await self.__internal.call_api(
            f"tags/{tag_id}", additional_fields=additional_fields
        )

        if res.Error:
            return res.Error

        data: Dict[str, Any] = res.Data

        return TagModel(**data)
