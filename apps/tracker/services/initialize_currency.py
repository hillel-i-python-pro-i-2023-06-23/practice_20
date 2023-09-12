from apps.tracker.models import Currency


def initialise_currency():
    currencys = [
        {"code": "UAH", "name": "hryvnia"},
        {"code": "USD", "name": "dollar"},
        {"code": "EUR", "name": "euro"},
    ]
    for currency in currencys:
        Currency.objects.get_or_create(**currency)
