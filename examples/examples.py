from asyncio import run

from coinpaprika_async import (
    CoinsEndpoint,
    ExchangesEndpoint,
    KeyEndpoint,
    MarketEndpoint,
    MiscellaneousEndpoints,
    TagsEndpoint,
    PeopleEndpoint,
    TickersEndpoint,
)


# List coins
async def list_coins(client: CoinsEndpoint):
    print(await client.get_all())


# Get coin by ID (example: btc-bitcoin)
async def find_coin_by_id(client: CoinsEndpoint, c_id: str):
    print(await client.coin_by_id(c_id))


# Get tweets by coin ID (max 50 tweets)
async def get_tweets_by_coin_id(client: CoinsEndpoint):
    print(await client.tweets_of_coin("btc-bitcoin"))


# Get coin events by coin ID
async def get_events_by_coin_id(client: CoinsEndpoint):
    print(await client.events_of_coin("btc-bitcoin"))


# Get exchanges by coin ID
async def get_exchanges_by_coin_id(client: CoinsEndpoint):
    print(await client.exchanges_of_coin("btc-bitcoin"))


# Get markets by coin ID (USD,BTC,ETH,PLN)
async def get_markets_by_coin_id(client: CoinsEndpoint):
    print(await client.markets_of_coin("btc-bitcoin", quotes="USD"))


# Get 24h OHLC candle (USD,BTC)
async def get_24h_ohlc(client: CoinsEndpoint):
    print(await client.latest_ohlcv("btc-bitcoin"))


# Get historical OHLCV information for a specific coin (USD,BTC)
async def get_hist_ohlcv(client: CoinsEndpoint):
    print(
        await client.historical_ohlcv(
            "btc-bitcoin", start="2019-01-11T00:00:00Z"
        )
    )


# Get today OHLC (can change every each request until actual close of the day at 23:59:59)
async def get_today_ohl(client: CoinsEndpoint):
    print(await client.ohlcv_of_today("btc-bitcoin"))


# Get people by ID (example: vitalik-buterin)
async def get_people_by_id(client: MiscellaneousEndpoints):
    print(await client.people("vitalik-buterin"))


# List tags
async def list_tags(client: TagsEndpoint):
    print(await client.tags())


async def list_tags_additonal_fields(client: TagsEndpoint):
    print(await client.tags(additional_fields="coins,icos"))


# Get tag by ID
async def get_tag_by_id(client: TagsEndpoint):
    print(await client.tag("blockchain-service"))


# Get tickers for all coins (USD,BTC,ETH)
async def get_all_tickers(client: TickersEndpoint):
    print(await client.tickers())


# Get ticker information for a specific coin (USD,BTC,ETH)
async def get_ticker_by_coin(client: TickersEndpoint):
    print(await client.ticker_by_coin("btc-bitcoin"))


# Get historical ticker information for a specific coin (USD,BTC,ETH)
async def get_historical_information(client: TickersEndpoint):
    print(
        await client.historical_ticks(
            "btc-bitcoin", start="2019-04-11T00:00:00Z"
        )
    )


# List exchanges
async def get_echange_list(client: ExchangesEndpoint):
    print(await client.exchange_list())


# Get exchange by ID
async def exchange_currencies(client: ExchangesEndpoint):
    print(await client.exchange("binance", {"quotes": "USD"}))


# Get markets by exchange ID (USD,BTC,ETH,PLN) with quotes USD
async def exchg_markers_by_id(client: ExchangesEndpoint):
    print(await client.exchange_markets("binance", {"quotes": "USD"}))


# Search
async def search_curr(client: MiscellaneousEndpoints):
    print(
        await client.search(
            q="btc",
            categories="currencies,exchanges,icos,people,tags",
            modifier="symbol_search",
            limit=42,
        )
    )


# Price converter
async def convt_curr(client: MiscellaneousEndpoints):
    print(
        await client.price_converter(
            base_currency_id="btc-bitcoin",
            quote_currency_id="usd-us-dollars",
            amount=1337,
        )
    )


if __name__ == "__main__":
    run(find_coin_by_id(CoinsEndpoint(), "btc"))
