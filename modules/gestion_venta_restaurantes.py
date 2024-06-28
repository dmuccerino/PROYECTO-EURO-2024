from .gestion_restaurantes import GestionRestaurantes


class GestionVentaRestaurantes:
    def __init__(self, gestion_restaurantes):
        self.gestion_restaurantes = gestion_restaurantes
        self.ventas = []

    def vender_producto(self, cliente, nombre_producto, cantidad, descuento=0):
        producto = next((p for p in self.gestion_restaurantes.productos if p['nombre'] == nombre_producto), None)
        if not producto:
            print(f'Producto {nombre_producto} no encontrado.')
            return

        precio_total = producto['precio'] * cantidad * (1 - descuento / 100)
        venta = {
            'cliente': cliente,
            'producto': nombre_producto,
            'cantidad': cantidad,
            'precio_total': precio_total
        }
        self.ventas.append(venta)
        print(f'Producto {nombre_producto} vendido a {cliente} por {precio_total}€.')

if __name__ == "__main__":
    gestion_restaurantes = GestionRestaurantes()
    gestion_restaurantes.agregar_producto('Hamburguesa', 'Comida', 5.5)  # Agregar producto

    gestion_venta_restaurantes = GestionVentaRestaurantes(gestion_restaurantes)
    gestion_venta_restaurantes.vender_producto('Juan Perez', 'Hamburguesa', 2, 10)  # Ejemplo de venta de producto
