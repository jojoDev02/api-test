from models.item_restaurant import ItemRestaurant
from db.database import db_session
from sqlalchemy.sql.expression import or_



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
   
   #retorna todos os itens que tenham a palavra buscada
    def search_itens(self, nome_item):
        return db_session.query(ItemRestaurant).filter(ItemRestaurant.nome.ilike(f"%{nome_item}%")).all()
    
    def search_itens_personalizada(self, termo_buscado, sort, order, filtros=None):
        
        query = db_session.query(ItemRestaurant).filter(ItemRestaurant.nome.ilike(f"%{termo_buscado}%"))

        if filtros:
            restricoes = [ItemRestaurant.restricoes.any(restricao) for restricao in filtros]
            query = query.filter(or_(*restricoes))

        if sort == 'alfa':
            if order== 'asc':
                return query.order_by(ItemRestaurant.nome.asc()).all()
            elif order == 'desc':
                return query.order_by(ItemRestaurant.nome.desc()).all()
        if sort == 'preco':
            if order== 'asc':
                return query.order_by(ItemRestaurant.preco.asc()).all()
            elif order == 'desc':
                return query.order_by(ItemRestaurant.preco.desc()).all()
            
        return query
            
