from typing import Optional, List, Dict, Any
from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class CoinsEndpoint(CoinpaprikaAPI):
    async def coins(self):
        res = await self.internal.call_api("coins")

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [CoinItem(**e) for e in data]

    async def coin(self, coin_id: str):
        return await self.internal.call_api(f"coins/{coin_id}")

    async def twitter(self, coin_id: str):
        res = await self.internal.call_api(f"coins/{coin_id}/twitter")

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [TwitterCoinItem(**e) for e in data]

    async def events(self, coin_id: str):
        res = await self.internal.call_api(f"coins/{coin_id}/events")

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [EventCointItem(**e) for e in data]

    async def exchanges(self, coin_id: str):
        res = await self.internal.call_api(f"coins/{coin_id}/exchanges")

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            ExchangeCoinItem(
                fiats=[Fiat(**f) for f in e["fiats"]],
                id=e["id"],
                name=e["name"],
                adjusted_volume_24h_share=e["adjusted_volume_24h_share"],
            )
            for e in data
        ]

    async def markets(self, coin_id: str, quotes: str = "USD"):
        res = await self.internal.call_api(f"coins/{coin_id}/markets", quotes=quotes)

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            MarketCoinItem(
                market_url=m["market_url"],
                outlier=m["outlier"],
                pair=m["pair"],
                quote_currency_id=m["quote_currency_id"],
                quote_currency_name=m["quote_currency_name"],
                quotes={key: Key(**m["quotes"][key]) for key in quotes.split(",")},
                last_updated=m["last_updated"],
                fee_type=m["fee_type"],
                exchange_name=m["exchange_name"],
                category=m["category"],
                base_currency_name=m["base_currency_name"],
                base_currency_id=m["base_currency_id"],
                exchange_id=m["exchange_id"],
                adjusted_volume_24h_share=m["adjusted_volume_24h_share"],
            )
            for m in data
        ]

    async def candle(self, coin_id: str, quote: str = "usd"):
        res = await self.internal.call_api(
            f"coins/{coin_id}/ohlcv/latest",
            quote=quote,
        )

        return self.__candle_handler(res)

    async def candles(
        self,
        coin_id: str,
        start: str,
        end: Optional[str] = None,
        limit: Optional[int] = None,
        interval: Optional[str] = None,
        quote: Optional[str] = None,
    ):
        res = await self.internal.call_api(
            f"coins/{coin_id}/ohlcv/historical",
            start=start,
            end=end,
            limit=limit,
            interval=interval,
            quote=quote,
        )
        return self.__candle_handler(res)

    async def today(self, coin_id: str, quote: str = "usd"):
        res = await self.internal.call_api(
            f"coins/{coin_id}/ohlcv/today",
            quote=quote,
        )

        return self.__candle_handler(res)

    async def __candle_handler(self, res: Any):
        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [CandleItem(**c) for c in data]
