from django.contrib.auth import views as auth_views
from django.urls import path

from .views.register_login import register_view, login_view
from .views.wallet import WalletCreateView, WalletListView, WalletDetailView

app_name = "tracker"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("create/", WalletCreateView.as_view(), name="wallet_create"),
    path("list/", WalletListView.as_view(), name="wallet_list"),
    path("detail/<int:pk>", WalletDetailView.as_view(), name="wallet_detail"),
]
