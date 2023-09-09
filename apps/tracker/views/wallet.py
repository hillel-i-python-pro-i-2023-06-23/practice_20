from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from apps.tracker.forms.wallet import WalletForm
from apps.tracker.models import Wallet
from apps.tracker.services.convert_currency import convert_currency, get_exchange_data


class WalletCreateView(CreateView):
    model = Wallet
    form_class = WalletForm
    template_name = "tracker/wallet/create_wallet.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("tracker:wallet_list")


class WalletListView(ListView):
    model = Wallet
    template_name = "tracker/wallet/wallet_list.html"
    context_object_name = "wallets"

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)


class WalletDetailView(DetailView):
    model = Wallet
    template_name = "tracker/wallet/wallet_detail.html"
    context_object_name = "wallet"

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Get the exchange data from the service
        exchange_data = get_exchange_data()
        # Create a list of currencies and their rates
        currency_rates = []
        for currency in exchange_data:
            currency_rates.append((currency["cc"], currency["rate"]))
        # Add the currency rates to the context
        context["currency_rates"] = currency_rates
        return context

    def post(self, request, *args, **kwargs):
        # Get the wallet object
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        # Get the data from the form
        amount = float(request.POST.get("amount"))
        from_currency = request.POST.get("from_currency")
        to_currency = request.POST.get("to_currency")
        # Convert the amount using the service
        converted_amount = convert_currency(amount, from_currency, to_currency)
        # Add the converted amount to the context
        context = self.get_context_data(**kwargs)
        context["amount"] = amount
        context["from_currency"] = from_currency
        context["converted_amount"] = converted_amount
        context["to_currency"] = to_currency
        return self.render_to_response(context)
