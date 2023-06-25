from sqlalchemy import Column, Enum, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from models.item_order import ItemOrder

from enums.payment_method import PaymentMethod
from enums.status_order import StatusOrder

class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    statusOrder = Column(Enum(StatusOrder), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)

    customer_id= Column(String, ForeignKey('customer.cpf'))
    customer = relationship('Customer', back_populates='orders')
    item_orders= relationship('ItemOrder', back_populates='order')



    # relacionar com cliente 
