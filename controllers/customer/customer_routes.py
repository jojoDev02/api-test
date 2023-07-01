from flask import Blueprint, jsonify, request

from repositories.customer_repository import CustomerRepository
from repositories.address_customer_repository import AddressCustomerRepository
from auth.auth import auth_required

customer_bp =  Blueprint("customer", __name__)

customer_repository = CustomerRepository()
address_repository = AddressCustomerRepository()


@customer_bp.route("/clientes", methods = ['GET'])
def get_customers():
    
    customers =customer_repository.get_customer_all()

    if not customers:
        return jsonify({'message': 'No customers found'}), 404
    
    customer_list = [
        {'id': customer.id, 'cpf': customer.cpf, 'nome': customer.nome, 'telefone': customer.telefone, 'email': customer.email}
        for customer in customers
    ]

    return jsonify({'clientes': customer_list}), 200
    

@customer_bp.route("/clientes/<int:cliente_id>", methods = ['GET'])
def get_customer_by_id(cliente_id):
    customer =customer_repository.get_customer_by_id(cliente_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    return jsonify(customer.to_dict()),200

@customer_bp.route("/clientes", methods = ['POST'])
def create_customer():
    data = request.json

    email = data.get('email')
    senha = data.get('senha')
    cpf = data.get('cpf')
    nome = data.get('nome')
    telefone = data.get('telefone')
    
    customer =customer_repository.create_customer(email, senha,cpf, nome, telefone)

    return jsonify(customer.to_dict()), 201
   
@customer_bp.route("/clientes/<int:cliente_id>", methods = ['PUT'])
def update_customer(cliente_id):
    customer=customer_repository.get_customer_by_id(cliente_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    data = request.json
    email = data.get('email')
    nome = data.get('nome')
    telefone = data.get('telefone')

    customer =customer_repository.update_customer(customer,email, nome, telefone)

    return jsonify(customer.to_dict())
    

@customer_bp.route("/clientes/<cliente_id>", methods = ['DELETE'])
def delete_customer(cliente_id):
    customer=customer_repository.get_customer_by_id(cliente_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    
    customer_repository.delete_customer(cliente_id)

    return jsonify({'message': 'Customer deleted successfully'}), 200



#ADDRESS ROUTES

@customer_bp.route("/clientes/<int:cliente_id>/enderecos/<int:endereco_id>", methods = ['GET'])
def get_address(cliente_id, endereco_id):
    customer = customer_repository.get_customer_by_id(cliente_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    endereco = address_repository.get_address_customer_by_id(endereco_id)

    if not endereco:
        return jsonify({'error': 'Address not found'}), 404

    return jsonify(endereco.to_dict())


@customer_bp.route("/clientes/<int:cliente_id>/enderecos", methods = ['GET'])
def get_addresses(cliente_id):
    enderecos = address_repository.get_address_customer_all(cliente_id)
    if not enderecos:
        return jsonify({'error': 'No enderecos found for the customer'}), 404

    enderecos_lista = []
    for endereco in enderecos:
        endereco_dados = endereco.to_dict()
        enderecos_lista.append(endereco_dados)

    if not enderecos_lista:
        return jsonify({'message':'Customer has no registered enderecos'}),204
    
    return jsonify({'enderecos': enderecos_lista})

@customer_bp.route("/clientes/<int:cliente_id>/enderecos", methods = ['POST'])
def create_address(cliente_id):
    customer = customer_repository.get_customer_by_id(cliente_id)

    if not customer:
        return jsonify({'error': 'Customer not found.'}),404
    
  
    address_data = request.get_json()
    address_data['cliente_id'] = cliente_id
    address_customer = address_repository.create_address_customer(**address_data)

    customer.enderecos.append(address_customer)
    return  jsonify(address_customer.to_dict()),201

@customer_bp.route("/clientes/<int:cliente_id>/enderecos/<int:endereco_id>", methods = ['PUT'])
def update_address(cliente_id, endereco_id):
    customer = customer_repository.get_customer_by_id(cliente_id)
    address_customer = address_repository.get_address_customer_by_id(endereco_id)
    if not customer or not address_customer:
        return jsonify({'error': 'Customer or endereco not found'}), 404

    address_data = request.get_json()
    address_repository.update_address_customer(address_customer, **address_data)

    return  jsonify(address_customer.to_dict())



@customer_bp.route("/clientes/<int:cliente_id>/enderecos/<int:endereco_id>", methods = ['DELETE'])
def delete_address(cliente_id, endereco_id):

    customer = customer_repository.get_customer_by_id(cliente_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    endereco = address_repository.get_address_customer_by_id(endereco_id)

    if not endereco:
        return jsonify({'error': 'Address not found'}), 404

    if endereco.cliente_id!= cliente_id:
        return jsonify({'error': 'Address does not belong to the customer'}), 400

    address_repository.delete_address_customer(endereco)

    return jsonify({'message': 'Address deleted successfully'})

    