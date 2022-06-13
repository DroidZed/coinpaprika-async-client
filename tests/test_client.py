import pytest
from pytest_httpx import HTTPXMock

from coinpaprika_async import Client, ResponseObject


@pytest.mark.asyncio
async def test_mock_async_price_conv(httpx_mock: HTTPXMock):
    params = {"base_currency_id": "btc-bitcoin", "quote_currency_id": "usd-us-dollars", "amount": 1337}

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

    client = Client()

    httpx_mock.add_response(json=json)

    response = await client.price_converter(params=params)

    assert response.status_code == 200

    assert response.data is not None

    assert response.data != {}


@pytest.mark.asyncio
async def test_failed_api_call(httpx_mock: HTTPXMock):

    json_obj = {"error": "id not found"}

    client = Client()

    httpx_mock.add_response(json=json_obj, status_code=404)

    response: ResponseObject = await client.coin("eth")

    assert response.status_code == 404
