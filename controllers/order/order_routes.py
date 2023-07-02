from flask import Blueprint, jsonify, request
from repositories.order_repository import OrderRepository
from repositories.customer_repository import CustomerRepository
from repositories.restaurant_repository import RestaurantRepository

order_bp = Blueprint("order", __name__)
order_repo = OrderRepository()
customer_repo = CustomerRepository()
restaurant_repo = RestaurantRepository()

@order_bp.route('/pedidos/<int:pedido_id>', methods=['GET'])
def get_order(pedido_id):
    pedido = order_repo.get_order_by_id(pedido_id)

    
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404
    
    return jsonify(pedido.to_dict()), 200

@order_bp.route('/clientes/<int:cliente_id>/pedidos', methods=['GET'])
def get_customer_orders(cliente_id):
    pedidos = order_repo.get_orders_by_customer_id(cliente_id)

    if not pedidos:
        return jsonify({'message': 'cliente has no pedidos'}),404
    
    pedidos_lista = [pedido.to_dict() for pedido in pedidos]
    return jsonify(pedidos_lista), 200

@order_bp.route('/restaurantes/<restaurante_id>/pedidos', methods=['GET'])
def get_restaurant_orders(restaurante_id):
    pedidos = order_repo.get_orders_by_restaurant_id(restaurante_id)

    if pedidos:
        pedidos_lista = [pedido.to_dict() for pedido in pedidos]
        return jsonify(pedidos_lista), 200
    return jsonify({'message': 'restaurante has no pedidos'})

@order_bp.route('/restaurantes/<int:restaurante_id>/clientes/<int:cliente_id>/pedidos', methods=['POST'])
def create_order(restaurante_id, cliente_id):
    restaurante = restaurant_repo.get_restaurant_by_id(restaurante_id)
    cliente = customer_repo.get_customer_by_id(cliente_id)

    if not cliente or not restaurante:
        return jsonify({'message' : 'cliente or restaurante not exist'}),403
    
    data = request.get_json()
    data['restaurante'] = restaurante
    data['cliente'] = cliente
 
    pedido = order_repo.create_order(**data)

    return jsonify(pedido.to_dict())

@order_bp.route('/pedidos/<int:pedido_id>/atualizar-status', methods=['PUT'])
def update_order_status(pedido_id):
    pedido = order_repo.get_order_by_id(pedido_id)

    if not pedido:
        return jsonify({'error': 'Pedido not found.'}), 404
    
    pedido = order_repo.update_status_order(pedido)
    
    if pedido:
        return jsonify({'message': 'Order status updated successfully.'}), 200
    else:
        return jsonify({'message':'Operação inválida para o status atual do pedido.'}),400
    
@order_bp.route('/pedidos/<int:pedido_id>/cancelar', methods=['PUT'])
def cancel_order(pedido_id):
    pedido = order_repo.get_order_by_id(pedido_id)
    
    if not pedido:
        return jsonify({'error': 'Pedido not found.'}), 404
    
    pedido = order_repo.cancel_order(pedido)
    
    if pedido:
        return jsonify({'message': 'Pedido cancelado.'}), 200
    return jsonify({'message':'O pedido não pode ser cancelado.'}),400