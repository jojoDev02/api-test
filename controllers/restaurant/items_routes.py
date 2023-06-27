from flask import Blueprint, jsonify, request

from repositories.item_repository import ItemRestaurantRepository

items_bp = Blueprint('items', __name__)

item_repository = ItemRestaurantRepository()


@items_bp.route('/<int:restaurant_id>/items', methods=['GET'])
def get_items(restaurant_id):
    items = item_repository.get_items_restarant_all(restaurant_id)
    if not items:
        return jsonify({'error': 'Items not found'}), 404

    items_data = []
    for item in items:
        item_data = {
            'id': item.id,
            'price': item.price,
            'name': item.name,
            'description': item.description,
            'url_image': item.url_image,
            'restaurant_id': item.restaurant_id
        }
        items_data.append(item_data)
    return jsonify(items_data)

@items_bp.route('/<int:restaurant_id>/items/<int:item_id>', methods=['GET'])
def get_item_by_id(restaurant_id,item_id):
    item = item_repository.get_item_restaurant_by_id(item_id)
    if not item or item.restaurant_id != restaurant_id:
        return jsonify({'error': 'Item not found'}), 404

    item_data = {
        'id': item.id,
        'price': item.price,
        'name': item.name,
        'description': item.description,
        'url_image': item.url_image,
        'restaurant_id': item.restaurant_id
    }
    return jsonify(item_data)

@items_bp.route('/<int:restaurant_id>/items', methods=['POST'])
def create_item(restaurant_id):
    data = request.json
    data['restaurant_id'] = restaurant_id
    item = item_repository.create_item_restaurant(**data)

    item_data = {
        'id': item.id,
        'price': item.price,
        'name': item.name,
        'description': item.description,
        'url_image': item.url_image,
        'restaurant_id': item.restaurant_id
    }

    return jsonify(item_data)

@items_bp.route('/<int:restaurant_id>/items/<int:item_id>', methods=['PUT'])
def update_item(restaurant_id, item_id):
    item = item_repository.get_item_restaurant_by_id(item_id)
    if item and item.restaurant_id == restaurant_id:
        data = request.json
        item = item_repository.update_item_restaurant(item, **data)

        item_data = {
            'id': item.id,
            'price': item.price,
            'name': item.name,
            'description': item.description,
            'url_image': item.url_image,
            'restaurant_id': item.restaurant_id
        }

        return jsonify(item_data)
    return jsonify({'error': 'Item not found'})

@items_bp.route('/<int:restaurant_id>/items/<int:item_id>', methods=['DELETE'])
def delete_item(restaurant_id,item_id):
    item = item_repository.get_item_restaurant_by_id(item_id)
    if item and item.restaurant_id == restaurant_id:
        item_repository.delete_item_restaurant(item)
        return jsonify({'message': 'Item deleted successfully'}),200
    return jsonify({'error': 'Item or restaurant not found'}), 404
