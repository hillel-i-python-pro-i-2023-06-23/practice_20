from django.contrib.auth import views as auth_views
from django.urls import path

from .views import register_login

app_name = "tracker"

urlpatterns = [
    path("register/", register_login.register_view, name="register"),
    path("login/", register_login.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
