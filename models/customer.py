from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.user import User
from models.address import AddressCustomer
from models.order import Order

class Customer(User):

    __tablename__ = 'customer'

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    cpf = Column(String(11), nullable=False, unique=True)
    nome = Column(String(255), nullable=False)
    telefone = Column(String(11), nullable=False)

    enderecos = relationship('AddressCustomer', back_populates='cliente', cascade="all, delete-orphan")
    pedidos = relationship('Order', back_populates='cliente')


    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }

    def to_dict(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'nome': self.nome,
            'email':self.email,
            'telefone': self.telefone,
            'enderecos': [endereco.to_dict() for endereco in self.enderecos],
            'pedidos': [pedido.to_dict() for pedido in self.pedidos]
        }
                


