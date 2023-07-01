from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from db.database import Base

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    restaurantes = relationship('Restaurant', back_populates='categoria_restaurante', uselist=True)


    
