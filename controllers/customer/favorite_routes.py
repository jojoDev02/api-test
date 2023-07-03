from flask import Blueprint, jsonify, request


favorite_bp =  Blueprint("favorite", __name__)

@favorite_bp.route('/clientes/<int:cliente_id>/favoritos', methods=['GET'])
def get_favorites(cliente_id):
    pass

@favorite_bp.route('/clientes/<int:cliente_id>/favoritos/<int:item_id>', methods=['POST'])
def add_favorite(cliente_id,item_id):
    pass

@favorite_bp.route('/clientes/<int:cliente_id>/favoritos/<int:item_id>', methods=['DELETE'])
def delete_favorite(cliente_id,item_id):
    pass