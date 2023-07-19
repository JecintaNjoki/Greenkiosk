from django.db import models
from Vendor.models import Vendor
from Customer.models import Customer

# Create your models here.
class Products(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Vendor=models.ForeignKey(Vendor,null =True, on_delete =models.CASCADE)
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image=models.ImageField()
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    