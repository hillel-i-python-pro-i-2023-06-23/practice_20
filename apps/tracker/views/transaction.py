# import geoip2.database
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from apps.tracker.forms.transaction import TransactionForm
from apps.tracker.models import Wallet, Transaction

# from apps.tracker.services.timezone_check import get_timezone_by_city
# from core.settings import GEOIP_DATABASE


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

    # # checking user ID
    # user_ip = request.META.get("REMOTE_ADDR")
    #
    # with geoip2.database.Reader(GEOIP_DATABASE.joinpath('GeoLite2-City.mmdb')) as reader:
    #     response = reader.city(user_ip)
    #
    # user_timezone = get_timezone_by_city(response.city.name)
    #
    # request.session["user_timezone"] = user_timezone

    # Getting filter parameters
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    search = request.GET.get("search")

    transactions = Transaction.objects.filter(wallet=wallet).order_by("-date")

    if start_date:
        transactions = transactions.filter(date__gte=start_date)

    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    if search:
        transactions = transactions.filter(Q(description__icontains=search) | Q(amount__icontains=search))

    return render(
        request,
        "tracker/wallet/transaction_history.html",
        {
            "wallet": wallet,
            "transactions": transactions,
            "start_date": start_date,
            "end_date": end_date,
            "search": search,
        },
    )
