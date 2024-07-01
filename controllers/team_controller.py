

from models.team import Team

from models.team import Team

class TeamController:
    def __init__(self):
        self.teams = []

    def agregar_equipo(self, nombre, codigo_fifa, grupo):
        equipo = Team(nombre, codigo_fifa, grupo)
        self.teams.append(equipo)

    def obtener_equipos(self):
        return self.teams

