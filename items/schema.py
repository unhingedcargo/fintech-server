from ninja import ModelSchema, Schema
from .models import Items
from typing import Optional

class ErrorSchema(Schema):
    message: str
    details : str

class ItemsListSchema(ModelSchema):
    class Meta:
        model = Items
        fields = "__all__"


class ItemsCreateSchema(ModelSchema):
    class Meta:
        model = Items
        fields = "__all__"
        exclude = ["item_id", "updated_at", "created_at"]

class ItemsUpdateSchema(Schema):
    item : Optional[str] = None
    unit : Optional[str] = None
    hsn_code : Optional[str] = None
    tax : Optional[str] = None
    purchase_rate : Optional[float] = None
    sales_rate : Optional[float] = None