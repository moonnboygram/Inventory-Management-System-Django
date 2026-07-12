from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("products/", views.product_list, name="product_list"),
    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("categories/", views.category_list, name="category_list"),
    path("supplies/", views.supply_list, name="supply_list"),
    path("low_stock/", views.low_stock_list, name="low_stock_list")
]