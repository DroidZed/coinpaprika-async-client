from ..client import CoinPaprikaAsyncClient

from ..networking_layer import Result, ApiError

from .models import *


class CoinsEndpoint:
    def __init__(self) -> None:
        self.__internal = CoinPaprikaAsyncClient()

    async def get_all(self) -> ApiError | list[CoinItem]:
        res = await self.__internal.call_api("coins")

        if res.Error:
            return res.Error

        return [CoinItem(**e) for e in res.Data]

    async def coin_by_id(self, coin_id: str) -> Result:
        return await self.__internal.call_api(f"coins/{coin_id}")

    async def tweets_of_coin(
        self, coin_id: str
    ) -> ApiError | list[TwitterCoinItem]:
        """Returns the last 50 timeline tweets from the official Twitter profile for a given coin.

        Args:
            coin_id: Required id for the coin
        """
        res = await self.__internal.call_api(f"coins/{coin_id}/twitter")

        if res.Error:
            return res.Error

        return [TwitterCoinItem(**e) for e in res.Data]

    async def events_of_coin(
        self, coin_id: str
    ) -> ApiError | list[EventCoinItem]:
        """Returns events for a given coin.

        Args:
            coin_id: Required id for the coin
        """
        res = await self.__internal.call_api(f"coins/{coin_id}/events")

        if res.Error:
            return res.Error

        return [EventCoinItem(**e) for e in res.Data]

    async def exchanges_of_coin(
        self, coin_id: str
    ) -> ApiError | list[ExchangeCoinItem]:
        """Returns exchanges where a given coin is traded.

        Args:
            coin_id:  Required id for the coin
        """
        res = await self.__internal.call_api(f"coins/{coin_id}/exchanges")

        if res.Error:
            return res.Error

        return [
            ExchangeCoinItem(
                fiats=[Fiat(**f) for f in e["fiats"]],
                id=e["id"],
                name=e["name"],
                adjusted_volume_24h_share=e["adjusted_volume_24h_share"],
            )
            for e in res.Data
        ]

    async def markets_of_coin(
        self, coin_id: str, quotes: str = "USD"
    ) -> ApiError | list[MarketCoinItem]:
        """Returns all available markets for a given coin.

        Args:
            coin_id: Required id for the coin
            quotes: Comma separated list of quotes to return. Currently allowed values: BTC, ETH, USD, EUR, PLN, KRW, GBP, CAD, JPY, RUB, TRY, NZD, AUD, CHF, UAH, HKD, SGD, NGN, PHP, MXN, BRL, THB, CLP, CNY, CZK, DKK, HUF, IDR, ILS, INR, MYR, NOK, PKR, SEK, TWD, ZAR, VND, BOB, COP, PEN, ARS and ISK.
        """
        res = await self.__internal.call_api(
            f"coins/{coin_id}/markets", quotes=quotes
        )

        if res.Error:
            return res.Error

        return [
            MarketCoinItem(
                market_url=m["market_url"],
                outlier=m["outlier"],
                pair=m["pair"],
                quote_currency_id=m["quote_currency_id"],
                quote_currency_name=m["quote_currency_name"],
                quotes={
                    key: QuotesKey(**m["quotes"][key])
                    for key in quotes.split(",")
                },
                last_updated=m["last_updated"],
                fee_type=m["fee_type"],
                exchange_name=m["exchange_name"],
                category=m["category"],
                base_currency_name=m["base_currency_name"],
                base_currency_id=m["base_currency_id"],
                exchange_id=m["exchange_id"],
                adjusted_volume_24h_share=m["adjusted_volume_24h_share"],
            )
            for m in res.Data
        ]

    async def latest_ohlcv(
        self, coin_id: str, quote: str = "usd"
    ) -> ApiError | list[CandleItem]:
        """Returns Open/High/Low/Close values with volume and market capitalization for the last full day.

        Args:
            coin_id: Required id for the coin
            quote: returned data quote (available values: usd & btc).
        """
        res = await self.__internal.call_api(
            f"coins/{coin_id}/ohlcv/latest",
            quote=quote,
        )

        return await self.__candle_handler(res)

    async def historical_ohlcv(
        self,
        coin_id: str,
        start: str,
        end: Optional[str] = None,
        limit: Optional[int] = None,
        interval: Optional[str] = None,
        quote: Optional[str] = None,
    ) -> ApiError | list[CandleItem]:
        """Returns Open/High/Low/Close values with volume and market capitalization for any date range. If the end date is the current day, data can change with every request until actual close of the day at 23:59:59"

        Args:
            coin_id: Required id for the coin
            start: start point for historical data. Supported formats: RFC3999, Simple date (yyyy-mm-dd) & Unix timestamp (in seconds)
            end: end point for ohlcv (max 1 year). Supported formats: same as start date.
            limit: limit of result rows (max 366)
            interval: returned OHLCV point interval (available values: 15m, 30m, 1h, 6h, 12h, 24h)
            quote: returned data quote (available values: usd & btc)
        """
        res = await self.__internal.call_api(
            f"coins/{coin_id}/ohlcv/historical",
            start=start,
            end=end,
            limit=limit,
            interval=interval,
            quote=quote,
        )
        return await self.__candle_handler(res)

    async def ohlcv_of_today(
        self, coin_id: str, quote: str = "usd"
    ) -> ApiError | list[CandleItem]:
        """Returns Open/High/Low/Close values with volume and market capitalization for the current day. Data can change every each request until actual close of the day at 23:59:59.

        Args:
            coin_id: Required id for the coin
            quote: returned data quote (available values: usd & btc)
        """
        res = await self.__internal.call_api(
            f"coins/{coin_id}/ohlcv/today",
            quote=quote,
        )

        return await self.__candle_handler(res)

    async def __candle_handler(
        self, result: Result
    ) -> ApiError | list[CandleItem]:
        if result.Error:
            return result.Error

        return [CandleItem(**c) for c in result.Data]
