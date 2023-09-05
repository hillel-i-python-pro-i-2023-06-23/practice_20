from django.contrib import admin

# Register your models here.
from apps.tracker.models.currency import Currency

admin.site.register(Currency)
