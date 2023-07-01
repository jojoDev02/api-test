from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from models.item_restaurant import ItemRestaurant

class ItemOrder(Base):
    __tablename__ = 'item_order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer, nullable= False)
    valor = Column(Float, nullable=False) #quantity * item_restaurant.price

    item_restaurante_id = Column(Integer, ForeignKey('item_restaurant.id'))
    item_restaurante = relationship('ItemRestaurant', back_populates='itens_pedidos')

    pedido_id = Column(Integer, ForeignKey('order.id'))
    pedido = relationship('Order', back_populates='itens_pedidos')


    def to_dict(self):
        return {
            'quantidade': self.quantidade,
            'valor': self.valor,
            'item_restaurante_id': self.item_restaurante_id,
            'pedido_id': self.pedido_id
        }