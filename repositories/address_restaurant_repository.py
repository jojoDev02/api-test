from db.database import db_session
from models.address import AddressRestaurant

class AddressRestaurantRepository:
    #revisar o fluxo de criacao do restaurant
    def create_address(self, **kwargs):
        endereco_restaurante = AddressRestaurant(**kwargs)
        db_session.add(endereco_restaurante)
        db_session.commit()
        return endereco_restaurante

    def get_address_by_id(self, endereco_id):
        return db_session.query(AddressRestaurant).get(endereco_id)

    def update_address(self, endereco_restaurante, **kwargs):
        for key, value in kwargs.items():
            setattr(endereco_restaurante, key, value)
        db_session.commit()
        return endereco_restaurante
