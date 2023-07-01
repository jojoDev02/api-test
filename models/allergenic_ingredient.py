from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class AllergenicIngredient(Base):
    __tablename__ = 'allergenic_ingredient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    restaurantes = relationship('Restaurant', secondary='restaurant_allergenic_ingredient_association', back_populates="ingredientes_alergenicos")

    