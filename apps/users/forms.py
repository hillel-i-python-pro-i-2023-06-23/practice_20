from django.contrib.auth import forms

from apps.users.models import User


class UserForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )
