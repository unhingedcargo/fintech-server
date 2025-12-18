from django.db import models
from orders.models import Orders
from core.models import Accounts

# Create your models here.
class Cashflow(models.Model):
    id = models.BigAutoField(primary_key=True)
    voucher_no = models.CharField(max_length=10)
    date = models.DateTimeField()
    ledger = models.CharField(max_length=50, blank=True, null=True)
    account = models.ForeignKey(Accounts, models.DO_NOTHING, blank=True, null=True)
    details = models.CharField(max_length=50, blank=True, null=True)
    cash_in = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'cashflow'

class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    payment_made = models.FloatField(blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payments'