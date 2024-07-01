
class Cliente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def es_cliente_vip(self):
        # Implementación para determinar si el cliente es VIP (por ejemplo, basado en la edad o historial de compras)
        return self.edad >= 18  # Ejemplo simple: cliente VIP si es mayor de edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Cédula: {self.cedula}, Edad: {self.edad}"


