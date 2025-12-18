from ninja import Router
from .schema import *

payment_router = Router(tags=["Payments"])

@payment_router.post("/create", response=PaymentListSchema)
def create_payment(request, payload:PaymentCreateSchema):
    print(payload.dict())

    return payload


