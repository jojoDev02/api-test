from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base
from models.restaurant_allergenic_ingredient_association import RestaurantAllergenicIngredientAssociation

class AllergenicIngredient(Base):
    __tablename__ = 'allergenic_ingredient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    restaurants = relationship("restaurant", secondary='restaurant_allergenic_ingredient_association', backref="allergenic_ingredients")

    def __init__(self, name):
        self.name = name
    