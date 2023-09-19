from django.db import models

from apps.tracker.models import Wallet


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
