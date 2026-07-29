from django.db import models
import random


    
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.name


class GoodsReceived(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    received_date = models.DateField()
    
    class Meta:
        verbose_name_plural = "Goods Received"
    def __str__(self):
        return self.invoice_number


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

def generate_po_number():
    while True:
        number = f"PO-{random.randint(100000, 999999)}"
        if not PurchaseOrder.objects.filter(po_number=number).exists():
            return number 

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True, default=generate_po_number,
                                 editable=False,)
    order_date = models.DateField()

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('received', 'Fully Received'),
        ('partially', 'Partially Received'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.po_number 
    
class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def line_total(self):
        return self.quantity_ordered * self.cost_price

    def __str__(self):
        return self.product.name


class GoodsReceivedItem(models.Model):
    goods_received = models.ForeignKey(GoodsReceived, on_delete=models.CASCADE)

    product =models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity_received = models.PositiveIntegerField()

    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.product.name