from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("products/", views.product_list, name="product_list"),
    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("categories/", views.category_list, name="category_list"),
    path("supplies/", views.supply_list, name="supply_list"),
    path("low_stock/", views.low_stock_list, name="low_stock_list"),
    path("add-product/", views.add_product, name= "add_product"),
    path("edit-product/<int:id>/", views.edit_product, name= "edit_product"),
    path("delete-product/<int:id>/", views.delete_product, name="delete_product"),
    path("goods-received/add/",views.add_goods_received,name="add_goods_received",),
    path("goods-received/",views.goods_received_list, name="goods_received_list"),
    path("purchase-orders/",views.purchase_order_list, name="purchase_order_list"),
    path("purchase-orders/add/",views.add_purchase_order,name="add_purchase_order"),
    path("purchase-orders/<int:pk>",views.purchase_order_detail,name="purchase_order_detail"),
    path("purchase-orders/<int:pk>/add-item/",views.add_purchase_order_item,name="add_purchase_order_item"),
    path("purchase-orders/<int:pk>/approve/",views.approve_purchase_order,name="approve_order",), 

]