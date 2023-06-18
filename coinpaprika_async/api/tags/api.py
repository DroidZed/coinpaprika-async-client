from typing import Dict, List, Any, Optional
from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class TagsEndpoint(CoinpaprikaAPI):
    async def tags(self, params: Optional[dict] = None):
        return await self.internal.call_api("tags", params)

    async def tag(self, tag_id: str, params: Optional[dict] = None):
        return await self.internal.call_api(f"tags/{tag_id}", params)
