from django.shortcuts import render
from .models import Product, Category, Supplier, Supply 

# def dashboard(request):
#     return render(request, "invmanagementsys/dashboard.html")

# # Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "invmanagementsys/product_list.html", {"products": products},)

def supplier_list(request):
        suppliers = Supplier.objects.all()
        return render(request,"invmanagementsys/supplier_list.html",
                      {"suppliers": suppliers})

def category_list(request):
     categories = Category.objects.all()
     return render(request, "invmanagementsys/category_list.html",
                   {"categories": categories})

def dashboard(request):
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()
    total_supplies = Supply.objects.count()
    low_stock = Product.objects.filter(quantity__lte=20).count()
   

    context = {
        "total_products": total_products,
        "total_categories": total_categories,
        "total_suppliers": total_suppliers,
        "total_supplies": total_supplies,
        "low_stock": low_stock
    }

    return render(request, "invmanagementsys/dashboard.html", context)