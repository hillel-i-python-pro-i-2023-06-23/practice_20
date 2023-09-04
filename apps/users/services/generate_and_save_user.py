import logging

from apps.users.models import User
from apps.users.services.faker_init import faker


def generate_and_save_user(amount: int):
    logger = logging.getLogger("django")

    queryset = User.objects.all()

    logger.info(f"Current amount of contacts before: {queryset.count()}")

    for _ in range(amount):
        User.objects.create(
            name=faker.unique.user_name(), email=faker.unique.company_email(), password=faker.unique.password()
        )

    logger.info(f"Current amount of contacts after: {queryset.count()}")
