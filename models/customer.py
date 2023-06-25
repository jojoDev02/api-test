from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.user import User
from models.address import AddressCustomer
from models.order import Order

class Customer(User):

    __tablename__ = 'customer'

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    cpf = Column(String(11), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(11), nullable=False)

    addresses = relationship('AddressCustomer', back_populates='customer', cascade="all, delete-orphan")
    orders = relationship('Order', back_populates='customer')


    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }

            
#relacionar com Adress

