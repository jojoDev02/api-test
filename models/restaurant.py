from sqlalchemy import Column, ForeignKey, Integer, String, Float, Time
from sqlalchemy.orm import relationship
from .user import User

class Restaurant(User):

    __tablename__ = 'restaurant'


    cnpj = Column(Integer, primary_key=True, unique=True)
    fantasy_name = Column(String(100))
    corporate_name = Column(String(100)) 
    delivery_fee = Column(Float, nullable=False)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))

    items = relationship("ItemRestaurant", backref='restaurant_items')
    allergenic_ingredients = relationship('AllergenicIngredient', secondary= 'restaurant_allergenic_ingredient_association', backref='restaurant')

    __mapper_args__ = {
        'polymorphic_identity': 'restaurant',
        'inherit_condition': (User.id == cnpj)
    }

    def __init__(self, username, password, email, cnpj, fantasy_name, corporate_name, delivery_fee, opening_time, closing_time):
        super().__init__(username, password, email)
        self.cnpj = cnpj
        self.fantasy_name = fantasy_name
        self.corporate_name = corporate_name
        self.delivery_fee = delivery_fee
        self.opening_time = opening_time
        self.closing_time = closing_time
    
        



    