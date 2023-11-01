from django.core.management.base import BaseCommand

from apps.tracker.services.initialize_api_key import initialize_api_key


class Command(BaseCommand):
    def handle(self, *args, **options):
        initialize_api_key()
