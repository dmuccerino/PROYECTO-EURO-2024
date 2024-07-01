# Función para calcular el promedio de gasto de un cliente VIP en un partido
def promedio_gasto_cliente_vip(clientes, partidos):
    total_gasto = 0
    cantidad_clientes = 0

    for cliente in clientes:
        if cliente.tipo_entrada == "VIP":
            for partido in partidos:
                if partido.nombre == cliente.partido.nombre:
                    total_gasto += cliente.total_pago
                    cantidad_clientes += 1
                    break

    if cantidad_clientes > 0:
        promedio = total_gasto / cantidad_clientes
    else:
        promedio = 0

    return promedio

# Función para generar la tabla de asistencia a los partidos
def tabla_asistencia_partidos(partidos):
    partidos_ordenados = sorted(partidos, key=lambda partido: partido.asistencia, reverse=True)

    print("\nTabla de Asistencia a los Partidos:")
    print("{:<40} {:<30} {:<15} {:<15} {:<20}".format(
        "Nombre del Partido", "Estadio", "Boletos Vendidos", "Personas Asistieron", "Relación Asistencia/Venta"
    ))
    for partido in partidos_ordenados:
        relacion = partido.asistencia / partido.boletos_vendidos if partido.boletos_vendidos > 0 else 0
        print("{:<40} {:<30} {:<15} {:<15} {:<20}".format(
            f"{partido.equipo_local} vs {partido.equipo_visitante}", partido.estadio, partido.boletos_vendidos,
            partido.asistencia, f"{relacion:.2f}"
        ))

# Función para determinar el partido con la mayor asistencia
def partido_mayor_asistencia(partidos):
    partido = max(partidos, key=lambda partido: partido.asistencia)
    return partido

# Función para determinar el partido con el mayor número de boletos vendidos
def partido_mayor_boletos_vendidos(partidos):
    partido = max(partidos, key=lambda partido: partido.boletos_vendidos)
    return partido

# Función para determinar los top 3 productos más vendidos en el restaurante
def top_3_productos_mas_vendidos(productos):
    productos_ordenados = sorted(productos, key=lambda producto: producto.ventas, reverse=True)
    return productos_ordenados[:3]

# Función para determinar los top 3 clientes que más compraron boletos
def top_3_clientes_mas_compras(clientes):
    clientes_ordenados = sorted(clientes, key=lambda cliente: cliente.total_compras, reverse=True)
    return clientes_ordenados[:3]

# Ejemplo de uso de las funciones
if __name__ == "__main__":
    # Simulación de datos
    from models import Partido, Producto, Cliente

    # Simulación de partidos con datos ficticios
    partidos = [
        Partido("Equipo A", "Equipo B", "01/07/2024 18:00", "Estadio A", 100, 80),
        Partido("Equipo C", "Equipo D", "02/07/2024 19:00", "Estadio B", 150, 120)
    ]

    # Simulación de productos con datos ficticios
    productos = [
        Producto("Cerveza", "Bebida", 5.00),
        Producto("Pizza", "Alimento", 12.00),
        Producto("Agua", "Bebida", 2.50)
    ]

    # Simulación de clientes con datos ficticios
    clientes = [
        Cliente("Juan Pérez", "1234567890", "Equipo A vs Equipo B", "VIP", 100.00),
        Cliente("María Gómez", "0987654321", "Equipo C vs Equipo D", "General", 50.00)
    ]

    # Ejemplo de llamada a funciones de estadísticas
    print(f"\nPromedio de gasto de un cliente VIP: ${promedio_gasto_cliente_vip(clientes, partidos):.2f}")
    tabla_asistencia_partidos(partidos)
    print(f"\nPartido con mayor asistencia: {partido_mayor_asistencia(partidos).equipo_local} vs {partido_mayor_asistencia(partidos).equipo_visitante}")
    print(f"Partido con mayor número de boletos vendidos: {partido_mayor_boletos_vendidos(partidos).equipo_local} vs {partido_mayor_boletos_vendidos(partidos).equipo_visitante}")

    # Ejemplo de top 3 productos más vendidos en el restaurante
    print("\nTop 3 productos más vendidos en el restaurante:")
    productos_mas_vendidos = top_3_productos_mas_vendidos(productos)
    for i, producto in enumerate(productos_mas_vendidos, 1):
        print(f"{i}. {producto.nombre} - ${producto.ventas:.2f}")

    # Ejemplo de top 3 clientes que más compraron boletos
    print("\nTop 3 clientes que más compraron boletos:")
    clientes_mas_compras = top_3_clientes_mas_compras(clientes)
    for i, cliente in enumerate(clientes_mas_compras, 1):
        print(f"{i}. {cliente.nombre} - {cliente.total_compras} boletos")

