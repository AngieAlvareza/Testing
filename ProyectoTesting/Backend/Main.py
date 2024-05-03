from Bodega import Bodega
from Producto import Producto
from CarritoDeCompras import CarritoDeCompras

# Crear algunos productos
producto1 = Producto("Vino Tinto", 10)
producto2 = Producto("Vino Blanco", 8)
producto3 = Producto("Vino Rosado", 12)

# Crear una bodega y agregar productos a ella
bodega = Bodega("Bodega Héritage d'Or", "Dirección de la bodega", "Teléfono de la bodega", "Calificación de la bodega")

bodega.agregar_producto(producto1)
bodega.agregar_producto(producto2)
bodega.agregar_producto(producto3)

# Mostrar los productos disponibles en la bodega
print("Productos disponibles en la bodega:")
bodega.mostrar_productos()

# Crear un carrito de compras
carrito = CarritoDeCompras()

# Agregar productos al carrito
carrito.agregar_producto(producto1, 2)
carrito.agregar_producto(producto2, 1)
carrito.agregar_producto(producto3, 3)

# Ver el contenido del carrito
print("\nContenido del carrito:")
carrito.ver_carrito()

# Calcular el total de la compra
total_compra = carrito.calcular_total()
print(f"\nTotal de la compra: ${total_compra}")
