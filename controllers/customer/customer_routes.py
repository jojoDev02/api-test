from flask import Blueprint, jsonify, request

from models.customer import Customer
from db.database import db_session

customer_bp =  Blueprint("customer", __name__)

@customer_bp.route("/customers", methods = ['GET'])
def get_customers():
    pass
    

@customer_bp.route("/customers/<int:id_customer>", methods = ['GET'])
def get_customer_by_id(id_customer):
    pass

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

@customer_bp.route("/customers", methods = ['DELETE'])
def delete_customer():
    pass

@customer_bp.route("/customers/<int:id_customer>/orders", methods =['GET'])
def get_orders_customer(id_customer):
    pass

@customer_bp.route("/customers/<int:id_customer>/orders", methods =['POST'])
def create_orders_customer(id_customer):
    pass

@customer_bp.route("/customers/<int:id_customer>/orders/<int:id_order>", methods =['DELETE'])
def delete_orders_customer(id_customer, id_order):
    pass


