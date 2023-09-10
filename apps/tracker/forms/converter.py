from django import forms

from apps.tracker.services.convert_currency import get_exchange_data, convert_currency


class CurrencyConversionForm(forms.Form):
    amount = forms.DecimalField(label="Amount", max_digits=15, decimal_places=2, min_value=1)
    from_currency = forms.ChoiceField(label="From currency", choices=[], initial="UAH")
    to_currency = forms.ChoiceField(label="To currency", choices=[], initial="USD")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the exchange data from the service
        exchange_data = get_exchange_data()
        # Create a list of currencies and their rates
        currency_rates = []
        for currency in exchange_data:
            currency_rates.append((currency["cc"], currency["cc"]))
        if not any(currency["cc"] == "UAH" for currency in exchange_data):
            # Add UAH with a fixed rate
            currency_rates.append(("UAH", "UAH"))
        # Set the choices for the currency fields
        self.fields["from_currency"].choices = currency_rates
        self.fields["to_currency"].choices = currency_rates
        self.fields["amount"].widget.attrs.update({"class": "form-input"})

    def clean(self):
        # Get the cleaned data from the form
        cleaned_data = super().clean()
        amount = float(cleaned_data.get("amount"))
        from_currency = cleaned_data.get("from_currency")
        to_currency = cleaned_data.get("to_currency")
        # Convert the amount using the service
        converted_amount = convert_currency(amount, from_currency, to_currency)
        # Add the converted amount to the cleaned data
        cleaned_data["converted_amount"] = converted_amount
        return cleaned_data
