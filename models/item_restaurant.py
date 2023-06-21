from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from models.item_restriction_association import ItemRestrictionAssociation

class ItemRestaurant(Base):
    __tablename__ = 'item_restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String(255), nullable=False)
    url_image = Column(String, nullable=True)
    
    restaurant = Column(Integer, ForeignKey('restaurant.cnpj'))
    item_orders = relationship("ItemOrder", backref='item_restaurant')
    restrictions = relationship("Restriction", secondary= ItemRestrictionAssociation , backref='items')
    

    def __init__(self, price, name, description, url_image):
        self.price = price
        self.name = name
        self.description = description
        self.url_image = url_image

    #relacionar com restaurant
    #relacionar com restriction 