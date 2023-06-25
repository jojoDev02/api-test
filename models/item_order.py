from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from models.item_restaurant import ItemRestaurant

class ItemOrder(Base):
    __tablename__ = 'item_order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable= False)
    value = Column(Float, nullable=False)

    item_restaurant_id = Column(Integer, ForeignKey('item_restaurant.id'))
    item_restaurant = relationship('ItemRestaurant', back_populates='item_orders')

    order_id = Column(Integer, ForeignKey('order.order_id'))
    order = relationship('Order', back_populates='item_orders')


