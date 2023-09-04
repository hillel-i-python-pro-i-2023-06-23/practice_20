from django import forms


class GenerateForm(forms.Form):
    amount = forms.IntegerField(
        label="Amount",
        min_value=1,
        max_value=100,
        required=True,
        initial=12,
    )
