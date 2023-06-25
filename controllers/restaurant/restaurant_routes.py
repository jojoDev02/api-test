from flask import Blueprint, jsonify, request
from db.database import db_session

from repositories.restaurant_repository import RestaurantRepository


restaurant_bp = Blueprint("restaurant", __name__)

@restaurant_bp.route("/restaurants", methods = ['GET'])
def get_restaurants():
    restaurants = RestaurantRepository.get_restarant_all()

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
    restaurant = RestaurantRepository.get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    return jsonify({'id': restaurant.id,
                    'email': restaurant.email,
                    'cnpj': restaurant.cnpj,
                    'fantasy_name': restaurant.fantasy_name,
                    'corporate_name': restaurant.corporate_name,
                    'delivery_fee': restaurant.delivery_fee,
                    'opening_time': str(restaurant.opening_time),
                    'closing_time': str(restaurant.closing_time)})

@restaurant_bp.route("/restaurants", methods = ['POST'])
def create_restaurant():
    data = request.get_json()

    restaurant = RestaurantRepository.create_restaurant(**data)

    return jsonify({'id': restaurant.id,
                    'email': restaurant.email,
                    'cnpj': restaurant.cnpj,
                    'fantasy_name': restaurant.fantasy_name,
                    'corporate_name': restaurant.corporate_name,
                    'delivery_fee': restaurant.delivery_fee,
                    'opening_time': str(restaurant.opening_time),
                    'closing_time': str(restaurant.closing_time)})

@restaurant_bp.route("/restaurants/<int:restaurant_id", methods = ['PUT'])
def update_restaurant(restaurant_id):
    restaurant = RestaurantRepository.get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    data=request.data

    restaurant = RestaurantRepository.update_restaurant(restaurant_id, **data)

    return jsonify({'id': restaurant.id,
                    'email': restaurant.email,
                    'cnpj': restaurant.cnpj,
                    'fantasy_name': restaurant.fantasy_name,
                    'corporate_name': restaurant.corporate_name,
                    'delivery_fee': restaurant.delivery_fee,
                    'opening_time': str(restaurant.opening_time),
                    'closing_time': str(restaurant.closing_time)})

@restaurant_bp.route("/restaurants/<int:restaurant_id>", methods= ['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = RestaurantRepository.get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    RestaurantRepository.delete_restaurant(restaurant_id)
    
    return jsonify({'message': 'Restaurant deleted successfully'}), 200


