from django.contrib import admin

# Register ymodels here.

from .models import Supplier, Category, GoodsReceived, GoodsReceivedItem, Product

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

@admin.register(GoodsReceived)
class GoodsReceivedAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "supplier", "recieved_date")
    # search_fields = ("invoice_number",)
    # list_filter =("supplier", "recieved_date")

@admin.register(GoodsReceivedItem)
class GoodsReceivedItemAdmin(admin.ModelAdmin):
    list_display = ("goods_recieved", "product", "quantity_recieved", "cost_price",)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category","quantity", "cost_price", "selling_price",)
    search_fields = ("name",)
    list_filter = ("category",)
  