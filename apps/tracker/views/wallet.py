from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from apps.tracker.forms.wallet import WalletForm
from apps.tracker.models import Wallet
from apps.tracker.services.calculate_total_balance_in_uah import calculate_total_balance_in_uah


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_balance_in_uah = calculate_total_balance_in_uah(self.request.user)
        context["total_balance_in_uah"] = total_balance_in_uah
        return context


class WalletDetailView(DetailView):
    model = Wallet
    template_name = "tracker/wallet/wallet_detail.html"
    context_object_name = "wallet"

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)
