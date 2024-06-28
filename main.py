import sys
import os

# Añadir el directorio 'modules' al path de Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from utils.api_handler import cargar_datos_iniciales
from modules.gestion_partidos import GestionPartidos
from modules.gestion_entradas import GestionEntradas
from modules.gestion_asistencia import GestionAsistencia
from modules.gestion_restaurantes import GestionRestaurantes
from modules.gestion_venta_restaurantes import GestionVentaRestaurantes
from modules.indicadores_gestion import IndicadoresGestion

if __name__ == "__main__":
    cargar_datos_iniciales()

    # print("\nEjemplo de mostrar partidos:")
    # gestion_partidos = GestionPartidos()
    # gestion_partidos.mostrar_partidos()

    print("\nEjemplo de venta de entradas:")
    gestion_entradas = GestionEntradas()
    gestion_entradas.vender_entrada("Juan Perez", 1, "A1", 10)

    print("\nEjemplo de registro de asistencia:")
    gestion_asistencia = GestionAsistencia()
    gestion_asistencia.registrar_asistencia("Juan Perez", 1)

    print("\nEjemplo de agregar producto a restaurante:")
    gestion_restaurantes = GestionRestaurantes()
    gestion_restaurantes.agregar_producto("Hamburguesa", "Comida", 5.99)

    print("\nEjemplo de venta de producto en restaurante:")
    gestion_venta_restaurantes = GestionVentaRestaurantes(gestion_restaurantes)
    gestion_venta_restaurantes.vender_producto("Juan Perez", "Hamburguesa",2)

    print("\nGeneración de reportes:")
    indicadores_gestion = IndicadoresGestion()
    indicadores_gestion.generar_reporte_entradas()
    indicadores_gestion.generar_reporte_ventas()
