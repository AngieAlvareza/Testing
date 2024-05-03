class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Ejemplo de uso
producto = Producto("Vino tinto", 20)
print(f"Nombre del producto: {producto.nombre}")
print(f"Precio del producto: ${producto.precio}")
