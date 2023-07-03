from sqlalchemy import Column, Enum, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from models.item_order import ItemOrder
from models.avaliacao import Avaliacao

from enums.payment_method import PaymentMethod
from enums.status_order import StatusOrder

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    statusPedido = Column(Enum(StatusOrder), nullable=False)
    metodo_pagamento = Column(Enum(PaymentMethod), nullable=False)

    cliente_id= Column(String, ForeignKey('customer.id'))
    cliente = relationship('Customer', back_populates='pedidos')
    itens_pedidos= relationship('ItemOrder', back_populates='pedido')

    restaurante_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurante = relationship('Restaurant', back_populates='pedidos', uselist=False)

    avaliacao = relationship('Avaliacao', back_populates='pedido', uselist=False , cascade="all, delete-orphan")

    def to_dict(self):
        return {
        'pedido_id': self.id,
        'valor': self.valor,
        'data': self.data.isoformat(),
        'statusPedido': self.statusPedido.value,
        'metodo_pagamento': self.metodo_pagamento.value,
        'cliente_id': self.cliente_id,
        'restaurante_id': self.restaurante_id,
        'itens': [item.to_dict() for item in self.itens_pedidos]
        }
