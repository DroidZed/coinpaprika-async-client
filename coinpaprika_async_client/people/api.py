from typing import Any, Dict, List

from ..client import CoinPaprikaAsyncClient

from ..networking_layer import ApiError

from .models import *


class PeopleEndpoint:
    def __init__(self) -> None:
        self.__internal = CoinPaprikaAsyncClient()

    async def people(self, person_id: str) -> ApiError | list[PeopleItem]:
        res = await self.__internal.call_api(f"people/{person_id}")

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            PeopleItem(
                id=p["id"],
                name=p["name"],
                description=p["description"],
                teams_count=p["teams_count"],
                links=PeopleLinks(
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
