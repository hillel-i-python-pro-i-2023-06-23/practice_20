from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from apps.users.forms import UserForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("base:home_page")  # Redirect to homepage after create new User
    else:
        form = UserForm()
    return render(request, "tracker/registration/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("base:home_page")  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, "tracker/registration/login.html", {"form": form})
