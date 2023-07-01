import datetime
from enums.status_order import StatusOrder
from models.order import Order
from models.item_order import ItemOrder
from models.item_restaurant import ItemRestaurant
from db.database import db_session

class OrderRepository:

    def get_order_by_id(self, pedido_id):
        return db_session.query(Order).get(pedido_id)

    def get_orders_by_customer_id(self, cliente_id):
        return db_session.query(Order).filter(Order.cliente_id == cliente_id).all()  
    
    def get_orders_by_restaurant_id(self, restaurante_id):
        return db_session.query(Order).filter(Order.restaurante_id == restaurante_id).all()

    def create_order(self, **kwargs):

        itens = kwargs['itens']
        
        restaurante = kwargs['restaurante']
        cliente = kwargs['cliente']

        valor = kwargs['valor']
        metodo_pagamento=kwargs['metodo_pagamento']
        data=datetime.date.today()
        statusPedido=StatusOrder.AWAINTING_CONFIRMATION

        pedido = Order(valor=valor, data=data, statusPedido=statusPedido, metodo_pagamento=metodo_pagamento, restaurante_id=restaurante.id, cliente_id=cliente.id)
        
        db_session.add(pedido)
        db_session.commit()

        for item in itens:
            item_order = ItemOrder(quantidade=item['quantidade'], valor=item['valor'], item_restaurante_id=item['item_restaurante_id'], pedido_id=pedido.id)
            pedido.itens_pedidos.append(item_order)
        
        restaurante.pedidos.append(pedido)
        cliente.pedidos.append(pedido)
        db_session.commit()

        return pedido
        
    def update_status_order(self, pedido_id):
        pedido = self.get_order_by_id(pedido_id)
        if pedido:
            status_mapping = {
                1: StatusOrder.AWAINTING_CONFIRMATION,
                2: StatusOrder.CONFIRMED,
                3: StatusOrder.IN_PREPARATION,
                4: StatusOrder.DELIVERED,
                5: StatusOrder.ON_THE_WAY,
                6: StatusOrder.CANCELLED
            }
        if pedido.statusPedido.value in (5, 6):
            raise ValueError('Invalid operation for current order status.')

        current_status = pedido.statusPedido
        next_status_value = current_status.value[0] + 1

        if next_status_value not in status_mapping:
            raise ValueError('Invalid next order status.')

        next_status = status_mapping[next_status_value]
        pedido.statusPedido = next_status
        db_session.commit()

        return pedido
    
    def cancel_order(self, pedido):

        if pedido.statusPedido.value[0] in (1, 2):
            pedido.statusPedido=StatusOrder.CANCELLED
            db_session.commit()
            return pedido
        raise ValueError('Não é possivel cancelar o pedido')