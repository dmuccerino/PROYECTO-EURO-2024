
import requests
from teams import load_teams_from_api
from stadiums import load_stadiums_from_api

class Match:
    def __init__(self, local_team, visitor_team, datetime, stadium):
        self.local_team = local_team
        self.visitor_team = visitor_team
        self.datetime = datetime
        self.stadium = stadium

def load_matches_from_api():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
    response = requests.get(url)
    matches_data = response.json()
    
    teams = load_teams_from_api()
    stadiums = load_stadiums_from_api()
    
    matches = []
    for match_data in matches_data:
        local_team = next((team for team in teams if team.fifa_code == match_data['local_team']), None)
        visitor_team = next((team for team in teams if team.fifa_code == match_data['visitor_team']), None)
        stadium = next((stadium for stadium in stadiums if stadium.name == match_data['stadium']), None)
        
        if local_team and visitor_team and stadium:
            match = Match(local_team, visitor_team, match_data['datetime'], stadium)
            matches.append(match)
    
    return matches


