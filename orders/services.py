from .models import OrderItems, Orders
from django.shortcuts import get_object_or_404
from django.http import Http404


from payments.models import Payments
from contacts.models import Contacts
from items.models import Items
from hashids import Hashids
from django.conf import settings

hashids = Hashids(salt = settings.SECRET_KEY, min_length=12)

def insert_order(order_data):
    order_items = order_data.pop('order_items', None)
   
    payment_data = order_data.pop('payment', None)
    del payment_data['order']

    contact_id = order_data.pop('contact', None)
    contact_instance = get_object_or_404(Contacts, pk=contact_id)

    if Orders.objects.filter(order_no=order_data['order_no']).exists():
        return 409, {
            "order_no" : f"{order_data['order_no']} Already Exists",
            "message" : "Create with a new Order Number"
        }
    order_no = order_data['order_no']
    order_slug = hashids.encode(int(order_no))
    order_data['order_slug'] = order_slug
    order_instance = Orders.objects.create(contact=contact_instance ,**order_data)

    order_lines = []
    for items in order_items:
        item_instance = Items.objects.get(pk=items['item_id'])
        if item_instance:
            print("ITEM exists")
            del items['item_id']
        
            order_lines.append(OrderItems(order=order_instance, item_id=item_instance, **items))
        # else:
        #     item_instance, item_created = Items.objects.get_or_create(pk=uuid.uuid4())

    OrderItems.objects.bulk_create(order_lines)

    Payments.objects.create(order=order_instance, **payment_data)

    return {
        "is_created" : True,
        "order_slug" : order_slug
        }


def get_order(slug):
    order_no = hashids.decode(slug)[0]
    try:
        # order_data = get_object_or_404(Orders, order_no=order_no)
        order_data = Orders.objects.filter(order_no=order_no).first()
    except Http404:
        return 404, {
            "message" : "No such Order exists"
        }
    
    order_items = OrderItems.objects.filter(order=order_data.id, is_active=True).values()
    payment_data = Payments.objects.filter(order=order_data.id).values()

    return {
        "order_data" : order_data,
        "order_items" : order_items,
        "payment_data" : payment_data
    }




