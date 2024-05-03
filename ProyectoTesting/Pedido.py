class Pedido:

    #Constructor
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.item_pedido = []

    #Métodos
    def agregar_item(self, producto, cantidad):
        self.item_pedido.append({
            "Producto" : producto, "Cantidad" :cantidad
        })
    def calcular_total(self):
        total = 0
        for item in self.item_pedido:
            total += item["Producto"].precio * item["Cantidad"]
        return total
    
    #Getters y Setters
    #Cliente
    def get_cliente(self):
        return self.cliente
    def set_cliente(self, cliente):
        self.cliente = cliente
    #Item_pedido
    def get_item_pedido(self):
        return self.item_pedido
    def set_item_pedido(self, item_pedido):
        self.item_pedido = item_pedido
    
    #Método to String
    def to_string(self):
        print("Cliente: ", self.cliente.to_string())
        print("Items: ")
        for item in self.item_pedido:
            print("Producto: ", item["Producto"].to_string())
            print("Cantidad: ", item["Cantidad"])
        print("Total: ", self.calcular_total())
    






    #Modificación de ítems dentro de la lista.
    #Item
    # def get_item(self):
    #     return self.item_pedido
    # def set_item(self, index, producto, cantidad):
    #     if 0 <= index < len(self.item_pedido):
    #         self.item_pedido[index] = {"producto": producto, "cantidad": cantidad}
