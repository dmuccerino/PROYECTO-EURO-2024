
class Restaurante:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_productos(self, nombre=None, tipo=None, rango_precio=None):
        resultados = []
        for producto in self.productos:
            if (nombre is None or nombre.lower() in producto.nombre.lower()) and \
               (tipo is None or tipo.lower() == producto.clasificacion.lower()) and \
               (rango_precio is None or (producto.precio >= rango_precio[0] and producto.precio <= rango_precio[1])):
                resultados.append(producto)
        return resultados