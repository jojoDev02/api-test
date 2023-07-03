from models.avaliacao import Avaliacao
from db.database import db_session

class AvaliacaoRepository:

    def create_avaliacao(self, pedido, nota):
        avaliacao = Avaliacao(pedido_id=pedido.id, nota=nota)
        db_session.add(avaliacao)
        pedido.avaliacao = avaliacao
        db_session.commit()
        return avaliacao

    def get_avaliacoes_by_pedido_id(self, pedido_id):
        return db_session.query(Avaliacao).filter_by(pedido_id=pedido_id).all()