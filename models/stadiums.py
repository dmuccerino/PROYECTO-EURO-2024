
import requests

class Stadium:
    def __init__(self, name, location):
        self.name = name
        self.location = location

def load_stadiums_from_api():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    response = requests.get(url)
    stadiums_data = response.json()
    
    stadiums = []
    for stadium_data in stadiums_data:
        stadium = Stadium(stadium_data['name'], stadium_data['location'])
        stadiums.append(stadium)
    
    return stadiums


