from ninja import ModelSchema, Schema
from .models import Payments
from typing import Optional

class PaymentListSchema(ModelSchema):
    class Meta:
        model = Payments
        fields = "__all__"
        exclude = ["id"]

class PaymentCreateSchema(ModelSchema):
    class Meta:
        model = Payments
        fields = "__all__"
        exclude = ["id", "updated_at", "created_at"]

class PaymentUpdateSchema(Schema):
    date : Optional[str] = None
    payment_made : Optional[str] = None
    mode : Optional[str] = None
    remark : Optional[str] = None
    





