from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from db.database import Base

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    restaurants = relationship('Restaurant', back_populates='category_restaurant', uselist=True)


    
