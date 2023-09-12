from django import forms

from apps.tracker.models import Wallet


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ("name", "balance", "currency")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-input"})
        self.fields["balance"].widget.attrs.update({"class": "form-input"})
        self.fields["currency"].widget.attrs.update({"class": "form-input"})
