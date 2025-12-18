from django.db import models
from orders.models import Orders
from contacts.models import Contacts
from payments.models import Payments

# Create your models here.
class Estimate(models.Model):
    estimate_no = models.CharField(max_length=10)
    date = models.DateField()
    expiry_date = models.DateField()
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, blank=True, null=True)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, blank=True, null=True) # CREATED, ACCEPTED, REJECTED, INVOICED
    accepted_at = models.DateTimeField(blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)
    invoiced_at = models.DateTimeField(blank=True, null=True)

class SalesOrder(models.Model):
    so_no = models.CharField(max_length=10)
    reference_no = models.CharField(max_length=10)
    date = models.DateField()
    expected_shipment_date = models.DateField()
    payment_terms = models.CharField(max_length=20)
    delivery_method = models.CharField(max_length=20)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, blank=True, null=True)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20) # CREATED, CONFIRMED, INVOICED
    confirmed_at = models.DateTimeField(blank=True, null=True)
    invoiced_at = models.DateTimeField(blank=True, null=True)

class Invoice(models.Model):
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, blank=True, null=True)
    inv_no = models.CharField(max_length=10)
    reference_no = models.CharField(max_length=10)
    date = models.DateField()
    payment_terms = models.CharField(max_length=20)
    customer_notes = models.CharField(max_length=100)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, blank=True, null=True)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE, blank=True, null=True)
    

    



