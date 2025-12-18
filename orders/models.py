from django.db import models
from contacts.models import Contacts
from items.models import Items
from uuid import uuid4


class OrderItems(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, blank=True, null=True)
    item_id = models.ForeignKey(Items, on_delete=models.SET_NULL, blank=True, null=True)
    item = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)
    is_active = models.BigIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_items'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    order_slug = models.CharField(max_length=50)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    grandtotal = models.FloatField(blank=True, null=True)
    current_status = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'