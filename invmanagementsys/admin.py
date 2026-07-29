from django.contrib import admin

# Register ymodels here.

from .models import (Supplier, Category, GoodsReceived, GoodsReceivedItem, Product,
                     PurchaseOrder, PurchaseOrderItem, )

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
    list_display = ("invoice_number", "supplier", "received_date")
    # search_fields = ("invoice_number",)
    # list_filter =("supplier", "recieved_date")

@admin.register(GoodsReceivedItem)
class GoodsReceivedItemAdmin(admin.ModelAdmin):
    list_display = ("goods_received", "product", "quantity_received", "cost_price",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category","quantity", "cost_price", "selling_price",)
    search_fields = ("name",)
    list_filter = ("category",)
  
@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ("po_number", "supplier", "order_date", "status")
    search_fields = ("po_number", "supplier__name")
    list_filter = ("status", "order_date", "supplier")

@admin.register(PurchaseOrderItem)
class PurchaseOrderItemAdmin(admin.ModelAdmin):
    list_display = ("purchase_order", "product", "quantity_ordered", "cost_price")
    