from flask import Blueprint, jsonify, request
from db.database import db_session

from repositories.restaurant_repository import RestaurantRepository
from repositories.address_restaurant_repository import AddressRestaurantRepository


restaurant_bp = Blueprint("restaurant", __name__)

restaurant_repository = RestaurantRepository()
address_repository = AddressRestaurantRepository()


@restaurant_bp.route("/restaurants", methods = ['GET'])
def get_restaurants():
    restaurants = restaurant_repository.get_restarant_all()

    if not restaurants:
        return jsonify({'message': 'No restaurants found'}), 404
    
    restaurants_list = [
        {'id': restaurant.id,
                'cnpj': restaurant.cnpj,
                'fantasy_name': restaurant.fantasy_name,
                'corporate_name': restaurant.corporate_name,
                'delivery_fee': restaurant.delivery_fee,
                'opening_time': str(restaurant.opening_time),
                'closing_time': str(restaurant.closing_time)}
        for restaurant in restaurants
    ]

    return jsonify({'restaurants': restaurants_list})


@restaurant_bp.route("/restaurants/<int:restaurant_id>", methods = ['GET'])
def get_restaurant_by_id(restaurant_id):
    restaurant = restaurant_repository.get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    return jsonify({'id': restaurant.id,
                    'email': restaurant.email,
                    'cnpj': restaurant.cnpj,
                    'fantasy_name': restaurant.fantasy_name,
                    'corporate_name': restaurant.corporate_name,
                    'delivery_fee': restaurant.delivery_fee,
                    'opening_time': str(restaurant.opening_time),
                    'closing_time': str(restaurant.closing_time),
                        'address': {
                            'id': restaurant.address.id,
                            'cep': restaurant.address.cep,
                            'street': restaurant.address.street,
                            'state': restaurant.address.state,
                            'city': restaurant.address.city,
                            'neighborhood': restaurant.address.neighborhood,
                            'number': restaurant.address.number,
                            'complement': restaurant.address.complement
                        }
                    })

@restaurant_bp.route("/restaurants", methods = ['POST'])
def create_restaurant():
    data = request.get_json()

    address_data = data.pop('address', None)
    if not address_data:
        return jsonify({'error': 'Address data is required'}), 400

    
    restaurant = restaurant_repository.create_restaurant(**data)

    address_data['restaurant_id'] = restaurant.id
    address = address_repository.create_address(**address_data)
    restaurant.address = address

    return jsonify({
        'id': restaurant.id,
        'email': restaurant.email,
        'cnpj': restaurant.cnpj,
        'fantasy_name': restaurant.fantasy_name,
        'corporate_name': restaurant.corporate_name,
        'delivery_fee': restaurant.delivery_fee,
        'opening_time': str(restaurant.opening_time),
        'closing_time': str(restaurant.closing_time),
        'address': {
            'id': restaurant.address.id,
            'cep': restaurant.address.cep,
            'street': restaurant.address.street,
            'state': restaurant.address.state,
            'city': restaurant.address.city,
            'neighborhood': restaurant.address.neighborhood,
            'number': restaurant.address.number,
            'complement': restaurant.address.complement
        }
})


@restaurant_bp.route("/restaurants/<int:restaurant_id>", methods = ['PUT'])
def update_restaurant(restaurant_id):
    restaurant = restaurant_repository.get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    data=request.json

    restaurant = restaurant_repository.update_restaurant(restaurant, **data)

    return jsonify({'id': restaurant.id,
                    'email': restaurant.email,
                    'cnpj': restaurant.cnpj,
                    'fantasy_name': restaurant.fantasy_name,
                    'corporate_name': restaurant.corporate_name,
                    'delivery_fee': restaurant.delivery_fee,
                    'opening_time': str(restaurant.opening_time),
                    'closing_time': str(restaurant.closing_time)})

@restaurant_bp.route("/restaurants/<int:restaurant_id>/addresses", methods = ['PUT'])
def update_restaurant_address(restaurant_id):
    restaurant = restaurant_repository.get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    data = request.json

    address = address_repository.get_address_by_id(restaurant.address.id)

    if address:
        address_repository.update_address(address, **data)

    return jsonify({
        'address': {
            'id': restaurant.address.id,
            'restaurant_id': restaurant.address.restaurant_id,
            'nickname': restaurant.address.nickname,
            'cep': restaurant.address.cep,
            'street': restaurant.address.street,
            'state': restaurant.address.state,
            'city': restaurant.address.city,
            'neighborhood': restaurant.address.neighborhood,
            'number': restaurant.address.number,
            'complement': restaurant.address.complement
        }
    })


@restaurant_bp.route("/restaurants/<int:restaurant_id>", methods= ['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = restaurant_repository.get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    restaurant_repository.delete_restaurant(restaurant)
    
    return jsonify({'message': 'Restaurant deleted successfully'}), 200


