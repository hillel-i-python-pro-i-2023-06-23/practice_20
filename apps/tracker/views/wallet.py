from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from apps.tracker.forms.wallet import WalletForm
from apps.tracker.models import Wallet


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
