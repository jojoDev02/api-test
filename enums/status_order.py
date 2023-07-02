from enum import Enum

class StatusOrder(Enum):
    AWAINTING_CONFIRMATION = (1, 'Aguardando Confirmação')
    CONFIRMED = (2, 'Confirmado')
    IN_PREPARATION = (3, 'Em Preparo')
    DELIVERED = (4, 'Entregue')
    ON_THE_WAY = (5, 'A Caminho')
    CANCELLED = (6, 'Cancelado')
