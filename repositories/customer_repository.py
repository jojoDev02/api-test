from models.customer import Customer
from db.database import db_session

class CustomerRepository:

    def get_customer_all(self):
        return db_session.query(Customer).all()
    
    def get_customer_by_id(self, customer_id):
        return db_session.query(Customer).get(customer_id)

    def create_customer(self,email, password, cpf, name, phone_number):
        customer = Customer(email=email, password=password, user_type="customer", cpf=cpf, name=name, phone_number=phone_number)
        db_session.add(customer)
        db_session.commit()
        return customer

    def update_customer(self, customer, email, name, phone_number):
        if customer:
            customer.email = email
            customer.name = name
            customer.phone_number = phone_number
            db_session.commit()
            return customer

    def delete_customer(self, customer_id):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            db_session.delete(customer)
            db_session.commit()

