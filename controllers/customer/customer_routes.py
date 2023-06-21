from flask import Blueprint

customer_bp =  Blueprint("customer", __name__)

@customer_bp.route("/customers", methods = ['GET'])
def get_customers():
    pass

@customer_bp.route("/customers/<int:id_customer>", methods = ['GET'])
def get_customer_by_id(id_customer):
    pass

@customer_bp.route("/customers", methods = ['POST'])
def create_customer():
    pass

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


