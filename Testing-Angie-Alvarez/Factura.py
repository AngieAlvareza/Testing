from datetime import date, datetime
from Pedido import Pedido

class Factura:
    def __init__(self, id_factura: str, pedido: Pedido, fecha: date):
        self.id_factura = id_factura
        self.pedido = Pedido.get_item_pedido
        self.fecha = datetime.now()
    
    def get_pedido(self):
        return self.pedido
    
    def get_total(self):
        total = 0
        for item in self.pedido:
            total += item.precio * item.cantidad
        return total
    
    def get_fecha(self):
        return self.fecha