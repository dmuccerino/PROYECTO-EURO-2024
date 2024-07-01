
from models.match import Match

class MatchController:
    def __init__(self):
        self.matches = []

    def agregar_partido(self, home_team, away_team, date, stadium):
        match = Match(home_team, away_team, date, stadium)
        self.matches.append(match)

    def get_matches_by_team(self, team_name):
        return [match for match in self.matches if match.home_team.name == team_name or match.away_team.name == team_name]

    def get_matches_by_stadium(self, stadium_name):
        return [match for match in self.matches if match.stadium.name == stadium_name]

    def get_matches_by_date(self, date):
        return [match for match in self.matches if match.date == date]
