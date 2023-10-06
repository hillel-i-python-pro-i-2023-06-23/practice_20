from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.contrib.auth import forms

from apps.users.models import User


class UserForm(forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("username", css_class="small-input"),
            Field("email", css_class="small-input"),
            Field("password1", css_class="small-input"),
            Field("password2", css_class="small-input"),
        )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )
