from django.db import models
from django.contrib.auth.models import User

from apps.tracker.models.currency import Currency


class Wallet(models.Model):
    # Field for user references
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Name, balance, status, currency
    name = models.CharField(max_length=255)
    balance = models.IntegerField()  # Use integers for cents
    status = models.BooleanField(default=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # Reference to the Currency model

    # Created and modified time fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
