from django.db import models

# Create your models here.
class Shipment(models.Model):
    tracking_number = models.CharField(max_length=128)
    sender = models.CharField(max_length=128)
    recipient = models.CharField(max_length=128)
    shipping_address = models.CharField(max_length=256)
    delivery_address = models.CharField(max_length=256)
