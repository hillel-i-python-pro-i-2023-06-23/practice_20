from django import forms

from apps.tracker.services.convert_currency import get_currencys


class CurrencyConversionForm(forms.Form):
    amount = forms.DecimalField(label="Amount", max_digits=15, decimal_places=2, min_value=1)
    from_currency = forms.ChoiceField(label="From currency", choices=get_currencys(), initial="UAH")
    to_currency = forms.ChoiceField(label="To currency", choices=get_currencys(), initial="USD")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["amount"].widget.attrs.update({"class": "form-input"})
