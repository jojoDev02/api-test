from flask import Blueprint, jsonify, request
from repositories.cupom_repository import CupomRepository

cupom_bp = Blueprint('cupom', __name__, url_prefix='/restaurantes')
cupom_repo = CupomRepository()
@cupom_bp.route('/<restaurante_id>/cupons',methods=['GET'])
def get_cupons(restaurante_id):
    cupons = cupom_repo.get_cupons(restaurante_id)

    cupons_list =[cupom.to_dict() for cupom in cupons]

    return jsonify(cupons_list),200



@cupom_bp.route('/<restaurante_id>/cupons/<cupom_id>', methods=['GET'])
def get_cupom_by_id(restaurante_id, cupom_id):
    cupom = cupom_repo.get_cupom_by_id(cupom_id)

    if cupom:
        return jsonify(cupom.to_dict()),200
    return jsonify({'message': 'cupom not found.'}),404


@cupom_bp.route('/<restaurante_id>/cupons', methods=['POST'])
def create_cupom(restaurante_id):
    dados = request.get_json()
    dados['restaurante_id'] = restaurante_id
    cupom = cupom_repo.create_cupom(**dados)

    if cupom:
        return jsonify(cupom.to_dict()),200


@cupom_bp.route('/<restaurante_id>/cupons/<cupom_id>', methods=['PUT'])
def update_cupom(restaurante_id,cupom_id):
    dados = request.get_json()
    cupom = cupom_repo.get_cupom_by_id(cupom_id)

    if cupom:
        cupom = cupom_repo.update_cupom(cupom, **dados)
        return jsonify(cupom.to_dict()),200
    return jsonify({'message': 'cupom not found.'}),404

@cupom_bp.route('/<restaurante_id>/cupons/<cupom_id>', methods=['DELETE'])
def delete_cupom(restaurante_id, cupom_id):
    cupom = cupom_repo.get_cupom_by_id(cupom_id)

    if cupom:
        cupom_repo.delete_cupom(cupom)
        return jsonify({'message': 'cupom deletado com sucesso.'}),200
    return jsonify({'message': 'cupom not found.'}),404
