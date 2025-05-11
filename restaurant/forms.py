from django import forms
from django.core.exceptions import ValidationError

from .models import Order, Table


class TableForm(forms.ModelForm):
    """Форма для столов"""

    class Meta:
        model = Table
        fields = ["number", "sitting", "price", "image"]

    def clean_number(self):
        number = self.cleaned_data.get("number")
        if number in [table.number for table in Table.objects.all()]:
            raise ValidationError("такой стол уже есть")
        return number

    def clean_sitting(self):
        sitting = self.cleaned_data.get("sitting")
        if sitting > 6:
            raise ValidationError("Не больше 6 мест")
        return sitting


class OrderForm(forms.ModelForm):
    """Форма для заказов"""

    class Meta:
        model = Order
        fields = ["table", "time", "date"]
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"class": "form-control", "placeholder": "Выберите дату", "type": "date"}
            ),
        }

    def clean(self):
        super().clean()
        time = self.cleaned_data.get("time")
        date = self.cleaned_data.get("date")
        table = self.cleaned_data.get("table")

        print(table, time, date)

        orders = Order.objects.filter(table=table, date=date, time=time)
        if orders.exists():
            raise ValidationError("Стол уже занят")
