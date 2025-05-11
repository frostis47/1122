from django.db import models

from config import settings



class TimeSection(models.Model):
    time = models.TimeField()

    def __str__(self):
        return f"{self.time}"


class Table(models.Model):
    """Модуль для столов"""

    number = models.PositiveIntegerField(verbose_name="номер стола", help_text="Введите номер стола")
    sitting = models.PositiveIntegerField(verbose_name="мест у стола", help_text="Введите сколько мест у стола")
    content = models.TextField(verbose_name="содержимое", help_text="Введите содержимое")
    price = models.CharField(max_length=100, verbose_name="Цена", help_text="Введите цену", default=3000)
    image = models.ImageField(
        upload_to="table_image/photo",
        blank=True,
        null=True,
        verbose_name="фото",
        help_text="Загрузити фотографию",
    )
    table_occupiers = models.BooleanField(verbose_name="занятость стола", default=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения", blank=True, null=True)

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"
        ordering = ["number"]


class Order(models.Model):
    """Модуль для заказов"""

    table = models.ForeignKey(Table, on_delete=models.SET_NULL, blank=True, null=True)
    time = models.ForeignKey(TimeSection, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Создатель заказа",
    )

    def __str__(self):
        return f"{self.table}, {self.time}"

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы "
