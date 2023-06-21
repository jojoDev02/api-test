from flask import Blueprint, jsonify, request
from models.address import AddressCustomer

from models.customer import Customer
from db.database import db_session

customer_bp =  Blueprint("customer", __name__)


@customer_bp.route("/customers", methods = ['GET'])
def get_customers():
    customers = Customer.query.all()

    if not customers:
        return jsonify({'message': 'No customers found'}), 404
    
    customer_list = [
        {'id': customer.id, 'cpf': customer.cpf, 'name': customer.name, 'phone_number': customer.phone_number}
        for customer in customers
    ]

    return jsonify({'customers': customer_list}), 200
    

@customer_bp.route("/customers/<int:id_customer>", methods = ['GET'])
def get_customer_by_id(id_customer):
    customer = Customer.query.get(id_customer)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    return jsonify({
        'customer': {
            'id': customer.id,
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

    customer = Customer(email=email, password=password, user_type= "customer" ,cpf=cpf, name=name, phone_number=phone_number)
    db_session.add(customer)
    db_session.commit()

    return jsonify({
        'message': 'Customer created successfully',

        'customer': {
            'id': customer.id,
            'email': customer.email,
            'cpf': customer.cpf,
            'name': customer.name,
            'phone_number': customer.phone_number
        },
        'user': {
            'email': customer.email,
            'type': customer.user_type
        }
    }), 201
   
@customer_bp.route("/customers", methods = ['PUT'])
def update_customer():
    pass

@customer_bp.route("/customers/<customer_id>", methods = ['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    db_session.delete(customer)
    db_session.commit()

    return jsonify({'message': 'Customer deleted successfully'}), 200

@customer_bp.route("/customers/<int:customer_id>/addresses/<int:address_id>", methods = ['GET'])
def get_address(id_customer, id_address):

    customer = Customer.query.get(id_customer)

    if not customer:
        return jsonify({'error':'Customer not found'}), 404
    
    address = AddressCustomer.query.filter_by(customer_id=id_customer, id=id_address).first()

    if not address:
        return jsonify({'error':'Address not found'}), 404
    
    address_data = {
        'id': address.id,
        'nickname': address.nickname,
        'cep': address.cep,
        'street': address.street,
        'state': address.state,
        'city': address.city,
        'neighborhood': address.neighborhood,
        'number': address.number,
        'complement': address.complement
    }

    return jsonify(address_data), 200


@customer_bp.route("/customers/<int:customer_id>/addresses", methods = ['GET'])
def get_addresses(customer_id):

    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    addresses = AddressCustomer.query.filter_by(customer_id=customer_id).all()

    addresses_data = []
    for address in addresses:
        address_data = {
            'id': address.id,
            'nickname': address.nickname,
            'cep': address.cep,
            'street': address.street,
            'state': address.state,
            'city': address.city,
            'neighborhood': address.neighborhood,
            'number': address.number,
            'complement': address.complement
        }
        addresses_data.append(address_data)

    return jsonify(addresses_data), 200

@customer_bp.route("/customers/<int:customer_id>/addresses", methods = ['POST'])
def create_address(customer_id):
    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    
    data = request.json
    nickname = data.get('nickname')
    cep = data.get('cep')
    street = data.get('street')
    state = data.get('state')
    city = data.get('city')
    neighborhood = data.get('neighborhood')
    number = data.get('number')
    complement = data.get('complement')

    address = AddressCustomer(
        customer_id=customer_id,
        nickname=nickname,
        cep=cep,
        street=street,
        state=state,
        city=city,
        neighborhood=neighborhood,
        number=number,
        complement=complement
    )

    customer.addresses.append(address)
    db_session.add(address)
    db_session.commit


    address_data = {
        'customer_id': address.customer_id ,
        'id': address.id_address_customer,
        'nickname': address.nickname,
        'cep': address.cep,
        'street': address.street,
        'state': address.state,
        'city': address.city,
        'neighborhood': address.neighborhood,
        'number': address.number,
        'complement': address.complement
    }

    return jsonify(address_data), 201 


@customer_bp.route("/customers/<int:id_customer>/orders", methods =['GET'])
def get_orders_customer(id_customer):
    pass

@customer_bp.route("/customers/<int:id_customer>/orders", methods =['POST'])
def create_orders_customer(id_customer):
    pass

@customer_bp.route("/customers/<int:id_customer>/orders/<int:id_order>", methods =['DELETE'])
def delete_orders_customer(id_customer, id_order):
    pass


