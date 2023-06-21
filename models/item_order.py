from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class ItemOrder(Base):
    __tablename__ = 'item_order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable= False)
    value = Column(Float, nullable=False)
    order = relationship(Integer, ForeignKey('order.order_id'))


    

