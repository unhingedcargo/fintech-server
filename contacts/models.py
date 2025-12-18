from django.db import models
from datetime import datetime
from core.models import Accounts
from uuid import uuid4

# Create your models here.

class Address(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    address1 = models.TextField(blank=True, null=True, max_length=50)
    address2 = models.TextField(blank=True, null=True, max_length=50)
    landmark = models.TextField(blank=True, null=True, max_length=50)
    city = models.TextField(blank=True, null=True, max_length=50)
    state = models.TextField(blank=True, null=True, max_length=50)
    pin_code = models.TextField(blank=True, null=True, max_length=6)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'address'

class Contacts(models.Model):
    cont_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company_name = models.CharField(blank=True, null=True, max_length=100)
    display_name = models.CharField(blank=True, null=True, max_length=100)
    name = models.CharField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=15)
    alt_phone = models.CharField(blank=True, null=True, max_length=15)
    email = models.CharField(blank=True, null=True, max_length=100)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    is_gst_registered = models.BooleanField(blank=False, null=False, default=False)
    gstin = models.CharField(blank=True, null=True, max_length=15)
    is_active = models.BooleanField(blank=False, null=False, default=True)
    type = models.CharField(blank=True, null=True, max_length=20)
    account = models.ForeignKey(Accounts, models.DO_NOTHING, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contacts'
        constraints = [
            models.UniqueConstraint(fields=['phone'], name='unique_contact_number')
        ]