class CarritoDeCompras:
    def __init__(self):
        self.items = []  # Lista para almacenar los productos en el carrito

    def agregar_producto(self, producto, cantidad=1):
        """Agrega un producto al carrito de compras."""
        self.items.append({'producto': producto, 'cantidad': cantidad})

    def eliminar_producto(self, producto):
        """Elimina un producto del carrito de compras."""
        for item in self.items:
            if item['producto'] == producto:
                self.items.remove(item)
                break

    def vaciar_carrito(self):
        """Vacía el carrito de compras."""
        self.items = []

    def calcular_total(self):
        """Calcula el total de la compra."""
        total = 0
        for item in self.items:
            total += item['producto'].precio * item['cantidad']
        return total

    def ver_carrito(self):
        """Muestra los productos en el carrito de compras."""
        for item in self.items:
            print(f"Producto: {item['producto'].nombre}, Cantidad: {item['cantidad']}")

# Ejemplo de uso
if __name__ == "__main__":
    from Producto import Producto

    # Crear algunos productos
    producto1 = Producto("Vino Tinto", 10)
    producto2 = Producto("Vino Blanco", 8)
    producto3 = Producto("Vino Rosado", 12)

    # Crear un carrito de compras
    carrito = CarritoDeCompras()

    # Agregar productos al carrito
    carrito.agregar_producto(producto1, 2)
    carrito.agregar_producto(producto2, 1)
    carrito.agregar_producto(producto3, 3)

    # Ver el contenido del carrito
    print("Contenido del carrito:")
    carrito.ver_carrito()

    # Calcular el total de la compra
    total_compra = carrito.calcular_total()
    print(f"Total de la compra: ${total_compra}")

    # Eliminar un producto del carrito
    carrito.eliminar_producto(producto2)
    print("\nContenido del carrito después de eliminar un producto:")
    carrito.ver_carrito()

    # Vaciar el carrito
    carrito.vaciar_carrito()
    print("\nContenido del carrito después de vaciarlo:")
    carrito.ver_carrito()
