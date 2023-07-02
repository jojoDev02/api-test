from flask import jsonify
from models.cupom import Cupom
from db.database import db_session
class CupomRepository:

    def create_cupom(self, **dados):
        cupom = Cupom(**dados)
        db_session.add(cupom)
        db_session.commit()
        return cupom

    def get_cupom_by_id(self, cupom_id):
        return db_session.query(Cupom).get(cupom_id)
    
    def get_cupons(self, restaurante_id):
        return db_session.query(Cupom).filter(Cupom.restaurante_id == restaurante_id).all()
        
    def update_cupom(self, cupom, **dados):
        if cupom:
           for key, value in dados.items():
               setattr(cupom, key, value)
        db_session.commit()
        return cupom


    def delete_cupom(self, cupom):
        db_session.delete(cupom)
        db_session.commit()

    