from models.product import Producto
from models.client import Cliente
class RestaurantSaleController:
    def __init__(self, product_controller):
        self.product_controller = product_controller
        self.sales = []

# Lista para simular los productos del restaurante
productos_restaurante = [
    Producto("Cerveza", "Bebida", 4.12, es_alcoholica=True),
    Producto("Agua Mineral", "Bebida", 1.50),
    Producto("Pizza", "Alimento", 10.00, es_empaque=True),
    Producto("Ensalada", "Alimento", 7.50, es_empaque=False)
]

# Función para buscar productos por nombre
def buscar_producto_por_nombre(nombre):
    resultados = [producto for producto in productos_restaurante if nombre.lower() in producto.nombre.lower()]
    return resultados

# Función para buscar productos por tipo (bebida o alimento)
def buscar_producto_por_tipo(tipo):
    resultados = [producto for producto in productos_restaurante if producto.clasificacion.lower() == tipo.lower()]
    return resultados

# Función para buscar productos por rango de precio
def buscar_producto_por_precio(min_precio, max_precio):
    resultados = [producto for producto in productos_restaurante if min_precio <= producto.precio <= max_precio]
    return resultados

# Función para gestionar la venta en el restaurante
def gestion_venta_restaurante(cliente, productos_comprados):
    # Verificar si el cliente tiene una entrada VIP
    if cliente.edad < 18:
        print("Lo siento, no puede comprar bebidas alcohólicas.")
        return

    # Calcular el monto total de la compra
    total = sum(producto.precio for producto in productos_comprados)

    # Aplicar descuento si la cédula es un número perfecto (ejemplo)
    descuento = 0.15 if int(cliente.cedula) == 28 else 0

    # Aplicar descuento
    total_descuento = total * (1 - descuento)

    # Mostrar resumen de la compra
    print("\nResumen de la compra en el restaurante:")
    for producto in productos_comprados:
        print(f"Producto: {producto.nombre} - ${producto.precio:.2f}")

    print(f"\nTotal: ${total:.2f}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Total a Pagar: ${total_descuento:.2f}")

    # Actualizar inventario (simulación)
    for producto in productos_comprados:
        print(f"Restando del inventario: {producto.nombre}")

# Ejemplo de uso de las funciones de búsqueda
if __name__ == "__main__":
    print("Productos en el restaurante:")
    for producto in productos_restaurante:
        print(f"{producto.nombre} - ${producto.precio:.2f}")

    # Ejemplo de búsqueda por nombre
    print("\nBúsqueda por nombre (Pizza):")
    resultados_nombre = buscar_producto_por_nombre("Pizza")
    for producto in resultados_nombre:
        print(f"{producto.nombre} - ${producto.precio:.2f}")

    # Ejemplo de búsqueda por tipo (Bebida)
    print("\nBúsqueda por tipo (Bebida):")
    resultados_tipo = buscar_producto_por_tipo("Bebida")
    for producto in resultados_tipo:
        print(f"{producto.nombre} - ${producto.precio:.2f}")

    # Ejemplo de búsqueda por rango de precio ($1.00 - $5.00)
    print("\nBúsqueda por rango de precio ($1.00 - $5.00):")
    resultados_precio = buscar_producto_por_precio(1.00, 5.00)
    for producto in resultados_precio:
        print(f"{producto.nombre} - ${producto.precio:.2f}")

    # Ejemplo de venta en el restaurante (simulado)
    cliente_ejemplo = Cliente("Juan Pérez", "1234567890", 25)
    productos_comprados = [productos_restaurante[0], productos_restaurante[2]]  # Cerveza y Pizza
    gestion_venta_restaurante(cliente_ejemplo, productos_comprados)
