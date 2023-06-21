from flask import Blueprint, jsonify, request
from db.database import db_session
from models.restaurant import Restaurant


restaurante_bp = Blueprint("restaurante", __name__)

@restaurante_bp.route("/restaurantes", methods = ['GET'])
def get_restaurantes():
    restaurants = Restaurant.query.all()
    results = []
    for restaurant in restaurants:
        results.append({
            'cnpj': restaurant.cnpj,
            'fantasy_name': restaurant.fantasy_name,
            'corporate_name': restaurant.corporate_name,
            'delivery_fee': restaurant.delivery_fee,
            'opening_time': str(restaurant.opening_time),
            'closing_time': str(restaurant.closing_time)
        })
    return jsonify(results)


@restaurante_bp.route("/restaurantes/<name>", methods = ['GET'])
def get_restaurante_by_name(name):
    return "dados do restaurante" + name

@restaurante_bp.route("/restaurantes", methods = ['POST'])
def create_restaurante():
    data = request.get_json()
    restaurant = Restaurant(**data)
    db_session.add(restaurant)
    db_session.commit()
    return jsonify({'message': 'Restaurant created successfully'})

@restaurante_bp.route("/restaurantes", methods = ['PUT'])
def update_restaurante():
    return "restaurante atualizado"

@restaurante_bp.route("/restaurantes", methods= ['DELETE'])
def delete_restaurante():
    return "restaurante apagado"


