class Cliente:
    def __init__(self):
        self.nombre = ""
        self.direccion = ""
        self.telefono = ""
        self.dni = ""

    # Métodos para obtener y establecer los atributos
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni
