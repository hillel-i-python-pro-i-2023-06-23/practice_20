from apps.tracker.models import Wallet
from apps.tracker.services.convert_currency import convert_currency


def calculate_total_balance_in_uah(user):
    wallets = Wallet.objects.filter(user=user)
    total_balance_in_uah = 0

    for wallet in wallets:
        if wallet.currency.code == "UAH":
            total_balance_in_uah += wallet.balance
        else:
            converted_balance = convert_currency(wallet.balance, wallet.currency.code, "UAH")
            if converted_balance is not None:
                total_balance_in_uah += converted_balance

    return total_balance_in_uah
