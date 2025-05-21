from django.contrib import admin
from .models import TimeSection, Table, Order

@admin.register(TimeSection)
class TimeSectionAdmin(admin.ModelAdmin):
    list_display = ('time',)
    search_fields = ('time',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'sitting', 'price', 'table_occupiers', 'updated_at')
    search_fields = ('number',)
    list_filter = ('table_occupiers',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('table', 'time', 'date', 'owner')
    search_fields = ('owner__username',)
    list_filter = ('date',)
