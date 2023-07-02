from flask import Blueprint, jsonify, request
from repositories.cupom_repository import CupomRepository

cupom_bp = Blueprint('cupom', __name__, url_prefix='/restaurantes')

@cupom_bp.route('/<restaurante_id>/cupons',methods=['GET'])
def get_cupons(restaurante_id):
    pass


@cupom_bp.route('/<restaurante_id>/cupons/<cupom_id>', methods=['GET'])
def get_cupom_by_id(restaurante_id, cupom_id):
    pass

@cupom_bp.route('/<restaurante_id>/cupons', methods=['POST'])
def create_cupom(restaurante_id):
    pass

@cupom_bp.route('/<restaurante_id>/cupons/<cupom_id>', methods=['PUT'])
def update_cupom(restaurante_id):
    pass

@cupom_bp.route('/<restaurante_id>/cupons/<cupom_id>', methods=['DELETE'])
def delete_cupom(restaurante_id, cupom_id):
    pass
