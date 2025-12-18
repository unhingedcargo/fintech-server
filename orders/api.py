from ninja import Router
from django.http import Http404
from django.shortcuts import get_object_or_404
from.schema import OrderCreateSchema, OrderListSchema
from .models import OrderItems, Orders
from payments.models import Payments
from items.models import Items
from contacts.models import Contacts

from hashids import Hashids
from django.conf import settings

from.services import insert_order, get_order


order_router = Router(tags=["Orders"])
hashids = Hashids(salt = settings.SECRET_KEY, min_length=12)


@order_router.post("/create", response={201:dict, 409:dict})
def create_order(request, payload:OrderCreateSchema):
    order_data = payload.dict()

    # order_items = order_data.pop('order_items', None)
   
    # payment_data = order_data.pop('payment', None)
    # del payment_data['order']

    # contact_id = order_data.pop('contact', None)
    # contact_instance = get_object_or_404(Contacts, pk=contact_id)

    # if Orders.objects.filter(order_no=order_data['order_no']).exists():
    #     return 409, {
    #         "order_no" : f"{order_data['order_no']} Already Exists",
    #         "message" : "Create with a new Order Number"
    #     }
    # order_no = order_data['order_no']
    # order_slug = hashids.encode(int(order_no))
    # order_data['order_slug'] = order_slug
    # order_instance = Orders.objects.create(contact=contact_instance ,**order_data)

    # order_lines = []
    # for items in order_items:
    #     item_instance = Items.objects.get(pk=items['item_id'])
    #     if item_instance:
    #         print("ITEM exists")
    #         del items['item_id']
        
    #         order_lines.append(OrderItems(order=order_instance, item_id=item_instance, **items))
    #     # else:
    #     #     item_instance, item_created = Items.objects.get_or_create(pk=uuid.uuid4())

    # OrderItems.objects.bulk_create(order_lines)

    # Payments.objects.create(order=order_instance, **payment_data)

    # return 201 , {
    #     "id" : f"{order_instance.order_no} and For {order_instance.contact}",
    #     "message" : "Order Created Successfully"
    # }

    order_created = insert_order(order_data=order_data)
    if order_created:
        return 201 , {
            "details" : order_created,
            "message" : "Order Created Successfully"
        }
        


@order_router.get("/{order_slug}", response={200:OrderListSchema, 404:dict})
def fetch_order(request, order_slug:str):
    return get_order(slug=order_slug)


# @order_router.patch("/{order_no}", response={201:OrderListSchema, 404:dict})
# def update_order(request, order_no)




