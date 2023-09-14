from django.core.management.base import BaseCommand

from apps.tracker.services.initialize_currency import initialize_currency


class Command(BaseCommand):
    def handle(self, *args, **options):
        initialize_currency()
