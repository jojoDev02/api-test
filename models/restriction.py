from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Restriction(Base):

    __tablename__ = 'restriction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)

    items_restaurant = relationship("ItemRestaurant", secondary='item_restriction_association', back_populates='restrictions')

    def __init__(self, name):
        self.name = name
