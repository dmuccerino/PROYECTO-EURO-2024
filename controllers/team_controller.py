
from models.team import Team

class TeamController:
    def __init__(self):
        self.teams = []

    def add_team(self, country_name, fifa_code, group):
        team = Team(country_name, fifa_code, group)
        self.teams.append(team)
        return team

    def get_team_by_name(self, country_name):
        for team in self.teams:
            if team.country_name == country_name:
                return team
        return None

    def get_all_teams(self):
        return self.teams

