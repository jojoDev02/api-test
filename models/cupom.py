from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Cupom(Base):

    __tablename__ = 'cupom'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(11), nullable=False)
    desconto= Column(Float, nullable=False)
    valor_minimo= Column(Float, nullable=False)

    restaurante_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurante = relationship('Restaurant', back_populates='cupons', uselist=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "desconto": self.desconto,
            "valor_minimo": self.valor_minimo,
            "restaurante_id": self.restaurante_id
        }