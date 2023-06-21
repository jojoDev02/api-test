from flask import Blueprint

cliente_bp =  Blueprint("cliente", __name__)

@cliente_bp.route("/clientes", methods = ['GET'])
def get_clientes():
    pass

@cliente_bp.route("/clientes/<int:id_cliente>", methods = ['GET'])
def get_cliente_by_id(id_cliente):
    pass

@cliente_bp.route("/clientes", methods = ['POST'])
def create_cliente():
    pass

@cliente_bp.route("/clientes", methods = ['PUT'])
def update_cliente():
    pass

@cliente_bp.route("/clientes", methods = ['DELETE'])
def delete_cliente():
    pass

@cliente_bp.route("/clientes/<int:id_cliente>/pedidos", methods =['GET'])
def get_pedidos_cliente(id_cliente):
    pass

@cliente_bp.route("/clientes/<int:id_cliente>/pedidos", methods =['POST'])
def create_pedidos_cliente(id_cliente):
    pass

@cliente_bp.route("/clientes/<int:id_cliente>/pedidos/<int:id_pedido>", methods =['DELETE'])
def delete_pedidos_cliente(id_cliente, id_pedido):
    pass


