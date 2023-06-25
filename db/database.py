from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# from models.order import Order
# from models.allergenic_ingredient import AllergenicIngredient

# from models.category import Category
# from models.restriction import Restriction

# from models.customer import Customer
# from models.restaurant import Restaurant
# from models.item_restaurant import ItemRestaurant
# from models.item_order import ItemOrder
# from models.item_restriction_association import ItemRestrictionAssociation
# from models.restaurant_allergenic_ingredient_association import RestaurantAllergenicIngredientAssociation



#engine = create_engine('mysql+mysqlconnector://root:123456@localhost/db-pickfood')
engine = create_engine('sqlite:///db/database.db', echo=True)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

from models import *
def init_db():
    
    Base.metadata.create_all(bind=engine)
    tabelas = Base.metadata.tables
    # Iterar sobre as tabelas e exibir seus nomes
    for tabela in tabelas:
        print(tabela)
    

