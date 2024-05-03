class Inventario:
    def __init__(self):
        self.productos = []

    def get_productos(self):
        return self.productos

    def set_productos(self, nuevos_productos):
        self.productos = nuevos_productos

    def agregar_producto(self, producto):
        self.productos.append(producto)
