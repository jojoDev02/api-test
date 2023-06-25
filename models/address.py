from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(20), nullable=True)
    cep = Column(String(8), nullable=False)
    street= Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    neighborhood = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    complement= Column(String(100), nullable=True)
    type = Column(String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'address'
    }

 
class AddressCustomer(Address):
    __tablename__ = 'address_customer'

    id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer', back_populates='addresses')

    __mapper_args__ = {
        'polymorphic_identity': 'address_customer',
    }

class AddressRestaurant(Address):
    __tablename__ = 'address_restaurant'

    id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    restaurant_id= Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', back_populates='address')

    __mapper_args__ = {
        'polymorphic_identity': 'address_restaurant',
    }