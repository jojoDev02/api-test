from db.database import db_session
from models.address import AddressCustomer
from models.customer import Customer

class AddressCustomerRepository:
    def create_address_customer(self, **kwargs):
        address_customer = AddressCustomer(**kwargs)
        db_session.add(address_customer)
        db_session.commit()
        return address_customer

    #ta errado, a consulta parte do customer
    def get_address_customer_all(self, customer_id):
        return db_session.query(AddressCustomer).filter(AddressCustomer.customer_id == customer_id)
    
    def get_address_customer_by_id(self, address_customer_id):
        return db_session.query(AddressCustomer).get(address_customer_id)

    def update_address_customer(self, address_customer, **kwargs):
        if address_customer:
            for key, value in kwargs.items():
                setattr(address_customer, key, value)
            db_session.commit()
        return address_customer

    def delete_address_customer(self, address):
        if address:
            db_session.delete(address)
            db_session.commit()
      
