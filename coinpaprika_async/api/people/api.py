from typing import Any, Dict, List
from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class PeopleEndpoint(CoinpaprikaAPI):
    async def people(self, person_id: str):
        res = await self.internal.call_api(f"people/{person_id}")

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            PeopleItem(
                id=p["id"],
                name=p["name"],
                description=p["description"],
                teams_count=p["teams_count"],
                links=Links(
                    additional=[Social(**s) for s in p["links"]["additional"]],
                    github=[Social(**s) for s in p["links"]["github"]],
                    linkedin=[Social(**s) for s in p["links"]["linkedin"]],
                    medium=[Social(**s) for s in p["links"]["medium"]],
                    twitter=[Social(**s) for s in p["links"]["twitter"]],
                ),
                positions=[Position(**pos) for pos in p["positions"]],
            )
            for p in data
        ]
