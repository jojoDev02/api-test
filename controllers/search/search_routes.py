from flask import Blueprint, jsonify, request
from repositories.item_repository import ItemRestaurantRepository

from repositories.restaurant_repository import RestaurantRepository


search_bp = Blueprint("search", __name__)

restaurante_repo = RestaurantRepository()
item_repo = ItemRestaurantRepository()
@search_bp.route('/restaurantes')
def search_restaurantes():

    query = request.args.get('q')
    sort = request.args.get('sort')
    order = request.args.get('order')

    if query and sort and order:
        restaurantes = restaurante_repo.search_restaurants_personalizada(query, sort, order)
    else:
        restaurantes = restaurante_repo.search_restaurants(query)

    restaurantes_list = [restaurante.to_dict() for restaurante in restaurantes]

    return jsonify(restaurantes_list),200

@search_bp.route('/itens', methods=['GET'])
def search_itens():

    query = request.args.get('q')
    sort = request.args.get('sort')
    order = request.args.get('order')
    filtros = request.args.get('restricoes').split(',')

    #verificar como ta sendo passado o encode

    if query and sort and order and filtros:
        itens = item_repo.search_itens_personalizada(query, sort, order, filtros)
    elif query and sort and order:
        itens = item_repo.search_itens_personalizada(query, sort, order)
    elif query and filtros:
        itens= item_repo.search_itens_personalizada(query, filtros)
    else:
        itens = item_repo.search_itens(query)

    if filtros:
        itens = item_repo.search_itens_personalizada(query,filtros)

    item_list = [item.to_dict() for item in itens]

    return jsonify(item_list),200
    
