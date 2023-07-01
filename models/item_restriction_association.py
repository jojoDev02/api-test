from sqlalchemy import Column, ForeignKey, Integer
from db.database import Base

class ItemRestrictionAssociation(Base):

    __tablename__ = 'item_restriction_association'

    item_restaurante_id = Column(Integer, ForeignKey('item_restaurant.id'), primary_key=True)
    restricao_id = Column(Integer, ForeignKey('restriction.id'), primary_key=True)

