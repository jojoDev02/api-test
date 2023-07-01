from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from models.restaurant import Restaurant
from models.restriction import Restriction
from models.item_restriction_association import ItemRestrictionAssociation

class ItemRestaurant(Base):
    __tablename__ = 'item_restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    preco = Column(Float, nullable=False)
    nome = Column(String, nullable=False)
    descricao = Column(String(255), nullable=False)
    url_imagem = Column(String, nullable=True)
    
    restaurante_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurante = relationship('Restaurant', back_populates='itens', uselist= False)

    restricoes = relationship("Restriction", secondary= 'item_restriction_association', back_populates='itens_restaurante')

    itens_pedidos = relationship("ItemOrder", back_populates='item_restaurante')

    #relate to favorite

    def to_dict(self):
        return {
            'id': self.id,
            'preco': self.preco,
            'nome': self.nome,
            'descricao': self.descricao,
            'url_imagem': self.url_imagem,
            'restaurante': self.restaurante.to_dict(),
            'restricoes': [restricao.to_dict() for restricao in self.restricoes]
        }