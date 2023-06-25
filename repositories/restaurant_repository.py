from models.restaurant import Restaurant
from db.database import db_session
from datetime import datetime, time

class RestaurantRepository:
    def get_restarant_all(self):
        return db_session.query(Restaurant).all()
    
    def get_restaurant_by_id(self, restaurant_id):
        return db_session.query(Restaurant).get(restaurant_id)
    
    def get_restaurant_by_name(self, name):
        return db_session.query(Restaurant).filter_by(name = name).first()

    def create_restaurant(self, **kwargs):
        opening_time = time.fromisoformat(kwargs.get('opening_time'))
        closing_time = time.fromisoformat(kwargs.get('closing_time'))
    
        restaurant = Restaurant(**kwargs)
        restaurant.opening_time = opening_time
        restaurant.closing_time = closing_time
   
        db_session.add(restaurant)
        db_session.commit()
        return restaurant

    def update_restaurant(self, restaurant, **kwargs):
        if restaurant:
            for key, value in kwargs.items():
                setattr(restaurant, key, value)

            restaurant.opening_time = time.fromisoformat(kwargs.get('opening_time'))
            restaurant.closing_time = time.fromisoformat(kwargs.get('closing_time'))
            db_session.commit()


        
        return restaurant

    def delete_restaurant(self, restaurant):
        if restaurant:
            db_session.delete(restaurant)
            db_session.commit()


