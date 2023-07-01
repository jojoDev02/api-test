from models.item_restaurant import ItemRestaurant
from db.database import db_session

class ItemRestaurantRepository:
    def get_items_restarant_all(self, restaurante_id):
        return db_session.query(ItemRestaurant).filter_by(restaurante_id=restaurante_id).all()
    
    def get_item_restaurant_by_id(self, item_id):
        return db_session.query(ItemRestaurant).get(item_id)
    
    def get_item_restaurant_by_name(self, nome):
        return db_session.query(ItemRestaurant).filter_by(nome = nome).first()

    def create_item_restaurant(self, **kwargs):
        item_resaturante = ItemRestaurant(**kwargs)
        db_session.add(item_resaturante)
        db_session.commit()
        return item_resaturante

    def update_item_restaurant(self, item_resaturante, **kwargs):
        for key, value in kwargs.items():
            setattr(item_resaturante, key, value)
        db_session.commit()
        return item_resaturante
  
    def delete_item_restaurant(self, item_resaturante):
        db_session.delete(item_resaturante)
        db_session.commit()
   
