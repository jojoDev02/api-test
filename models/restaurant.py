from sqlalchemy import Column, ForeignKey, Integer, String, Float, Time
from sqlalchemy.orm import relationship
from models.user import User
from models.restaurant_allergenic_ingredient_association import RestaurantAllergenicIngredientAssociation
from models.category import Category
from models.address import AddressRestaurant

class Restaurant(User):

    __tablename__ = 'restaurant'

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    cnpj = Column(String(14), unique=True, nullable=False)
    nome_fantasia = Column(String(100), nullable= False)
    razao_social = Column(String(100), nullable= False) 
    taxa_entrega = Column(Float, nullable=False)
    horario_abertura = Column(Time, nullable=False)
    horario_fechamento = Column(Time, nullable=False)

    categoria_id = Column(Integer, ForeignKey('category.id'))
    categoria_restaurante = relationship('Category', back_populates='restaurantes')

    itens = relationship('ItemRestaurant', back_populates='restaurante', cascade="all, delete-orphan")

    ingredientes_alergenicos = relationship('AllergenicIngredient', secondary='restaurant_allergenic_ingredient_association', back_populates='restaurantes')

    endereco = relationship('AddressRestaurant', back_populates='restaurante', uselist=False, cascade="all, delete-orphan")

    pedidos = relationship('Order', back_populates='restaurante')
    __mapper_args__ = {
        'polymorphic_identity': 'restaurant'
    }

    def to_dict(self):
        return {
            'id': self.id,
            'cnpj': self.cnpj,
            'email': self.email,
            'nome_fantasia': self.nome_fantasia,
            'razao_social': self.razao_social,
            'taxa_entrega': self.taxa_entrega,
            'horario_abertura': str(self.horario_abertura),
            'horario_fechamento': str(self.horario_fechamento),
            'categoria_restaurante': self.categoria_restaurante.to_dict(),
            'itens': [item.to_dict() for item in self.itens],
            'ingredientes_alergenicos': [ingrediente.to_dict() for ingrediente in self.ingredientes_alergenicos],
            'endereco': self.endereco.to_dict(),
            'pedidos': [pedido.to_dict() for pedido in self.pedidos]
        }






    