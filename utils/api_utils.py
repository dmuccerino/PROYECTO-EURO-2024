
import requests
from controllers.team_controller import TeamController
from controllers.stadium_controller import StadiumController
from controllers.match_controller import MatchController

def cargar_datos_iniciales():
    equipos_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    estadios_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    partidos_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"

    equipos_response = requests.get(equipos_url)
    estadios_response = requests.get(estadios_url)
    partidos_response = requests.get(partidos_url)

    equipos = equipos_response.json()
    estadios = estadios_response.json()
    partidos = partidos_response.json()

    team_controller = TeamController()
    stadium_controller = StadiumController()
    match_controller = MatchController()

    for equipo in equipos:
        team_controller.add_team(equipo['name'], equipo['fifa_code'], equipo['group'])

    for estadio in estadios:
        stadium_controller.add_stadium(estadio['name'], estadio['location'])

    for partido in partidos:
        match_controller.add_match(
            team_controller.get_team(partido['home_team']),
            team_controller.get_team(partido['away_team']),
            partido['date'],
            stadium_controller.get_stadium(partido['stadium'])
        )

    print("Datos iniciales cargados desde la API.")
