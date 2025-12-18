from django.db import models


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    gst_code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return f"({self.gst_code}) {self.name}"

    class Meta:
        db_table = 'state'
        verbose_name = 'State'
        verbose_name_plural = 'States'


class Taxes(models.Model):
    id = models.BigAutoField(primary_key=True)
    tax = models.TextField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.rate})"
    
    class Meta:
        db_table = 'taxes'
              

class Accounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    txn_type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'accounts'