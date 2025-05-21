from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с заданным email и паролем.
        """
        if not username:
            raise ValueError('Имя пользователя должно быть указано')
        if not email:
            raise ValueError('Эл. почта должна быть указана')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(
        max_length=100,
        verbose_name="Имя пользователя",
        blank=True,
        null=True,
        help_text="Введите свое имя",
    )
    email = models.EmailField(unique=True, verbose_name="Эл. почта")
    name = models.CharField(max_length=45, verbose_name="Имя", help_text="Введите имя")

    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона",
        blank=True,
        null=True,
    )
    is_moder = models.BooleanField(default=False, verbose_name="Модератор")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email}, {self.name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
