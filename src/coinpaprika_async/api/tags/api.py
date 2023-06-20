from typing import Dict, List, Any, Optional
from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class TagsEndpoint(CoinpaprikaAPI):
    async def tags(self, additional_fields: Optional[str] = None):
        res = await self.internal.call_api("tags", additional_fields=additional_fields)

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [Tag(**t) for t in data]

    async def tag(self, tag_id: str, additional_fields: Optional[str] = None):
        res = await self.internal.call_api(f"tags/{tag_id}", additional_fields=additional_fields)

        if res.Error:
            return res.Error

        data: Dict[str, Any] = res.Data

        return Tag(**data)
