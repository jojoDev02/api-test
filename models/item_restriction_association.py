from sqlalchemy import Column, ForeignKey, Integer
from db.database import Base

class ItemRestrictionAssociation(Base):

    __tablename__ = 'item_restriction_association'

    item_id = Column(Integer, ForeignKey('item_restaurante.id'), primary_key=True)
    restriction_id = Column(Integer, ForeignKey('restriction.id'), primary_key=True)

