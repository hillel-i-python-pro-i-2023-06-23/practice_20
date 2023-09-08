from django.contrib import admin

from apps.tracker.models.currency import Currency
from apps.tracker.models.wallet import Wallet

# Register your models here.

admin.site.register(Currency)
admin.site.register(Wallet)
