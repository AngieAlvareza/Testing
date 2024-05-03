import Producto
from Producto import Producto

# Luego, puedes usar la clase Producto normalmente
producto1 = Producto("Vino Tinto", 10)

class Bodega:
    def __init__(self, nombre, direccion, telefono, calificacion):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.calificacion = calificacion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def mostrar_productos(self):
        print(f"Productos en la bodega {self.nombre}:")
        for producto in self.productos:
            print(f"- {producto.nombre}: ${producto.precio}")

# Ejemplo de uso
bodega = Bodega("Bodega Héritage d'Or", "Av.EEUU 543", "951838123", 3)

# Crear algunos productos
producto1 = Producto("Vino tinto", 20)
producto2 = Producto("Vino blanco", 15)

# Agregar productos a la bodega
bodega.agregar_producto(producto1)
bodega.agregar_producto(producto2)

# Mostrar los productos en la bodega
bodega.mostrar_productos()
