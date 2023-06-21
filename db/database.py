from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base




#engine = create_engine('mysql+mysqlconnector://root:123456@localhost/db-pickfood')
engine = create_engine('sqlite:///db/database.db')

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

from models.user import User
from models.customer import Customer
from models.restaurant import Restaurant
from models.address import Address
from models.order import Order
from models.allergenic_ingredient import AllergenicIngredient
from models.category import Category
from models.item_restaurant import ItemRestaurant
from models.restriction import Restriction


def init_db():
    Base.metadata.create_all(bind=engine)
    

