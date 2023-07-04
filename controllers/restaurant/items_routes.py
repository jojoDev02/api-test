from flask import Blueprint, jsonify, request

from repositories.item_repository import ItemRestaurantRepository

items_bp = Blueprint('itens', __name__, url_prefix='/restaurantes')

item_repository = ItemRestaurantRepository()


@items_bp.route('/<int:restaurante_id>/itens', methods=['GET'])
def get_items(restaurante_id):
    itens = item_repository.get_items_restarant_all(restaurante_id)
    
    if not itens:
        return jsonify({'error': 'Items not found'}), 404

    itens = [item.to_dict() for item in itens]
    
    return jsonify(itens)

@items_bp.route('/<int:restaurante_id>/itens/<int:item_id>', methods=['GET'])
def get_item_by_id(restaurante_id,item_id):
    item = item_repository.get_item_restaurant_by_id(item_id)
    if not item or item.restaurante_id != restaurante_id:
        return jsonify({'error': 'Item not found'}), 404

    return jsonify(item.to_dict())

@items_bp.route('/<int:restaurante_id>/itens', methods=['POST'])
def create_item(restaurante_id):
    data = request.get_json()
    data['restaurante_id'] = restaurante_id
    item = item_repository.create_item_restaurant(**data)
    

    return jsonify(item.to_dict())

@items_bp.route('/<int:restaurante_id>/itens/<int:item_id>', methods=['PUT'])
def update_item(restaurante_id, item_id):
    item = item_repository.get_item_restaurant_by_id(item_id)
    if item and item.restaurante_id == restaurante_id:
        data = request.get_json()
        item = item_repository.update_item_restaurant(item, **data)

        return jsonify(item.to_dict)
    return jsonify({'error': 'Item not found'})

@items_bp.route('/<int:restaurante_id>/itens/<int:item_id>', methods=['DELETE'])
def delete_item(restaurante_id,item_id):
    item = item_repository.get_item_restaurant_by_id(item_id)
    if item and item.restaurante_id == restaurante_id:
        item_repository.delete_item_restaurant(item)

        return jsonify({'message': 'Item deleted successfully'}),200
    return jsonify({'error': 'Item or restaurant not found'}), 404
