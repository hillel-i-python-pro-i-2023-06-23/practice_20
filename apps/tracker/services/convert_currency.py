import requests


def get_exchange_data():
    """Get exchange data from NBU website"""
    # We request data on exchange rates from the NBU website
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    return None


def get_currency_rates(from_currency, to_currency, exchange_data):
    """Get the currency rates"""
    from_rate = None
    to_rate = None

    if from_currency == "UAH":
        from_rate = 1

    for currency in exchange_data:
        if currency["cc"] == from_currency and from_rate is None:
            from_rate = currency["rate"]
        elif currency["cc"] == to_currency:
            to_rate = currency["rate"]

        if from_rate is not None and to_rate is not None:
            break

    return from_rate, to_rate


def convert_currency(amount, from_currency, to_currency):
    """
    Convert currency amount

    # Usage example:
    amount_in_usd = 100  # Amount in USD
    new_currency = 'EUR'  # New currency

    converted_amount = convert_currency(amount_in_usd, 'USD', new_currency)
    if converted_amount is not None:
        print(f'{amount_in_usd} USD equals {converted_amount} {new_currency}')
    else:
    print('Conversion failed.')
    """

    if from_currency == to_currency:
        return amount

    exchange_data = get_exchange_data()

    if exchange_data:
        # We are looking for rates of the required currencies
        from_rate, to_rate = get_currency_rates(from_currency, to_currency, exchange_data)

        if from_rate is not None and to_rate is not None:
            # Recalculate the amount
            return round(amount * (from_rate / to_rate), 2)
        else:
            return None  # Currencies not found in data
    else:
        return None  # Request error


# if __name__ == "__main__":
#     amount_in_usd = 100  # Amount in USD
#     new_currency = 'EUR'  # New currency
#
#     converted_amount = convert_currency(amount_in_usd, 'USD', new_currency)
#     if converted_amount is not None:
#         print(f'{amount_in_usd} USD equals {converted_amount} {new_currency}')
#     else:
#         print('Conversion failed.')
