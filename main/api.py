from ninja import NinjaAPI
from core.api import core_router as coreRouter
from contacts.api import contact_router
from items.api import items_router
from payments.api import payment_router
from orders.api import order_router


api = NinjaAPI(
    title= "Fintech Backend",
    version= "1.0.0",

)

api.add_router('/core', coreRouter)
api.add_router('/contacts', contact_router)
api.add_router('/items', items_router)
api.add_router('/payments', payment_router)
api.add_router('/order', order_router)

