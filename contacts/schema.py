from ninja import ModelSchema, Schema
from .models import Contacts, Address
from core.models import Accounts
from typing import List, Optional

class ErrorSchema(Schema):
    message : str
    details : str

class AddressListSchema(ModelSchema):
    class Meta:
        model = Address
        fields = "__all__"
        exclude = ["id"]

class AddressCreateSchema(ModelSchema):
    class Meta:
        model = Address
        fields = "__all__"
        exclude = ["id", "updated_at", "created_at"]

class AddressUpdateSchema(Schema):
    address1 : Optional[str] = None
    address2 : Optional[str] = None
    landmark : Optional[str] = None
    city : Optional[str] = None
    state : Optional[str] = None
    pin_code : Optional[str] = None

class ContactListSchema(ModelSchema):
    class Meta:
        model = Contacts
        fields = "__all__"
    address : AddressListSchema

class ContactCreateSchema(ModelSchema):
    class Meta:
        model = Contacts
        fields = "__all__"
        exclude = ["cont_id", "updated_at", "created_at"]
    address : AddressCreateSchema

class ContactUpdateSchema(Schema):
    company_name : Optional[str] = None
    display_name : Optional[str] = None
    name : Optional[str] = None
    phone : Optional[str] = None
    alt_phone : Optional[str] = None
    email : Optional[str] = None
    is_gst_registered : Optional[bool] = None
    gstin : Optional[str] = None
    is_active : Optional[bool] = None
    type : Optional[str] = None
    account : Optional[int] = None

    address : Optional[AddressUpdateSchema] = None







