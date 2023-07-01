from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    apelido = Column(String(20), nullable=True)
    cep = Column(String(8), nullable=False)
    rua= Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    numero = Column(Integer, nullable=False)
    complemento= Column(String(100), nullable=True)
    tipo = Column(String(20))

    __mapper_args__ = {
        'polymorphic_on': tipo,
        'polymorphic_identity': 'address'
    }

 
class AddressCustomer(Address):
    __tablename__ = 'address_customer'

    id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    cliente_id = Column(Integer, ForeignKey('customer.id'))
    cliente = relationship('Customer', back_populates='enderecos')

    __mapper_args__ = {
        'polymorphic_identity': 'address_customer',
    }

class AddressRestaurant(Address):
    __tablename__ = 'address_restaurant'

    id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    restaurante_id= Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', back_populates='endereco')

    __mapper_args__ = {
        'polymorphic_identity': 'address_restaurant',
    }