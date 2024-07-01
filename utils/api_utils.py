import requests
import json
from models import match
from controllers.team_controller import TeamController
from controllers.stadium_controller import StadiumController
from controllers.match_controller import MatchController

def cargar_datos_iniciales():
    equipos_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'
    estadios_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
    partidos_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'
    
    equipos_response = requests.get(equipos_url).json()
    estadios_response = requests.get(estadios_url).json()
    partidos_response = requests.get(partidos_url).json()
    
    team_controller = TeamController()
    stadium_controller = StadiumController()
    match_controller = MatchController(team_controller, stadium_controller)
    
    for equipo in equipos_response:
        team_controller.agregar_equipo(equipo['nombre'], equipo['codigo_fifa'], equipo['grupo'])
    
    for estadio in estadios_response:
        stadium_controller.agregar_estadio(estadio['nombre'], estadio['ubicacion'])
    
    for partido in partidos_response:
        equipo_local = team_controller.obtener_equipos(partido['equipo_local'])
        equipo_visitante = team_controller.obtener_equipos(partido['equipo_visitante'])
        estadio = stadium_controller.obtener_estadio_por_nombre(partido['estadio'])
        match_controller.agregar_partido(equipo_local, equipo_visitante, partido['fecha_hora'], estadio)
    
    return team_controller, stadium_controller, match_controller

# Función para cargar datos de la API de partidos
def cargar_partidos():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
    response = requests.get(url)
    partidos_data = response.json()

    partidos = []
    for partido in partidos_data:
        equipo_local = partido['local_team']
        equipo_visitante = partido['visitor_team']
        fecha_hora = partido['date_time']
        estadio = partido['stadium']
        partido_obj = partido(equipo_local, equipo_visitante, fecha_hora, estadio)
        partidos.append(partido_obj)

    return partidos
