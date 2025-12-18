from ninja import Router, errors
from django.shortcuts import get_object_or_404
from .models import Contacts, Address
from .schema import ContactListSchema, ContactCreateSchema, ErrorSchema, ContactUpdateSchema
from typing import List
from core.models import Accounts


contact_router = Router(tags=["Contact : (Customer/Vendor)"])


@contact_router.post("/create", response={200:ContactListSchema, 409: ErrorSchema})
def create_contact(request, payload:ContactCreateSchema):

    if Contacts.objects.filter(phone = payload.phone):
        raise errors.HttpError(status_code=409, message="this user already exists.")

    address_data = payload.address.dict()
    address_instance = Address.objects.create(**address_data)

    accounts_instance = Accounts.objects.get(pk=payload.account)

    contact_data = payload.dict()
    del contact_data['address']
    del contact_data['account']
    
    contact_instance = Contacts.objects.create(
        **contact_data,
        address = address_instance,
        account = accounts_instance
    )
    
    return contact_instance

@contact_router.get('/all', response=List[ContactListSchema])
def contact_list(request):
    return Contacts.objects.all()

@contact_router.get("/{cont_id}", response=ContactListSchema)
def fetch_contact(request, cont_id:str):
    return get_object_or_404(Contacts, pk=cont_id)

@contact_router.patch('/{cont_id}', response=ContactListSchema)
def update_contact(request, cont_id:str, payload:ContactUpdateSchema):
    contact_instance = get_object_or_404(Contacts, pk=cont_id)

    payload_data = payload.dict(exclude_unset=True)
    address_data = payload_data.pop('address', None)
    account_id = payload_data.pop('account', None)

    if address_data:
        address_instance = contact_instance.address

        if address_instance:
            for field, value in address_data.items():
                setattr(address_instance, field, value)
            
            address_instance.save()
    
    if account_id:
        account_instance = get_object_or_404(Accounts, pk=account_id)
        contact_instance.account = account_instance

    for field, value in payload_data.items():
        setattr(contact_instance, field, value)

    contact_instance.save()
    contact_instance.refresh_from_db()

    
    return contact_instance


@contact_router.delete("/{cont_id}", response={200 : ErrorSchema})
def delete_contact(request, cont_id:str):
    contact = get_object_or_404(Contacts, pk=cont_id)
    deleted_object = contact.display_name
    contact.delete()
    
    return 200, {"message" : "This Contact has been deleted", "details" : f"{deleted_object} deleted"}

    
    # return "Deleted Successfully"

