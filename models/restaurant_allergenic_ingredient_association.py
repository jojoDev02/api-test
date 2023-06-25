from sqlalchemy import Column, ForeignKey, Integer, String
from db.database import Base
from models.allergenic_ingredient import AllergenicIngredient


class RestaurantAllergenicIngredientAssociation(Base):

    __tablename__ = 'restaurant_allergenic_ingredient_association'

    restaurant_id = Column('restaurant_id', String, ForeignKey('restaurant.cnpj'), primary_key=True)
    allergenic_ingredient_id = Column('allergenic_ingredient_id', Integer, ForeignKey('allergenic_ingredient.id'), primary_key=True)