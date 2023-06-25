from flask import Blueprint, jsonify, request

from repositories.customer_repository import CustomerRepository
from repositories.address_customer_repository import AddressCustomerRepository

customer_bp =  Blueprint("customer", __name__)

customer_repository = CustomerRepository()
address_repository = AddressCustomerRepository()


@customer_bp.route("/customers", methods = ['GET'])
def get_customers():
    
    customers =customer_repository.get_customer_all()

    if not customers:
        return jsonify({'message': 'No customers found'}), 404
    
    customer_list = [
        {'id': customer.id, 'cpf': customer.cpf, 'name': customer.name, 'phone_number': customer.phone_number, 'email': customer.email}
        for customer in customers
    ]

    return jsonify({'customers': customer_list}), 200
    

@customer_bp.route("/customers/<int:id_customer>", methods = ['GET'])
def get_customer_by_id(id_customer):
    customer =customer_repository.get_customer_by_id(id_customer)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    return jsonify({
        'customer': {
            'id': customer.id,
            'email': customer.email,
            'cpf': customer.cpf,
            'name': customer.name,
            'phone_number': customer.phone_number
        }
    }), 200

@customer_bp.route("/customers", methods = ['POST'])
def create_customer():
    data = request.json

    email = data.get('email')
    password = data.get('password')
    cpf = data.get('cpf')
    name = data.get('name')
    phone_number = data.get('phone_number')
    
    customer =customer_repository.create_customer(email=email, password=password,cpf=cpf, name=name, phone_number=phone_number)

    return jsonify({
        'customer':{
            'id': customer.id,
            'email': customer.email,
            'cpf': customer.cpf,
            'name': customer.name,
            'phone_number': customer.phone_number,
            'type': customer.user_type
            }
    }), 201
   
@customer_bp.route("/customers/<int:customer_id>", methods = ['PUT'])
def update_customer(customer_id):
    customer=customer_repository.get_customer_by_id(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    data = request.json
    email = data.get('email')
    name = data.get('name')
    phone_number = data.get('phone_number')

    customer =customer_repository.update_customer(customer,email, name, phone_number)

    return jsonify({
        'customer':{
            'id': customer.id,
            'email': customer.email,
            'cpf': customer.cpf,
            'name': customer.name,
            'phone_number': customer.phone_number,
            'type': customer.user_type
            }
    })
    

@customer_bp.route("/customers/<customer_id>", methods = ['DELETE'])
def delete_customer(customer_id):
    customer=customer_repository.get_customer_by_id(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    
    customer_repository.delete_customer(customer_id)

    return jsonify({'message': 'Customer deleted successfully'}), 200



#ADDRESS ROUTES

@customer_bp.route("/customers/<int:customer_id>/addresses/<int:address_id>", methods = ['GET'])
def get_address(customer_id, address_id):
    customer = customer_repository.get_customer_by_id(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    address = address_repository.get_address_customer_by_id(address_id)

    if not address:
        return jsonify({'error': 'Address not found'}), 404

    # Retorne os detalhes do endereço em formato JSON
    return jsonify({
        'address': {
            'id': address.id,
            'customer_id': address.customer_id,
            'nickname': address.nickname,
            'cep': address.cep,
            'street': address.street,
            'state': address.state,
            'city': address.city,
            'neighborhood': address.neighborhood,
            'number': address.number,
            'complement': address.complement
        }
    })


@customer_bp.route("/customers/<int:customer_id>/addresses", methods = ['GET'])
def get_addresses(customer_id):
    addresses = address_repository.get_address_customer_all(customer_id)
    if not addresses:
        return jsonify({'error': 'No addresses found for the customer'}), 404

    address_list = []
    for address in addresses:
        address_data = {
            'id': address.id,
            'customer_id': address.customer_id,
            'nickname': address.nickname,
            'cep': address.cep,
            'street': address.street,
            'state': address.state,
            'city': address.city,
            'neighborhood': address.neighborhood,
            'number': address.number,
            'complement': address.complement
        }
        address_list.append(address_data)

    if not address_list:
        return jsonify({'message':'Customer has no registered addresses'}),204
    
    return jsonify({'addresses': address_list})

@customer_bp.route("/customers/<int:customer_id>/addresses", methods = ['POST'])
def create_address(customer_id):
    customer = customer_repository.get_customer_by_id(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found.'}),404
    
    data = request.json
    address_data = {
        'customer_id': customer_id,
        'nickname': data.get('nickname'),
        'cep': data.get('cep'),
        'street': data.get('street'),
        'state': data.get('state'),
        'city': data.get('city'),
        'neighborhood': data.get('neighborhood'),
        'number': data.get('number'),
        'complement': data.get('complement'),
    }

    address_customer = address_repository.create_address_customer(**address_data)
    customer.addresses.append(address_customer)
    return  jsonify({
        'id': address_customer.id,
        'nickname': address_customer.nickname,
        'cep': address_customer.cep,
        'street': address_customer.street,
        'state': address_customer.state,
        'city': address_customer.city,
        'neighborhood': address_customer.neighborhood,
        'number': address_customer.number,
        'complement': address_customer.complement,
        'customer_id': address_customer.customer_id
    })

@customer_bp.route("/customers/<int:customer_id>/addresses/<int:address_id>", methods = ['PUT'])
def update_address(customer_id, address_id):
    customer = customer_repository.get_customer_by_id(customer_id)
    address_customer = address_repository.get_address_customer_by_id(address_id)
    if not customer or not address_customer:
        return jsonify({'error': 'Customer or address not found'}), 404
    
    data = request.json

    address_data = {
        'nickname': data.get('nickname'),
        'cep': data.get('cep'),
        'street': data.get('street'),
        'state': data.get('state'),
        'city': data.get('city'),
        'neighborhood': data.get('neighborhood'),
        'number': data.get('number'),
        'complement': data.get('complement'),
    }
    
    address_repository.update_address_customer(address_customer, **address_data)

    return  jsonify({
        'id': address_customer.id,
        'nickname': address_customer.nickname,
        'cep': address_customer.cep,
        'street': address_customer.street,
        'state': address_customer.state,
        'city': address_customer.city,
        'neighborhood': address_customer.neighborhood,
        'number': address_customer.number,
        'complement': address_customer.complement,
        'customer_id': address_customer.customer_id
    })



@customer_bp.route("/customers/<int:customer_id>/addresses/<int:address_id>", methods = ['DELETE'])
def delete_address(customer_id, address_id):

    customer = customer_repository.get_customer_by_id(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    address = address_repository.get_address_customer_by_id(address_id)

    if not address:
        return jsonify({'error': 'Address not found'}), 404

    if address.customer_id != customer_id:
        return jsonify({'error': 'Address does not belong to the customer'}), 400

    address_repository.delete_address_customer(address)

    return jsonify({'message': 'Address deleted successfully'})

    



@customer_bp.route("/customers/<int:id_customer>/orders", methods =['GET'])
def get_orders_customer(id_customer):
    pass

@customer_bp.route("/customers/<int:id_customer>/orders", methods =['POST'])
def create_orders_customer(id_customer):
    pass

@customer_bp.route("/customers/<int:id_customer>/orders/<int:id_order>", methods =['DELETE'])
def delete_orders_customer(id_customer, id_order):
    pass


