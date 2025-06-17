from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_classes = (
            "block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 "
            "placeholder:text-gray-400 sm:text-sm/6 border border-gray-300 "
            "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        )

        self.fields["username"].widget.attrs.update(
            {
                "class": input_classes,
                "placeholder": "Nazwa",
                "autocomplete": "username",
                "autofocus": True,
                "id": "username",
            }
        )

        self.fields["email"].widget.attrs.update(
            {
                "class": input_classes,
                "placeholder": "Email",
                "autocomplete": "email",
                "id": "email",
            }
        )

        self.fields["password1"].widget.attrs.update(
            {
                "class": input_classes,
                "placeholder": "Hasło",
                "autocomplete": "new-password",
                "id": "password1",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": input_classes,
                "placeholder": "Powtórz hasło",
                "autocomplete": "new-password",
                "id": "password2",
            }
        )
