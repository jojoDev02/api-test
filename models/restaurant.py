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
    fantasy_name = Column(String(100), nullable= False)
    corporate_name = Column(String(100), nullable= False) 
    delivery_fee = Column(Float, nullable=False)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'))
    category_restaurant = relationship('Category', back_populates='restaurants')

    items = relationship('ItemRestaurant', back_populates='restaurant', cascade="all, delete-orphan")

    allergenic_ingredients = relationship('AllergenicIngredient', secondary='restaurant_allergenic_ingredient_association', back_populates='restaurants')

    address = relationship('AddressRestaurant', back_populates='restaurant', uselist=False, cascade="all, delete-orphan")

    __mapper_args__ = {
        'polymorphic_identity': 'restaurant'
    }

#relate to Address





    