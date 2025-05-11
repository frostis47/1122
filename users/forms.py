from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from users.models import User

forbidden = []


class UserRegistrationForm(UserCreationForm):
    """Форма для регестрация usera"""

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "phone_number")


class UserForm(forms.ModelForm):
    """Форма usera"""

    class Meta:
        model = User
        fields = ["name", "email", "phone_number"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите имя",  # Текст подсказки внутри поля
            }
        )
        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "Введите email"})

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in forbidden):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return name