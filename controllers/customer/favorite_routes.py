from flask import Blueprint, jsonify, request
from repositories.customer_repository import CustomerRepository

from repositories.favorite_repository import FavoriteRepository
from repositories.item_repository import ItemRestaurantRepository


favorite_bp =  Blueprint("favorite", __name__, url_prefix='/clientes')
favorite_repo = FavoriteRepository()
customer_repo = CustomerRepository()
item_repo = ItemRestaurantRepository()

@favorite_bp.route('/<int:cliente_id>/favoritos', methods=['GET'])
def get_favorites(cliente_id):
    cliente = customer_repo.get_customer_by_id(cliente_id)
    favoritos = favorite_repo.get_favorites(cliente)

    favoritos=[favorito.to_dict() for favorito in favoritos]
    return jsonify(favoritos)

@favorite_bp.route('/<int:cliente_id>/favoritos/<int:item_id>', methods=['POST'])
def add_favorite(cliente_id,item_id):
    cliente = customer_repo.get_customer_by_id(cliente_id)
    item = item_repo.get_item_restaurant_by_id(item_id)

    if not cliente:
        return jsonify({'message': 'Cliente não encontrado.'}), 404
    if not item:
        return jsonify({'message': 'Item não encontrado.'}), 404
    
    favorito = favorite_repo.add_favorite(cliente, item)
    return jsonify({
        'cliente_id': favorito.cliente_id,
        'item_id' : favorito.item_id
    }),200

@favorite_bp.route('/<int:cliente_id>/favoritos/<int:item_id>', methods=['DELETE'])
def delete_favorite(cliente_id,item_id):
    cliente = customer_repo.get_customer_by_id(cliente_id)
    item = item_repo.get_item_restaurant_by_id(item_id)

    if not cliente:
        return jsonify({'message': 'Cliente não encontrado.'}), 404
    if not item:
        return jsonify({'message': 'Item não encontrado.'}), 404

    favorito = favorite_repo.get_favorite(cliente_id, item_id)
    if not favorito:
        return jsonify({'message': 'Favorito não encontrado.'}), 404

    favorite_repo.remove_favorite(favorito)
    return jsonify({'message': 'Favorito excluído com sucesso.'}),200