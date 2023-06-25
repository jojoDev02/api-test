from models.restaurant import Restaurant
from db.database import db_session

class RestaurantRepository:
    def get_restarant_all():
        return db_session.query(Restaurant).all()
    
    def get_restaurant_by_id(self, restaurant_id):
        return db_session.query(Restaurant).get(restaurant_id)
    
    def get_restaurant_by_name(self, name):
        return db_session.query(Restaurant).filter_by(name = name).first()

    def create_restaurant(self,email, password, cnpj, fantasy_name, corporate_name, delivery_fee, opening_time, closing_time, category_id):
        restaurant = Restaurant(
            email=email,
            password=password,
            cnpj=cnpj,
            fantasy_name=fantasy_name,
            corporate_name=corporate_name,
            delivery_fee=delivery_fee,
            opening_time=opening_time,
            closing_time=closing_time,
            category_id=category_id
        )
        db_session.add(restaurant)
        db_session.commit()
        return restaurant

    def update_restaurant(self,email, restaurant_id, fantasy_name, corporate_name, delivery_fee, opening_time, closing_time):
        restaurant = self.get_restaurant_by_id(restaurant_id)
        if restaurant:
            restaurant.email= email,
            restaurant.fantasy_name = fantasy_name
            restaurant.corporate_name = corporate_name
            restaurant.delivery_fee = delivery_fee
            restaurant.opening_time = opening_time
            restaurant.closing_time = closing_time
            db_session.commit()
            return restaurant

    def delete_restaurant(self, restaurant_id):
        restaurant = self.get_restaurant_by_id(restaurant_id)
        if restaurant:
            db_session.delete(restaurant)
            db_session.commit()


