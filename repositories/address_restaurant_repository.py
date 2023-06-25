from db.database import db_session
from models.address import AddressRestaurant

class AddressRestaurantRepository:
    #revisar o fluxo de criacao do restaurant
    def create_address(self, **kwargs):
        address_restaurant = AddressRestaurant(**kwargs)
        db_session.add(address_restaurant)
        db_session.commit()
        return address_restaurant

    def get_address_by_id(self, address_id):
        return db_session.query(AddressRestaurant).get(address_id)

    def update_address(self, address_restaurant, **kwargs):
        for key, value in kwargs.items():
            setattr(address_restaurant, key, value)
        db_session.commit()
        return address_restaurant
