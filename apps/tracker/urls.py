from django.contrib.auth import views as auth_views
from django.urls import path

from .views.converter import CurrencyConversionView
from .views.cryptocurrency import CryptoCurrencyView
from .views.register_login import register_view, login_view
from .views.transaction import create_transaction, transaction_history
from .views.wallet import WalletCreateView, WalletListView, WalletDetailView

app_name = "tracker"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("create/", WalletCreateView.as_view(), name="wallet_create"),
    path("list/", WalletListView.as_view(), name="wallet_list"),
    path("detail/<int:pk>", WalletDetailView.as_view(), name="wallet_detail"),
    path("wallet/<int:wallet_id>/create_transaction/", create_transaction, name="create_transaction"),
    path("wallet/<int:wallet_id>/history/", transaction_history, name="transaction_history"),
    path("currency_converter/", CurrencyConversionView.as_view(), name="currency_converter"),
    path("cryptocurrency/", CryptoCurrencyView.as_view(), name="cryptocurrency"),
]
