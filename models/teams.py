
import requests

class Team:
    def __init__(self, name, fifa_code, group):
        self.name = name
        self.fifa_code = fifa_code
        self.group = group

def load_teams_from_api():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    response = requests.get(url)
    teams_data = response.json()
    
    teams = []
    for team_data in teams_data:
        team = Team(team_data['country'], team_data['fifa_code'], team_data['group'])
        teams.append(team)
    
    return teams


