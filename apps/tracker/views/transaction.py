from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.tracker.forms.transaction import TransactionForm
from apps.tracker.models import Wallet, Transaction


@login_required
def create_transaction(request, wallet_id):
    wallet = Wallet.objects.get(id=wallet_id, user=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.wallet = wallet

            amount = form.cleaned_data["amount"]
            if wallet.balance >= amount:
                wallet.balance -= amount
                wallet.save()
                transaction.save()
                return redirect("tracker:wallet_detail", wallet_id)
            else:
                messages.error(request, "Not enough money for transaction in current wallet")
        else:
            messages.error(request, "Incorrect form")
    else:
        form = TransactionForm()

    return render(request, "tracker/wallet/transaction_create.html", {"form": form, "wallet": wallet})


@login_required()
def transaction_history(request, wallet_id):
    wallet = Wallet.objects.get(id=wallet_id, user=request.user)
    transactions = Transaction.objects.filter(wallet=wallet).order_by("-date")
    return render(request, "tracker/wallet/transaction_history.html", {"wallet": wallet, "transactions": transactions})
