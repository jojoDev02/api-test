from sqlalchemy import exists, func, text
from models.item_restaurant import ItemRestaurant
from db.database import db_session
from sqlalchemy.sql.expression import or_, alias, and_
from models.item_restriction_association import ItemRestrictionAssociation

from models.restriction import Restriction



class ItemRestaurantRepository:
    def get_items_restarant_all(self, restaurante_id):
        return db_session.query(ItemRestaurant).filter_by(restaurante_id=restaurante_id).all()
    
    def get_item_restaurant_by_id(self, item_id):
        return db_session.query(ItemRestaurant).get(item_id)
    
    def get_item_restaurant_by_name(self, nome):
        return db_session.query(ItemRestaurant).filter_by(nome = nome).first()

    def create_item_restaurant(self,**kwargs):
        restricoes = kwargs.pop('restricoes',[])
        item_restaurante = ItemRestaurant(**kwargs)

        if restricoes:
            restricoes_existentes = db_session.query(Restriction).filter(Restriction.id.in_(restricoes)).all()
            item_restaurante.restricoes = restricoes_existentes

        db_session.add(item_restaurante)
        db_session.commit()
        return item_restaurante

    def update_item_restaurant(self, item_restaurante, **kwargs):
        for key, value in kwargs.items():
            setattr(item_restaurante, key, value)
        db_session.commit()
        return item_restaurante
  
    def delete_item_restaurant(self, item_restaurante):
        db_session.delete(item_restaurante)
        db_session.commit()
   
   #retorna todos os itens que tenham a palavra buscada
    def search_itens(self, termo_buscado):
        return db_session.query(ItemRestaurant).filter(ItemRestaurant.nome.ilike(f"%{termo_buscado}%")).all()
    



    
    def search_itens_personalizada(self, termo_buscado, filtros=None, sort=None, order=None):
    
        query =  db_session.query(ItemRestaurant).filter(ItemRestaurant.nome.ilike(f"%{termo_buscado}%"), ItemRestaurant.restricoes.any(Restriction.nome.in_(filtros))).all()


        # if sort and order:
        #     if sort == 'alfa':
        #         if order== 'asc':
        #             return query.order_by(ItemRestaurant.nome.asc()).all()
        #         elif order == 'desc':
        #             return query.order_by(ItemRestaurant.nome.desc()).all()
        #     if sort == 'preco':
        #         if order== 'asc':
        #             return query.order_by(ItemRestaurant.preco.asc()).all()
        #         elif order == 'desc':
        #             return query.order_by(ItemRestaurant.preco.desc()).all()
                   
        return query
            
