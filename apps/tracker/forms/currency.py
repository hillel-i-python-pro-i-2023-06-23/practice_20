from django import forms
from apps.tracker.models.currency import Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ["code", "name"]
