import json

from django.core.cache import cache
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from core.settings import API_KEY


def get_cryptocurrency_info():
    crypto_list = cache.get("crypto_list")

    if crypto_list:
        return crypto_list
    else:
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

        parameters = {"start": "1", "limit": "5000", "convert": "USD"}
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": API_KEY,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            raise e

        data = json.loads(response.text)

        crypto_list = []
        try:
            cryptocurrencies = data["data"]
        except KeyError as e:
            raise e

        for item in cryptocurrencies:
            cryptocurrency = {
                "name": item.get("name"),
                "symbol": item["symbol"],
                "price": item["quote"]["USD"]["price"],
                "percent_change_24h": item["quote"]["USD"]["percent_change_24h"],
                "volume_24h": item["quote"]["USD"]["volume_24h"],
                "volume_change_24h": item["quote"]["USD"]["volume_change_24h"],
            }
            crypto_list.append(cryptocurrency)

        cache.set("crypto_list", crypto_list, 30 * 60)
        return crypto_list
