
# Función para calcular el promedio de gasto de un cliente VIP
def calcular_promedio_gasto_vip(partidos, tickets_vip):
    total_gasto = 0
    total_clientes = 0
    for partido in partidos:
        for ticket in tickets_vip:
            if ticket.partido == partido:
                total_gasto += ticket.precio
                total_clientes += 1
    if total_clientes > 0:
        return total_gasto / total_clientes
    else:
        return 0

# Función para determinar el partido con mayor asistencia
def encontrar_partido_mayor_asistencia(partidos):
    partido_max = None
    max_asistencia = 0
    for partido in partidos:
        if partido.asistencia > max_asistencia:
            partido_max = partido
            max_asistencia = partido.asistencia
    return partido_max

# Otras funciones para generar estadísticas según las necesidades del proyecto

