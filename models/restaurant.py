from sqlalchemy import Column, ForeignKey, Integer, String, Float, Time
from sqlalchemy.orm import relationship
from models.user import User

class Restaurant(User):

    __tablename__ = 'restaurant'

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    cnpj = Column(String(14), unique=True, nullable=False)
    fantasy_name = Column(String(100), nullable= False)
    corporate_name = Column(String(100), nullable= False) 
    delivery_fee = Column(Float, nullable=False)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='restaurants', uselist=False)

    

    __mapper_args__ = {
        'polymorphic_identity': 'restaurant'
    }

#relate to Address
#relate to Category
#relate to ItemRestaurant
#relate to AllergenicIngredient 
        



    