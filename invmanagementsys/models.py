from django.db import models


    
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
    recieved_date = models.DateField()
    
    # class Meta:
    #     verbose_name_plural = "Supplies"
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


class GoodsReceivedItem(models.Model):
    goods_recieved = models.ForeignKey(GoodsReceived, on_delete=models.CASCADE)

    product =models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity_recieved = models.PositiveIntegerField()

    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.product.name