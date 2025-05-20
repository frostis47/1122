from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from users.models import User

forbidden = []

class UserRegistrationForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "phone_number")  # Добавлено поле username

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise ValidationError("Имя пользователя обязательно.")
        return username



class UserForm(forms.ModelForm):
    """Форма usera"""

    class Meta:
        model = User
        fields = ["name", "email", "phone_number"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите имя",
            }
        )
        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "Введите email"})

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in forbidden):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return name
