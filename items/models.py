from django.db import models
from uuid import uuid4
from core.models import Taxes

# Create your models here.
class Items(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    item = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    hsn_code = models.CharField(max_length=20, blank=True, null=True)
    tax = models.ForeignKey(Taxes, models.DO_NOTHING, blank=True, null=True)
    purchase_rate = models.FloatField(blank=True, null=True)
    sales_rate = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'items'