from django.core.management.base import BaseCommand

from apps.users.services.generate_and_save_user import generate_and_save_user


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help="How many users do you want to generate?",
            default=12,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        generate_and_save_user(amount=amount)
