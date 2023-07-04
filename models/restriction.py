from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Restriction(Base):

    __tablename__ = 'restriction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False, unique=True)

    itens_restaurante = relationship("ItemRestaurant", secondary='item_restriction_association', back_populates='restricoes')

    def to_dict(self):
        return {
            'nome': self.nome
        }