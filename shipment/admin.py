from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Shipment, Package, TrackingEvent


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'sender', 'recipient', 'shipping_address', 'delivery_address', 'status', 'date_shipped', 'date_delivered')

