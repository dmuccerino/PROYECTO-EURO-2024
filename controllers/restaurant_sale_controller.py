
class RestaurantSaleController:
    def __init__(self, product_controller):
        self.product_controller = product_controller
        self.sales = []

    def vender_producto(self, client_name, product_name, quantity):
        client = self.client_controller.buscar_cliente(client_name)
        if client is None:
            print(f"Cliente '{client_name}' no encontrado.")
            return

        product = self.product_controller.buscar_producto(product_name)
        if product is None:
            print(f"Producto '{product_name}' no encontrado.")
            return

        if product.clasificacion == "alcoholica" and client.edad < 18:
            print(f"Cliente '{client_name}' no puede comprar bebidas alcohólicas.")
            return

        if product.cantidad_disponible < quantity:
            print(f"No hay suficientes unidades disponibles de '{product_name}'.")
            return

        subtotal = product.precio * quantity
        iva = subtotal * 0.16
        total = subtotal + iva

        if client.cedula_vampiro:
            descuento = total * 0.5
            total -= descuento
            print(f"¡Cliente '{client_name}' tiene un 50% de descuento por ser cédula vampiro!")

        self.sales.append({
            "client": client,
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
            "iva": iva,
            "total": total
        })

        product.cantidad_disponible -= quantity
        print(f"Venta exitosa a cliente '{client_name}' de '{quantity}' unidades de '{product_name}'.")
        print(f"Subtotal: ${subtotal:.2f}")
        if client.cedula_vampiro:
            print(f"Descuento: ${descuento:.2f}")
        print(f"IVA: ${iva:.2f}")
        print(f"Total: ${total:.2f}")

    def get_all_sales(self):
        return self.sales[:]
