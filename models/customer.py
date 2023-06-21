from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.user import User

class Customer(User):

    __tablename__ = 'customer'

    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    cpf = Column(String(11), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(11), nullable=False)


    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }

            
#relacionar com Adress
#relacionar com Order
