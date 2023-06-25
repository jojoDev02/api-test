from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from models.restaurant import Restaurant
from models.restriction import Restriction
from models.item_restriction_association import ItemRestrictionAssociation

class ItemRestaurant(Base):
    __tablename__ = 'item_restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String(255), nullable=False)
    url_image = Column(String, nullable=True)
    
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', back_populates='items', uselist= False)

    restrictions = relationship("Restriction", secondary= 'item_restriction_association', back_populates='items_restaurant')

    item_orders = relationship("ItemOrder", back_populates='item_restaurant')

    #relate to favorite

    