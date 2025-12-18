from ninja import Router
from .schema import *
from .models import *
from core.models import Taxes
from typing import List
from django.shortcuts import get_object_or_404


items_router = Router(tags=["Items"])


@items_router.post("/create", response={200:ItemsListSchema, 409:ErrorSchema})
def create_item(request, payload:ItemsCreateSchema):
    payload_data = payload.dict()
    
    tax_id = payload_data.pop('tax', None)
    tax_instance = Taxes.objects.get(pk=tax_id)

    item_instance = Items.objects.create(
        **payload_data,
        tax = tax_instance
    )
    return item_instance

@items_router.get("/all", response=List[ItemsListSchema])
def item_list(request):
    return Items.objects.all()

@items_router.get("/{item_id}", response=ItemsListSchema)
def fetch_item(request, item_id:str):
    return get_object_or_404(Items, pk=item_id)

@items_router.patch("/{item_id}", response=ItemsListSchema)
def update_item(request, item_id:str, payload:ItemsUpdateSchema):
    item_instance = get_object_or_404(Items, pk=item_id)
    payload_data = payload.dict(exclude_unset=True)

    tax_id = payload_data.pop('tax', None)
    if tax_id:
        tax_instance = get_object_or_404(Taxes, pk=tax_id)
        item_instance.tax = tax_instance

    for field, value in payload_data.items():
        setattr(item_instance, field, value)
    
    item_instance.save()
    item_instance.refresh_from_db()

    return item_instance

@items_router.delete("/{item_id}", response={200 : ErrorSchema})
def delete_item(request, item_id:str):
    item_instance = get_object_or_404(Items, pk=item_id)
    deleted_item = item_instance.item
    item_instance.delete()

    return 200, {"message" : "This item has been deleted",
                 "details" : f"{deleted_item} deleted successfully."}



