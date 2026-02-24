from django.contrib import admin
from .models import Product, Stock


class StockInline(admin.TabularInline):
    model = Stock
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "unit", "price", "active")
    search_fields = ("name", "sku")
    inlines = [StockInline]
