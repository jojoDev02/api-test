from sqlalchemy import Column, ForeignKey, Integer
from db.database import Base

class Favorite(Base):

    __tablename__ = 'favorite'

    cliente_id =  Column(Integer, ForeignKey('customer.id'), primary_key=True)
    item_id =  Column(Integer, ForeignKey('item_restaurant.id'), primary_key=True)
