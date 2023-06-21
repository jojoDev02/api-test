from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base
from models.item_restriction_association import ItemRestrictionAssociation


class Restriction(Base):

    __tablename__ = 'restriction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)

    items = relationship("ItemRestaurant", secondary=ItemRestrictionAssociation, backref='restrictions')

    def __init__(self, name):
        self.name = name

#relacionar com itens