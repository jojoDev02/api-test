from flask import Blueprint, jsonify, request

from repositories.restaurant_repository import RestaurantRepository
from repositories.address_restaurant_repository import AddressRestaurantRepository


restaurant_bp = Blueprint("restaurante", __name__)

restaurant_repository = RestaurantRepository()
address_repository = AddressRestaurantRepository()


@restaurant_bp.route("/restaurantes", methods = ['GET'])
def get_restaurants():
    restaurantes = restaurant_repository.get_restarant_all()

    if not restaurantes:
        return jsonify({'message': 'No restaurantes found'}), 404
    
    restaurants_list = [restaurante.to_dict() for restaurante in restaurantes]

    return jsonify({'restaurantes': restaurants_list})


@restaurant_bp.route("/restaurantes/<int:restaurante_id>", methods = ['GET'])
def get_restaurant_by_id(restaurante_id):
    restaurante = restaurant_repository.get_restaurant_by_id(restaurante_id)

    if not restaurante:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    return jsonify(restaurante.to_dict())

@restaurant_bp.route("/restaurantes", methods = ['POST'])
def create_restaurant():
    data = request.get_json()

    address_data = data.pop('endereco', None)
    if not address_data:
        return jsonify({'error': 'Address data is required'}), 400

    
    restaurante = restaurant_repository.create_restaurant(**data)

    address_data['restaurante_id'] = restaurante.id
    endereco = address_repository.create_address(**address_data)
    restaurante.endereco = endereco

    return jsonify(restaurante.to_dict())


@restaurant_bp.route("/restaurantes/<int:restaurante_id>", methods = ['PUT'])
def update_restaurant(restaurante_id):
    restaurante = restaurant_repository.get_restaurant_by_id(restaurante_id)

    if not restaurante:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    data=request.get_json()

    restaurante = restaurant_repository.update_restaurant(restaurante, **data)

    return jsonify(restaurante.to_dict())

@restaurant_bp.route("/restaurantes/<int:restaurante_id>/enderecos", methods = ['PUT'])
def update_restaurant_address(restaurante_id):
    restaurante = restaurant_repository.get_restaurant_by_id(restaurante_id)

    if not restaurante:
        return jsonify({'error': 'Restaurant not found'}), 404

    data = request.get_json()

    endereco = address_repository.get_address_by_id(restaurante.endereco.id)

    if endereco:
        address_repository.update_address(endereco, **data)

    return jsonify(endereco.to_dict())

@restaurant_bp.route("/restaurantes/<int:restaurante_id>", methods= ['DELETE'])
def delete_restaurant(restaurante_id):
    restaurante = restaurant_repository.get_restaurant_by_id(restaurante_id)

    if not restaurante:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    restaurant_repository.delete_restaurant(restaurante)
    
    return jsonify({'message': 'Restaurant deleted successfully'}), 200


# @restaurant_bp.route('/int:restaurante_id/orders', methods=['GET'])
# def get_orders_by_restaurant(restaurante_id):
#     #orders = db_session.query(Order).filter_by(restaurante_id=restaurante_id).all()
#     #orders_data = [] 
#     pass