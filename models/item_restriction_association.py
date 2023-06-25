from sqlalchemy import Column, ForeignKey, Integer
from db.database import Base

class ItemRestrictionAssociation(Base):

    __tablename__ = 'item_restriction_association'

    item_restaurant_id = Column(Integer, ForeignKey('item_restaurant.id'), primary_key=True)
    restriction_id = Column(Integer, ForeignKey('restriction.id'), primary_key=True)

