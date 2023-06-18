from typing import Optional
from ..coinpaprika_api import CoinpaprikaAPI


class MiscelanousEndpoints(CoinpaprikaAPI):
    async def people(self, person_id: Optional[str] = None):
        return await self.internal.call_api(f"people/{person_id}")

    async def search(
        self,
        q: str,
        categories: Optional[str] = None,
        modifier: Optional[str] = None,
        limit: Optional[int] = 6,
    ):
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
            _type_: _description_
        """
        return await self.internal.call_api(
            "search",
            q=q,
            c=categories,
            modifier=modifier,
            limit=limit,
        )

    async def price_converter(self, params: Optional[dict] = None):
        return await self.internal.call_api("price-converter", params)
