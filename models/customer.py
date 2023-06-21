from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .user import User

class Customer(User):

    __tablename__ = 'customer'

    cpf = Column(String(11), primary_key=True, nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(11), nullable=False)

    orders = relationship("Order", backref='customer_id')


    __mapper_args__ = {
        'polymorphic_identity': 'customer',
        'inherit_condition': (User.id == cpf)
    }

    def __init__(self, cpf, name, phone_number, **kwargs):
            super().__init__(**kwargs)
            self.cpf = cpf
            self.name = name
            self.phone_number = phone_number
            
#relacionar com adress
