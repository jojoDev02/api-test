from db.database import db_session
from models.address import AddressCustomer


class AddressCustomerRepository:
    def create_address_customer(self, **kwargs):
        endereco_cliente = AddressCustomer(**kwargs)
        db_session.add(endereco_cliente)
        db_session.commit()
        return endereco_cliente

    def get_address_customer_all(self, cliente_id):
        return db_session.query(AddressCustomer).filter(AddressCustomer.cliente_id == cliente_id)
    
    def get_address_customer_by_id(self, endereco_cliente_id):
        return db_session.query(AddressCustomer).get(endereco_cliente_id)

    def update_address_customer(self, endereco_cliente, **kwargs):
        if endereco_cliente:
            for key, value in kwargs.items():
                setattr(endereco_cliente, key, value)
            db_session.commit()
        return endereco_cliente

    def delete_address_customer(self, endereco):
        if endereco:
            db_session.delete(endereco)
            db_session.commit()
      
