[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Coinpaprika API Python Asynchronous Client

## 1. Usage

This library provides convenient and modern way to use [coinpaprika.com](https://api.coinpaprika.com/) API in Python.

[Coinpaprika](https://coinpaprika.com/) delivers full market data to the world of crypto: coin prices, volumes, market caps, ATHs, return rates and more.

## 2. Requirements

```sh
pip install coinpaprika_async
```

Or:

```sh
pipenv install coinpaprika_async
```

## 3. Getting started

```py
from coinpaprika_async import Client

client = Client()
```

## 4 Examples:

Check out the [examples](./examples) directory.

## 5. Tests

```test
pip install -r requirements-dev.txt

pytest tests/test_client.py
```

## 6. License
CoinpaprikaAPI is available under the MIT license. See the LICENSE file for more info.
