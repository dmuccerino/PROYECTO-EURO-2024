import requests
import json

# Funciones para cargar datos desde las APIs y guardarlos en archivos TXT
def load_teams_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        teams = response.json()
        with open('data/teams.txt', 'w') as file:
            json.dump(teams, file)

def load_stadiums_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        stadiums = response.json()
        with open('data/stadiums.txt', 'w') as file:
            json.dump(stadiums, file)

def load_matches_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        matches = response.json()
        with open('data/matches.txt', 'w') as file:
            json.dump(matches, file)

# URLs de las APIs proporcionadas
teams_api_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'
stadiums_api_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
matches_api_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'

# Llamadas para cargar los datos iniciales
load_teams_from_api(teams_api_url)
load_stadiums_from_api(stadiums_api_url)
load_matches_from_api(matches_api_url)
