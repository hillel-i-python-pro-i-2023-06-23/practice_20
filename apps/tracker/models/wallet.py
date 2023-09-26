from django.contrib.auth import get_user_model
from django.db import models

from .currency import Currency

User = get_user_model()


class Wallet(models.Model):
    # Field for user references
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Name, balance, status, currency
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # Reference to the Currency model

    # Created and modified time fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
