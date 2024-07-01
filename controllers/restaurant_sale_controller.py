
class RestaurantSaleController:
    def __init__(self, product_controller):
        self.sales = []
        self.product_controller = product_controller

    def sell_product(self, client, product_name, quantity):
        product = self.product_controller.get_product_by_name(product_name)
        if product:
            if product.is_alcoholic and client.age < 18:
                return "Client is underage and cannot buy alcoholic beverages."

            sale = {
                "client": client,
                "product": product,
                "quantity": quantity,
                "total_price": product.price * quantity * 1.16  # Adding 16% IVA
            }
            self.sales.append(sale)
            return sale
        return "Product not found."

    def get_sales_by_client(self, client):
        return [sale for sale in self.sales if sale["client"] == client]

    def get_all_sales(self):
        return self.sales
