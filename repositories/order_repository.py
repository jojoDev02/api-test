import datetime
from enums.status_order import StatusOrder
from models.order import Order
from models.item_order import ItemOrder
from models.item_restaurant import ItemRestaurant
from db.database import db_session

class OrderRepository:

    def get_order_by_id(self, order_id):
        return db_session.query(Order).get(order_id)

    def get_orders_by_customer_id(self, customer_id):
        return db_session.query(Order).filter_by(customer_id=customer_id).all()
    
    def get_orders_by_restaurant_id(self, restaurant_id):
        return db_session.query(Order).join(Order.item_orders).join(ItemOrder.item_restaurant).filter(ItemRestaurant.restaurant_id == restaurant_id).all()

    def create_order(self,restaurant, customer, **kwargs):

        items = kwargs.pop('items', [])
        #resolver questao com o tipo data
        order = Order(value=kwargs['value'],
                  date=datetime.date.today(), 
                  statusOrder=StatusOrder.AWAINTING_CONFIRMATION,  
                  payment_method=kwargs['payment_method'], 
                  restaurant_id=restaurant.id,
                  customer_id=customer.id)
        
        # order = Order(**kwargs)
        # order.restaurant_id = restaurant.id
        # order.customer_id = customer.id
        db_session.add(order)
        db_session.commit()


        for item in items:
            item_order = ItemOrder(quantity=item['quantity'], value=item['value'], item_restaurant_id=item['item_restaurant_id'], order_id=order.order_id)
            order.item_orders.append(item_order)
        
        restaurant.orders.append(order)
        db_session.commit()

        return order
        
    def update_status_order(self, order_id, status_order):
        order = self.get_order_by_id(order_id)
        if order:
            order.statusOrder = status_order
            db_session.commit()
        return order

