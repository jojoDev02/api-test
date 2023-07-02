from enum import Enum

class PaymentMethod(Enum):
   PIX = 'Pix'
   CASH = 'Cash'
   DEBIT_CARD = 'Cartão de Débito'
   CREDIT_CARD = 'Cartão de Crédito'

