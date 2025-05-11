from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta

class Restaurant(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название ресторана")
    description = models.TextField(blank=True, verbose_name="Описание")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables', verbose_name="Ресторан")
    table_number = models.IntegerField(unique=True, verbose_name="Номер столика")
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], verbose_name="Вместимость")  # Пример: от 1 до 20 мест

    def __str__(self):
        return f"Столик {self.table_number} (вместимость: {self.capacity})"

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Столик")
    booking_datetime = models.DateTimeField(verbose_name="Дата и время бронирования")
    number_of_guests = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Количество гостей")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    notes = models.TextField(blank=True, verbose_name="Примечания")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return f"Бронь столика {self.table.table_number} на {self.booking_datetime.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
        ordering = ['-booking_datetime']  # Сортировка по убыванию даты бронирования