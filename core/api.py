from ninja import Router
from .models import State, Taxes, Accounts
from .schema import StateListSchema, TaxListSchema, AccountListSchema
from typing import List

core_router = Router(tags=["Core"])

@core_router.get('/state_list', response=List[StateListSchema])
def state_list(request):
    return State.objects.all().order_by('name')

@core_router.get('/tax_list', response=List[TaxListSchema])
def tax_list(request):
    return Taxes.objects.all()

@core_router.get('/account_list', response=List[AccountListSchema])
def account_list(request):
    return Accounts.objects.all()
