from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key= True, autoincrement= True)
    email = Column(String, unique= True, nullable= False)
    password = Column(String, unique= True, nullable= False)
    user_type = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_on': user_type,
        'polymorphic_identity': 'user'
    }

