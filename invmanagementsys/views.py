from django.shortcuts import render, redirect
from .models import Product, Category, Supplier, GoodsReceived 
from .forms import ProductForm
from .forms import GoodsReceivedForm

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

def supply_list(request):
     supplies = GoodsReceived.objects.all()
     return render(request, "invmanagementsys/supply_list.html",
                   {"supplies": supplies})


#LOW STOCK
def low_stock_list(request):
     products = Product.objects.filter(quantity__lte=20)
     return render(request, "invmanagementsys/low_stock_list.html",{
        "products": products
     })

   #ADD PRODUCT 
def add_product(request):
    if request.method =="POST":
        form = ProductForm(request.POST)

        if form.is_valid():
             form.save()
             return redirect("product_list")
        
    else:
         form = ProductForm()

    return render(request, "invmanagementsys/add_product.html", {"form": form})

def edit_product(request,id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
             form.save()
             return redirect("product_list")
          
    else:
        form = ProductForm(instance=product)

    return render(request, "invmanagementsys/edit_product.html", {"form": form})


#DELETE PRODUCT 
def delete_product(request,id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    
    return render (request, "invmanagementsys/delete_product.html", {"product": product})
    

def add_goods_received(request):
    if request.method == "POST":
        form = GoodsReceivedForm(request.POST)

        if form.is_valid():
             form.save()
             return redirect ("goods_received_list")
    else:
        form = GoodsReceivedForm()

    return render(request, "invmanagementsys/add_goods_received.html", {"form": form})




def dashboard(request):
    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()
    total_supplies = GoodsReceived.objects.count()
    low_stock = Product.objects.filter(quantity__lte=20).count()


    context = {
        "total_products": total_products,
        "total_categories": total_categories,
        "total_suppliers": total_suppliers,
        "total_supplies": total_supplies,
        "low_stock": low_stock
    }

    return render(request, "invmanagementsys/dashboard.html", context)


