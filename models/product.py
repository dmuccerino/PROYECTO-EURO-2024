
class Producto:
    def __init__(self, nombre, clasificacion, precio, es_alcoholica=False, es_empaque=False):
        self.nombre = nombre
        self.clasificacion = clasificacion  # "alimento" o "bebida"
        self.precio = precio
        self.es_alcoholica = es_alcoholica  # True si es bebida alcohólica
        self.es_empaque = es_empaque  # True si es alimento de empaque

