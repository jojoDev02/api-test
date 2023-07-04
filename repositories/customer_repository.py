from models.customer import Customer
from db.database import db_session

class CustomerRepository:

    def get_customer_all(self):
        return db_session.query(Customer).all()
    
    def get_customer_by_id(self, cliente_id):
        return db_session.query(Customer).get(cliente_id)

    def create_customer(self,email, senha, cpf, nome, telefone):
        cliente = Customer(email=email, senha=senha, tipo="customer", cpf=cpf, nome=nome, telefone=telefone)
        db_session.add(cliente)
        db_session.commit()
        return cliente

    def update_customer(self, cliente, email, nome, telefone):
        if cliente:
            cliente.email = email
            cliente.nome = nome
            cliente.telefone = telefone
            db_session.commit()
            return cliente

    def delete_customer(self, cliente_id):
        cliente = self.get_customer_by_id(cliente_id)
        if cliente:
            db_session.delete(cliente)
            db_session.commit()