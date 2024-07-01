

from models.teams import Team

class TeamController:
    def __init__(self):
        self.teams = []

    def add_team(self, name, fifa_code, group):
        team = Team(name, fifa_code, group)
        self.teams.append(team)

    def get_team(self, name):
        for team in self.teams:
            if team.name == name:
                return team
        return None
