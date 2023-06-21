from sqlalchemy import Column, Enum, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

from enums.payment_method import PaymentMethod
from enums.status_order import StatusOrder
from .item_order import ItemOrder

class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    statusOrder = Column(Enum(StatusOrder), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)

    items_order= relationship('ItemOrder', backref='order')
    customer= Column(String, ForeignKey('customer.cpf'))

    def __init__(self, value, date, statusOrder, payment_method):
        self.value = value
        self.date = date
        self.statusOrder = statusOrder
        self.payment_method = payment_method

    # relacionar com item_pedido 
    # relacionar com cliente 
