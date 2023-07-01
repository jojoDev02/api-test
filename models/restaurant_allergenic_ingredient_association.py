from sqlalchemy import Column, ForeignKey, Integer, String
from db.database import Base
from models.allergenic_ingredient import AllergenicIngredient


class RestaurantAllergenicIngredientAssociation(Base):

    __tablename__ = 'restaurant_allergenic_ingredient_association'

    restaurante_id = Column(String, ForeignKey('restaurant.cnpj'), primary_key=True)
    ingrediente_alergenico_id = Column(Integer, ForeignKey('allergenic_ingredient.id'), primary_key=True)