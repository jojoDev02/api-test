from models.item_order import ItemOrder
from db.database import db_session
class ItemOrderRepository:
    def get_item_order_by_id(self, item_order_id):
        return db_session.query(ItemOrder).get(item_order_id)

    def create_item_order(self, quantity, value, item_restaurant_id, order_id):
        new_item_order = ItemOrder(
            quantity=quantity,
            value=value,
            item_restaurant_id=item_restaurant_id,
            order_id=order_id
        )
        db_session.add(new_item_order)
        db_session.commit()
        return new_item_order

    def update_item_order(self, item_order_id, quantity=None, value=None):
        item_order = self.get_item_order_by_id(item_order_id)
        if item_order:
            if quantity is not None:
                item_order.quantity = quantity
            if value is not None:
                item_order.value = value
            db_session.commit()
        return item_order

    def delete_item_order(self, item_order_id):
        item_order = self.get_item_order_by_id(item_order_id)
        if item_order:
            db_session.delete(item_order)
            db_session.commit()
        return item_order
