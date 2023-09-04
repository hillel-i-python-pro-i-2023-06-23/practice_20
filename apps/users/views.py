from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.users.forms import GenerateForm
from apps.users.models import User
from apps.users.services.delete_users import delete_users
from apps.users.services.generate_and_save_user import generate_and_save_user


class UsersListView(ListView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = (
        "name",
        "email",
        "password",
    )

    success_url = reverse_lazy("users:user_list")


class UserUpdateView(UpdateView):
    model = User
    fields = (
        "name",
        "email",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context

    success_url = reverse_lazy("users:user_list")


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("users:user_list")


def generate_users_view(request):
    if request.method == "POST":
        form = GenerateForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data["amount"]

            generate_and_save_user(amount=amount)
    else:
        form = GenerateForm()

    return render(
        request=request,
        template_name="users/users_generate.html",
        context=dict(
            users_list=User.objects.all(),
            form=form,
        ),
    )


def delete_users_view(request):
    delete_users()

    return redirect(reverse_lazy("users:user_list"))
