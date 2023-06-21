from flask import Blueprint, jsonify, request
from db.database import db_session
from models.restaurant import Restaurant


restaurant_bp = Blueprint("restaurant", __name__)

@restaurant_bp.route("/restaurants", methods = ['GET'])
def get_restaurants():
    return "restaurant list"


@restaurant_bp.route("/restaurants/<string:name>", methods = ['GET'])
def get_restaurant_by_name(name):
    return "restaurant data " + name

@restaurant_bp.route("/restaurants", methods = ['POST'])
def create_restaurant():
    data = request.get_json()
    restaurant = Restaurant(**data)
    db_session.add(restaurant)
    db_session.commit()
    return jsonify({'message': 'Restaurant created successfully'})

@restaurant_bp.route("/restaurants", methods = ['PUT'])
def update_restaurant():
    return "restaurant updated"

@restaurant_bp.route("/restaurants", methods= ['DELETE'])
def delete_restaurant():
    return "restaurant deleted"


