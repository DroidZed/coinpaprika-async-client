[![Documentation Status](https://readthedocs.org/projects/coinpaprika-async-client/badge/?version=latest)](https://coinpaprika-async-client.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Coinpaprika API Python Async Client

## Usage

This library provides convenient and modern way to use [coinpaprika.com](https://api.coinpaprika.com/) API in Python.

[Coinpaprika](https://coinpaprika.com/) delivers full market data to the world of crypto: coin prices, volumes, market caps, ATHs, return rates and more.

## Requirements

```sh
pip install coinpaprika_async
```

Or:

```sh
pipenv install coinpaprika_async
```

## Getting started

```py
from coinpaprika_async import Client

client = Client()
```

## Examples and Docs
Check out the [examples](./examples) directory.

## Tests

```test
pip install -r requirements-dev.txt

pytest tests/test_client.py
```

## License
CoinpaprikaAPI is available under the MIT license. See the LICENSE file for more info.
