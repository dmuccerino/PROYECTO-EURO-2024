
# models/producto.py

class Producto:
    def __init__(self, nombre, tipo, precio, es_alcoholica=False, es_empaque=False):
        self.nombre = nombre
        self.tipo = tipo  # Puede ser 'alimento' o 'bebida'
        self.precio = precio
        self.es_alcoholica = es_alcoholica  # True si es bebida alcohólica
        self.es_empaque = es_empaque  # True si es alimento de empaque

    def aplicar_iva(self):
        # Aplicar 16% de IVA al precio del producto
        self.precio *= 1.16

    def __str__(self):
        return f"{self.nombre} - {self.tipo}: ${self.precio:.2f}"



