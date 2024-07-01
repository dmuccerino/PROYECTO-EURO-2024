class StatisticsController:
    # ... (definiciones anteriores)

    def generar_reporte_ventas(self):
        reporte_ventas = []

        for venta in self.restaurant_sale_controller.get_all_sales():
            reporte_ventas.append({
                "cliente": venta["client"].nombre,
                "producto": venta["product"].nombre,
                "cantidad": venta["quantity"],
                "subtotal": venta["subtotal"],
                "iva": venta["iva"],
                "total": venta["total"]
            })

        return reporte_ventas
