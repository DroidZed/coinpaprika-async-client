from typing import Dict, Any
from ..coinpaprika_api import CoinpaprikaAPI
from .models import KeyInfo, APIUsage, CurrentMonthUsage


class KeyEndpoint(CoinpaprikaAPI):
    async def get_key_info(self):
        res = await self.internal.call_api("key/info")

        if res.Error:
            return res.Error

        data: Dict[str, Any] = res.Data

        return KeyInfo(
            plan=data["plan"],
            plan_started_at=data["plan_started_at"],
            plan_status=data["plan_status"],
            portal_url=data["portal_url"],
            usage=APIUsage(
                message=data["message"],
                current_month=CurrentMonthUsage(
                    requests_left=data["requests_left"], requests_made=data["requests_made"]
                ),
            ),
        )
