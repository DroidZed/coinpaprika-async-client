from typing import Optional, Any, Dict, List

from ..client import CoinPaprikaAsyncClient

from ..networking_layer import ApiError

from .models import *


class MiscellaneousEndpoints:
    def __init__(self) -> None:
        self.__internal = CoinPaprikaAsyncClient()

    async def people(self, person_id: str) -> ApiError | list[PeopleModel]:
        res = await self.__internal.call_api(f"people/{person_id}")

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            PeopleModel(
                id=p["id"],
                name=p["name"],
                description=p["description"],
                teams_count=p["teams_count"],
                links=MiscLinks(
                    additional=[
                        MiscSocial(**s) for s in p["links"]["additional"]
                    ],
                    github=[MiscSocial(**s) for s in p["links"]["github"]],
                    linkedin=[MiscSocial(**s) for s in p["links"]["linkedin"]],
                    medium=[MiscSocial(**s) for s in p["links"]["medium"]],
                    twitter=[MiscSocial(**s) for s in p["links"]["twitter"]],
                ),
                positions=[MiscPosition(**pos) for pos in p["positions"]],
            )
            for p in data
        ]

    async def search(
        self,
        q: str,
        categories: Optional[str] = None,
        modifier: Optional[str] = None,
        limit: Optional[int] = 6,
    ) -> ApiError | list[SearchResult]:
        """Returns currencies, exchanges, icos, people, tags on coinpaprika.com for a given search query.

        Available on the following API plans:

           * Free
           * Starter
           * Pro
           * Business
           * Enterprise

        Args:
            q (str): _phrase for search eg. btc_.
            categories: Available options: currencies|exchanges|icos|people|tags.
            modifier: Available options: symbol_search - search only by symbol (works for currencies only).
            limit: Limit of results per category (max 250) Defaults to 6.

        Returns:
            A list of the search result items.
        """
        res = await self.__internal.call_api(
            "search",
            q=q,
            c=categories,
            modifier=modifier,
            limit=limit,
        )
        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            SearchResult(
                currencies=[Currency(**c) for c in s["currencies"]],
                icos=[Ico(**i) for i in s["icos"]],
                exchanges=[MiscExchange(**e) for e in s["exchanges"]],
                people=[Person(**p) for p in s["people"]],
                tags=[Tag(**t) for t in s["tags"]],
            )
            for s in data
        ]

    async def price_converter(
        self,
        base_currency_id: str,
        quote_currency_id: str,
        amount: Optional[int] = 0,
    ) -> ApiError | ConvertResult:
        res = await self.__internal.call_api(
            "price-converter",
            base_currency_id=base_currency_id,
            quote_currency_id=quote_currency_id,
            amount=amount,
        )

        if res.Error:
            return res.Error

        data: Dict[str, Any] = res.Data

        return ConvertResult(**data)
