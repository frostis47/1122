from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(
        max_length=100,
        verbose_name="Username",
        blank=True,
        null=True,
        help_text="Введите свое имя",
    )
    email = models.EmailField(unique=True, verbose_name="Эл.почта")
    name = models.CharField(max_length=45, verbose_name="имя", help_text="Введите имя")

    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона",
        blank=True,
        null=True,
    )
    is_moder = models.BooleanField(default=False, verbose_name="модератор")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}, {self.name}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "Пользователи"