from django import forms

from apps.tracker.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("wallet", "description", "amount")
