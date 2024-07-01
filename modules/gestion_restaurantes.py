
from models.product import Producto

# Lista de productos disponibles en el restaurante (puedes cargar desde API o archivo)
productos_disponibles = [
    Producto("Hamburguesa", "alimento", 12.50, es_empaque=True),
    Producto("Pizza", "alimento", 15.00, es_empaque=True),
    Producto("Cerveza", "bebida", 5.00, es_alcoholica=True),
    Producto("Refresco", "bebida", 3.50),
]

# Función para buscar productos por nombre
def buscar_producto_por_nombre(nombre):
    for producto in productos_disponibles:
        if producto.nombre.lower() == nombre.lower():
            return producto
    return None

# Función para buscar productos por tipo (alimento o bebida)
def buscar_productos_por_tipo(tipo):
    resultados = []
    for producto in productos_disponibles:
        if producto.tipo == tipo:
            resultados.append(producto)
    return resultados

# Función para buscar productos por rango de precio
def buscar_productos_por_rango_de_precio(min_precio, max_precio):
    resultados = []
    for producto in productos_disponibles:
        if min_precio <= producto.precio <= max_precio:
            resultados.append(producto)
    return resultados

# Función para realizar la venta de productos
def realizar_venta(producto, cliente):
    # Verificar edad del cliente para bebidas alcohólicas
    if producto.tipo == 'bebida' and producto.es_alcoholica and cliente.edad < 18:
        print("El cliente es menor de 18 años. No puede comprar bebidas alcohólicas.")
        return False

    # Calcular precio final (con IVA)
    producto.aplicar_iva()
    costo_total = producto.precio

    # Mostrar resumen de la compra
    print(f"Producto: {producto}")
    print(f"Costo total (con IVA): ${costo_total:.2f}")

    # Aquí se podría integrar la lógica de pago exitoso y actualización de inventario

    return True
