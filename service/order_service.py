from repositories.order_repository import OrderRepository
from repositories.item_order_repository import ItemOrderRepository

class OrderService:

    order_repo = OrderRepository()
    item_order_repo = ItemOrderRepository()


    def create_order(self, **kwargs):
        items = kwargs.pop('items', [])

        order = order


