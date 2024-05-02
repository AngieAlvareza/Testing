from Cliente import Cliente
from Producto import Producto
from Pedido import Pedido

def main():
    # Crear un cliente
    cliente = Cliente()
    cliente.set_nombre("Angie")
    cliente.set_direccion("Calle Principal")
    cliente.set_telefono("123456789")
    cliente.set_dni("12345678A")

    # Crear algunos productos
    producto1 = Producto("001", "Camiseta", 20.99, "Camiseta de algodón")
    producto2 = Producto("002", "Pantalón", 35.50, "Pantalón de mezclilla")

    # Crear un pedido y agregar productos

    pedido.agregar_item(producto1, 2)
    pedido.agregar_item(producto2, 1)

    # Crear una factura para el pedido
    factura = Factura("F001", pedido)

    # Imprimir detalles del pedido y factura
    print("Detalles del Pedido:")
    print(pedido.to_string())
    print("\nDetalles de la Factura:")
    print(f"ID de Factura: {factura.id_factura}")
    print(f"Fecha de Factura: {factura.get_fecha()}")
    print(f"Total de Factura: ${factura.get_total()}")

if __name__ == "__main__":
    main()