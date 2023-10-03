import requests
from decimal import Decimal
from django.core.cache import cache


def get_exchange_data():
    """Get exchange data from NBU website"""
    exchange_data = cache.get("exchange_data")

    if exchange_data is None:
        # We request data on exchange rates from the NBU website
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.get(url)
        if response.status_code == 200:
            exchange_data = response.json()
            cache.set("exchange_data", exchange_data, 60 * 60)

    return exchange_data


def get_currencys():
    exchange_data = get_exchange_data()
    # Create a list of currencies and their rates
    currency_list = []
    for currency in exchange_data:
        currency_list.append((currency["cc"], currency["cc"]))
    if not any(currency["cc"] == "UAH" for currency in exchange_data):
        # Add UAH with a fixed rate
        currency_list.append(("UAH", "UAH"))
    return currency_list


def get_currency_rates(from_currency, to_currency, exchange_data):
    """Get the currency rates"""
    from_rate = None
    to_rate = None

    if from_currency == "UAH":
        from_rate = 1
    if to_currency == "UAH":
        to_rate = 1

    for currency in exchange_data:
        if currency["cc"] == from_currency and from_rate is None:
            from_rate = currency["rate"]
        elif currency["cc"] == to_currency:
            to_rate = currency["rate"]

        if from_rate is not None and to_rate is not None:
            break

    return from_rate, to_rate


def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    exchange_data = get_exchange_data()

    if exchange_data:
        from_rate, to_rate = get_currency_rates(from_currency, to_currency, exchange_data)

        if from_rate is not None and to_rate is not None:
            # Transformation in decimal.Decimal
            amount_decimal = Decimal(str(amount))
            from_rate_decimal = Decimal(str(from_rate))
            to_rate_decimal = Decimal(str(to_rate))

            # Calculate
            converted_amount = amount_decimal * (from_rate_decimal / to_rate_decimal)

            # Return result in Decimal format
            return round(converted_amount, 2)
        else:
            return None  # Not currency is found
    else:
        return None  # Error
