# controllers/estadisticas_controller.py

class EstadisticasController:
    @staticmethod
    def calcular_promedio_gasto_clientes_vip(tickets_vendidos, restaurantes_vendidos):
        total_gasto = 0
        total_clientes = 0
        for ticket in tickets_vendidos:
            if ticket.tipo == "VIP":
                total_gasto += ticket.calcular_costo_total(restaurantes_vendidos)
                total_clientes += 1
        if total_clientes > 0:
            promedio_gasto = total_gasto / total_clientes
        else:
            promedio_gasto = 0
        return promedio_gasto

    @staticmethod
    def generar_reporte_asistencia(partidos):
        # Ordenar partidos por asistencia (ejemplo)
        partidos_ordenados = sorted(partidos, key=lambda x: x.asistencia(), reverse=True)
        reporte = []
        for partido in partidos_ordenados:
            reporte.append({
                "Partido": f"{partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}",
                "Estadio": partido.estadio.nombre,
                "Boletos Vendidos": partido.boletos_vendidos,
                "Personas que Asistieron": partido.asistencia(),
                "Relación Asistencia/Venta": partido.relacion_asistencia_venta()
            })
        return reporte
