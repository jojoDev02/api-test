from models.item_restaurant import ItemRestaurant
from db.database import db_session

class ItemRestaurantRepository:
    def get_items_restarant_all(self, restaurant_id):
        return db_session.query(ItemRestaurant).filter_by(restaurant_id=restaurant_id).all()
    
    def get_item_restaurant_by_id(self, item_id):
        return db_session.query(ItemRestaurant).get(item_id)
    
    def get_item_restaurant_by_name(self, name):
        return db_session.query(ItemRestaurant).filter_by(name = name).first()

    def create_item_restaurant(self, **kwargs):
        item_restaurant = ItemRestaurant(**kwargs)
        db_session.add(item_restaurant)
        db_session.commit()
        return item_restaurant

    def update_item_restaurant(self, item_restaurant, **kwargs):
        for key, value in kwargs.items():
            setattr(item_restaurant, key, value)
        db_session.commit()
        return item_restaurant
  
    def delete_item_restaurant(self, item_restaurant):
        db_session.delete(item_restaurant)
        db_session.commit()
   
