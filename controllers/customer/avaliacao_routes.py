from flask import Blueprint, jsonify, request
from repositories.order_repository import OrderRepository
from repositories.avaliacao_repository import AvaliacaoRepository
from repositories.restaurant_repository import RestaurantRepository

avaliacao_bp =  Blueprint("avaliacao", __name__, url_prefix='/clientes')
pedido_repo = OrderRepository()
avaliacao_repo = AvaliacaoRepository()
restaurant_repo = RestaurantRepository()

@avaliacao_bp.route('/<int:cliente_id>/pedidos/<int:pedido_id>/avaliar', methods=['POST'])
def avaliar_pedido(cliente_id, pedido_id):
    dados = request.get_json()

    nota = dados['nota']

    pedido = pedido_repo.get_order_by_id(pedido_id)

    if not pedido:
        return jsonify({'mensagem': 'Pedido não encontrado.'}), 404
    
    avaliacao = avaliacao_repo.create_avaliacao(pedido, nota)
    restaurant_repo.atualizar_nota_media(pedido.restaurante_id)

    return jsonify(avaliacao.to_dict())