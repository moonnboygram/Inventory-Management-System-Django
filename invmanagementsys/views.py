from django.shortcuts import render
from .models import Product 

def dashboard(request):
    return render(request, "invmanagementsys/dashboard.html")

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "invmanagementsys/product_list.html", {"products": products})