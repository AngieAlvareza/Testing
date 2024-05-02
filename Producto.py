class Producto:
    def __init__(self, id_producto, nombre, precio, descripcion):
        self.id_producto = str(id_producto)
        self.nombre = str(nombre)
        self.precio = float(precio)
        self.descripcion = str(descripcion)
        self.inventario = 0

    # Métodos para obtener y establecer los atributos
    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = str(id_producto)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = str(nombre)

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = str(precio)

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = str(descripcion)

    # Método para obtener el inventario
    def get_inventario(self):
        return self.inventario

    def to_string(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Precio: ${self.precio}, Descripción: {self.descripcion}"

# Ejemplo de uso
producto1 = Producto("001", "Camiseta", "20.99", "Camiseta de algodón")
print("ID del producto:", producto1.get_id_producto())
print("Nombre del producto:", producto1.get_nombre())
print("Precio del producto:", producto1.get_precio())
print("Descripción del producto:", producto1.get_descripcion())
print("Inventario del producto:", producto1.get_inventario())
