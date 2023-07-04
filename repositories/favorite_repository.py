from db.database import db_session
from models.favorite import Favorite
from models.item_restaurant import ItemRestaurant

class FavoriteRepository:

    def get_favorites(self, cliente):
        if cliente:
           return cliente.favoritos
            
    def get_favorite(self, cliente_id, item_id):
        return db_session.query(ItemRestaurant).filter(Favorite.cliente_id == cliente_id, Favorite.item_id == item_id).first()
    
    def add_favorite(self, cliente, item):
        favorito = Favorite(cliente_id = cliente.id, item_id= item.id)
        db_session.add(favorito)
        db_session.commit()
        return favorito

    def remove_favorite(self, favorite):
        if favorite:
            db_session.delete(favorite)
            db_session.commit()