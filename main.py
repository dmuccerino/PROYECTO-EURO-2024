
import sys
import os
from datetime import datetime

# Añadir el directorio 'modules' al path de Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from utils.api_utils import cargar_datos_iniciales
from controllers.team_controller import TeamController
from controllers.stadium_controller import StadiumController
from controllers.match_controller import MatchController
from controllers.ticket_controller import TicketController
from controllers.client_controller import ClientController
from controllers.product_controller import ProductController
from controllers.restaurant_sale_controller import RestaurantSaleController
from controllers.statistics_controller import StatisticsController

if __name__ == "__main__":
    # Inicializar controladores
    team_controller = TeamController()
    stadium_controller = StadiumController()
    match_controller = MatchController(team_controller, stadium_controller)
    ticket_controller = TicketController()
    client_controller = ClientController()
    product_controller = ProductController()
    restaurant_sale_controller = RestaurantSaleController(product_controller)
    statistics_controller = StatisticsController()

    # Cargar datos iniciales desde la API
    cargar_datos_iniciales(team_controller, stadium_controller, match_controller)

    # Ejemplo de agregar productos al restaurante
    product_controller.add_product("Hamburguesa", "Comida", 5.99, is_packaged=False)
    product_controller.add_product("Cerveza", "Bebida", 2.99, is_alcoholic=True)
    product_controller.add_product("Refresco", "Bebida", 1.49, is_alcoholic=False)
    
    # Ejemplo de venta de productos en el restaurante
    client = client_controller.add_client("Juan Perez", "12345678", 30)
    sale = restaurant_sale_controller.sell_product(client, "Hamburguesa", 2)
    if isinstance(sale, dict):
        print(f"\nVenta exitosa: Cliente {sale['client'].name}, Producto {sale['product'].name}, Cantidad {sale['quantity']}, Precio total {sale['total_price']}")
    else:
        print(f"\nVenta fallida: {sale}")
    
    # Intento de venta de producto alcohólico a menor de edad
    underage_client = client_controller.add_client("Pedro Gomez", "87654321", 17)
    sale = restaurant_sale_controller.sell_product(underage_client, "Cerveza", 1)
    if isinstance(sale, dict):
        print(f"\nVenta exitosa: Cliente {sale['client'].name}, Producto {sale['product'].name}, Cantidad {sale['quantity']}, Precio total {sale['total_price']}")
    else:
        print(f"\nVenta fallida: {sale}")
