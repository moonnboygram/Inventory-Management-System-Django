from django import forms
from .models import Product
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
        