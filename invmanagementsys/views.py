from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Supplier, GoodsReceived 
from .forms import ProductForm, PurchaseOrder, PurchaseOrderForm, GoodsReceivedForm, PurchaseOrderItemForm
from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from django.contrib import messages
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

    return render(request, "invmanagementsys/add_goods_received.html", {"form": form},)

def goods_received_list(request):
    goods_received = GoodsReceived.objects.all()

    return render(
        request,
        "invmanagementsys/goods_received_list.html",
        {"goods_received": goods_received},
    ) 

def purchase_order_list(request):
    purchase_orders =PurchaseOrder.objects.all().order_by("-po_number")

    context = {
        "purchase_orders": purchase_orders,
    }
    
    return render(request,
        "invmanagementsys/purchase_order_list.html",context,
    )

def add_purchase_order(request):
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST)

        if form.is_valid():
            purchase_order = form.save()

            return redirect("purchase_order_list", pk=purchase_order.pk)
    else:
        form = PurchaseOrderForm
    
    context = {
        "form": form
    }
    
    return render(request, "invmanagementsys/add_purchase_order.html",context,)

def purchase_order_detail(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder,pk=pk)
    
    items = purchase_order.items.all()
    
    total_items = items.count()

    total_quantity = (items.aggregate(total=Sum("quantity_ordered"))["total"] or 0)

    estimated_cost = (items.aggregate(total=Sum(ExpressionWrapper(F("quantity_ordered") * 
                        F("cost_price"),output_field=DecimalField())))["total"])
    
    context = {
        "purchase_order": purchase_order,
        "items": items,
        "total_items": total_items,
        "total_quantity": total_quantity,
        "estimated_cost": estimated_cost,
    }

    return render (request, "invmanagementsys/ourchase_order_detail.html", context,)

def add_purchase_order_item(request, pk):

    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)

    if request.method == "POST":
        form = PurchaseOrderItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)

            item.purchase_order = purchase_order

            item.save()

            return redirect("purchase_order_detail", pk=purchase_order.pk)
        
    else:
        form = PurchaseOrderItemForm()

    context = {"form": form, "purchase_order": purchase_order}
    return render(request, "invmanagementsys/add_purchase_item.html", context)

def approve_purchase_order(request, pk):

    purchase_order = get_object_or_404(PurchaseOrder,pk=pk)

    if purchase_order.items.count()== 0:

        messages.error(
            request,"you cannot approve a Purchase Order without any products.")
        return redirect("purchase_order_detail", pk=purchase_order.pk)
    
    purchase_order.status = "appproved"

    purchase_order.save()

    messages.success(request, "Purchase Order approved successsfully.")

    return redirect("purchase_order_detail",pk=purchase_order.pk)

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


