import requests
from controllers.team_controller import TeamController
from controllers.stadium_controller import StadiumController
from controllers.match_controller import MatchController

def cargar_datos_iniciales(team_controller, stadium_controller, match_controller):
    teams_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    stadiums_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    matches_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"

    teams_data = requests.get(teams_url).json()
    stadiums_data = requests.get(stadiums_url).json()
    matches_data = requests.get(matches_url).json()

    for team in teams_data:
        team_controller.add_team(team['country'], team['fifa_code'], team['group'])

    for stadium in stadiums_data:
        stadium_controller.add_stadium(stadium['name'], stadium['location'])

    for match in matches_data:
        match_controller.add_match(match['id'], match['home_team'], match['away_team'], match['date'], match['stadium'])
