from ninja import ModelSchema, Schema
from contacts.models import Contacts
from .models import OrderItems, Orders
from typing import Optional, List
from payments.schema import PaymentCreateSchema, PaymentListSchema

class OrderItemListSchema(ModelSchema):
    class Meta:
        model = OrderItems
        fields = "__all__"

class OrderItemCreateSchema(ModelSchema):
    class Meta:
        model = OrderItems
        fields = "__all__"
        exclude = ["id", "order", "updated_at", "created_at"]

class OrderItemUpdateSchema(Schema):
    item_id : Optional[str] = None
    item : Optional[str] = None
    description : Optional[str] = None
    qty : Optional[str] = None
    rate : Optional[str] = None
    tax_rate : Optional[str] = None
    is_active : Optional[str] = None

class OrderList(ModelSchema):
    class Meta:
        model = Orders
        fields = "__all__"


class OrderListSchema(Schema):
    order_data : OrderList
    order_items : List[OrderItemListSchema]
    payment_data : List[PaymentListSchema]

class OrderCreateSchema(ModelSchema):
    class Meta:
        model = Orders
        fields = "__all__"
        exclude = ["id", "order_slug", "updated_at", "created_at"]
    order_items: List[OrderItemCreateSchema]
    payment : PaymentCreateSchema


# class OrderUpdateSchema(ModelSchema):
    
#     order_items = List[OrderItemUpdateSchema]



