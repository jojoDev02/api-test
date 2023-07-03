from models.restaurant import Restaurant
from db.database import db_session
from datetime import datetime, time

class RestaurantRepository:
    def get_restarant_all(self):
        return db_session.query(Restaurant).all()
    
    def get_restaurant_by_id(self, restaurante_id):
        return db_session.query(Restaurant).get(restaurante_id)
    
    def get_restaurant_by_name(self, name):
        return db_session.query(Restaurant).filter_by(name = name).first()

    def create_restaurant(self, **kwargs):
        horario_abertura = time.fromisoformat(kwargs.get('horario_abertura'))
        horario_fechamento = time.fromisoformat(kwargs.get('horario_fechamento'))
    
        restaurante = Restaurant(**kwargs)
        restaurante.horario_abertura = horario_abertura
        restaurante.horario_fechamento = horario_fechamento
   
        db_session.add(restaurante)
        db_session.commit()
        return restaurante

    def update_restaurant(self, restaurante, **kwargs):
        if restaurante:
            for key, value in kwargs.items():
                setattr(restaurante, key, value)

            restaurante.horario_abertura = time.fromisoformat(kwargs.get('horario_abertura'))
            restaurante.horario_fechamento = time.fromisoformat(kwargs.get('horario_fechamento'))
            db_session.commit()

        return restaurante

    def delete_restaurant(self, restaurante):
        if restaurante:
            db_session.delete(restaurante)
            db_session.commit()

    
    def search_restaurants(self, termo_buscado):
        return db_session.query(Restaurant).filter(Restaurant.nome_fantasia.ilike(f"%{termo_buscado}%")).all()
    
    def search_restaurants_personalizada(self, termo_buscado, sort, order):

        query = db_session.query(Restaurant).filter(Restaurant.nome_fantasia.ilike(f"%{termo_buscado}%"))
        if sort == 'alfa':
            if order== 'asc':
                return query.order_by(Restaurant.nome_fantasia.asc()).all()
            elif order == 'desc':
                return query.order_by(Restaurant.nome_fantasia.desc()).all()
            # elif sort == 'avaliacao':
            #     if sort == 'asc':
            #         query = query.order_by(Restaurant.avaliacao.asc())
            #     elif sort == 'desc':
            #         query = query.order_by(Restaurant.avaliacao.desc())
