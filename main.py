import sys
import os

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
    statistics_controller = StatisticsController(match_controller, ticket_controller, client_controller, restaurant_sale_controller)

    # Cargar datos iniciales desde la API
    cargar_datos_iniciales(team_controller, stadium_controller, match_controller)

    # Ejemplos de gestión de venta en restaurante
    print("\nEjemplo de venta de producto en restaurante:")
    restaurant_sale_controller.vender_producto("Juan Perez", "Hamburguesa", 2)

    # Ejemplos de generación de reportes
    print("\nEjemplo de generar reporte de ventas en restaurante:")
    reporte_ventas = statistics_controller.generar_reporte_ventas()
    for venta in reporte_ventas:
        print(f"Cliente: {venta['cliente']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Total: ${venta['total']:.2f}")
