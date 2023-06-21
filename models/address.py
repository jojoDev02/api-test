from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Address(Base):

    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(20), nullable=True)
    cep = Column(String(8), nullable=False)
    street= Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    neighborhood = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)
    complement= Column(String(100), nullable=True)

    

    def __init__(self, nickname, cep, street, state, city, neighborhood, number, complement):
        self.nickname = nickname
        self.cep = cep
        self.street = street
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.number = number
        self.complement = complement

    

    
    #relacionar com costumer and restaurant


