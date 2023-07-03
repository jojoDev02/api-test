from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.database import Base


class Avaliacao(Base):
    __tablename__ = 'avaliacoes'
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('order.id'))
    nota = Column(Float)
    pedido = relationship('Order', back_populates='avaliacao')

    def to_dict(self):
        return {
            'id': self.id,
            'pedido_id': self.pedido_id,
            'nota': self.nota
        }