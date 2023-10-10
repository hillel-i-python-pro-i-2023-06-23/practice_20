from celery import shared_task
from apps.tracker.services.convert_currency import get_exchange_data


@shared_task
def update_currency_exchange():
    get_exchange_data()
