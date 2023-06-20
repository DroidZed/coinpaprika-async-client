from typing import Optional, List, Dict, Any
from ..coinpaprika_api import CoinpaprikaAPI
from .models import *


class TickersEndpoint(CoinpaprikaAPI):
    async def tickers(self, quotes: str = "USD"):
        res = await self.internal.call_api("tickers", quotes=quotes)
        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            TickerItem(
                id=tc["id"],
                name=tc["name"],
                symbol=tc["symbol"],
                rank=tc["rank"],
                circulating_supply=tc["circulating_supply"],
                total_supply=tc["total_supply"],
                max_supply=tc["max_supply"],
                beta_value=tc["beta_value"],
                first_data_at=tc["first_data_at"],
                last_updated=tc["last_updated"],
                quotes={t: Quote(**v) for t, v in tc["quotes"]},
            )
            for tc in data
        ]

    async def ticker_by_coin(self, coin_id: str, quotes: str = "USD"):
        res = await self.internal.call_api(f"tickers/{coin_id}", quotes=quotes)

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [
            TickerItem(
                id=tc["id"],
                name=tc["name"],
                symbol=tc["symbol"],
                rank=tc["rank"],
                circulating_supply=tc["circulating_supply"],
                total_supply=tc["total_supply"],
                max_supply=tc["max_supply"],
                beta_value=tc["beta_value"],
                first_data_at=tc["first_data_at"],
                last_updated=tc["last_updated"],
                quotes={t: Quote(**v) for t, v in tc["quotes"]},
            )
            for tc in data
        ]

    async def historical_ticks(
        self,
        coin_id: str,
        start: str,
        end: str = "NOW",
        limit: Optional[int] = 1000,
        quotes: str = "USD",
        interval: str = "5m",
    ):
        res = await self.internal.call_api(
            f"tickers/{coin_id}/historical",
            start=start,
            end=end,
            limit=limit,
            interval=interval,
            quotes=quotes,
        )

        if res.Error:
            return res.Error

        data: List[Dict[str, Any]] = res.Data

        return [HistoryTickerItem(**ht) for ht in data]
