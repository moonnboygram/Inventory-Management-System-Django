from django.contrib import admin

# Register ymodels here.

from .models import Supplier, Category, Supply, Product

# admin.site.register(Supplier)
# admin.site.register(Category)
# admin.site.register(Supply)
# admin.site.register(Product)

#CUSTOMIZE DJANGO ADMIN

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email")
    search_fields = ("name", "phone", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ("id", "invoice_number", "supplier", "supply_date")
    search_fields = ("invoice_number",)
    list_filter =("supplier", "supply_date")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "supply", "quantity", "price")
    search_fields = ("name",)
    list_filter = ("category",)
