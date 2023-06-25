from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class AllergenicIngredient(Base):
    __tablename__ = 'allergenic_ingredient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    restaurants = relationship('Restaurant', secondary='restaurant_allergenic_ingredient_association', back_populates="allergenic_ingredients")

    