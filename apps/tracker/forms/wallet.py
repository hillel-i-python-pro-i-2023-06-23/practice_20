from django import forms

from apps.tracker.models import Wallet


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ("name", "balance", "currency")
