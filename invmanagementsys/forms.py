from django import forms
from .models import Product, PurchaseOrder, PurchaseOrderItem
from .models import GoodsReceived

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets ={
            "name": forms. TextInput(attrs={"class": "form-control"}),
            "category": forms. Select(attrs={"class": "form-select"}),
            "supply": forms. Select(attrs={"class": "form-select"}),
            "quantity": forms. NumberInput(attrs={"class": "form-control"}),
            "price": forms. NumberInput(attrs={"class": "form-control"}),
            
        }
class GoodsReceivedForm(forms.ModelForm):
    class Meta:
        model = GoodsReceived
        fields = "__all__"
        widgets = {
            "supplier": forms.Select(attrs={"class": "form-select"}),
            "invoice_number": forms.TextInput(attrs={"class":"form-control"}),
            "received_date": forms.DateInput(
                attrs={
                "class": "form-conctrol",
                "type": "date",
                }
            ),
        }
class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ["supplier", "order_date"]

        widgets ={
            "supplier": forms.Select(attrs={"class": "form-select"}),
            "order_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
        }
class PurchaseOrderItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderItem
        fields = ["product", "quantity_ordered"]

        widgets ={
            "product": forms.Select(
                attrs={"class": "form-select"}
            ),
            "quantity_ordered": forms.NumberInput(
                attrs={"class": "form-control" }
            ),
        }