import pytest
from pytest_httpx import HTTPXMock

from coinpaprika_async import MiscelanousEndpoints, CoinsEndpoint, ApiError


class TestClient:
    @pytest.mark.asyncio
    async def test_mock_async_price_conv(self, httpx_mock: HTTPXMock):
        params = {
            "base_currency_id": "btc-bitcoin",
            "quote_currency_id": "usd-us-dollars",
            "amount": 1337,
        }

        json = {
            "base_currency_id": "btc-bitcoin",
            "base_currency_name": "Bitcoin",
            "base_price_last_updated": "2022-01-16T23:46:14Z",
            "quote_currency_id": "xmr-monero",
            "quote_currency_name": "Monero",
            "quote_price_last_updated": "2022-01-16T23:46:14Z",
            "amount": 12.2,
            "price": 2336.6037613108747,
        }

        api = MiscelanousEndpoints()

        httpx_mock.add_response(json=json)

        response = await api.price_converter(**params)

        assert not isinstance(response, ApiError)

    @pytest.mark.asyncio
    async def test_should_give_proper_coins(self):
        coins_api = CoinsEndpoint()

        resp = await coins_api.get_all()

        if isinstance(resp, ApiError):
            assert False

        assert len(resp) != 0

    @pytest.mark.asyncio
    async def test_failed_api_call(self, httpx_mock: HTTPXMock):
        json_obj = {"error": "id not found"}

        coins_api = CoinsEndpoint()

        httpx_mock.add_response(json=json_obj, status_code=404)

        response = await coins_api.coin_by_id("eth")

        if response.Error:
            assert response.Error.error == json_obj["error"]

    @pytest.mark.asyncio
    async def test_for_markets(self):
        coins_api = CoinsEndpoint()

        response = await coins_api.markets_of_coin("btc-bitcoin")

        if isinstance(response, ApiError):
            assert False

        assert len(response)
