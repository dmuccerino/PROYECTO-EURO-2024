
from models.match import Match
from datetime import datetime

class MatchController:
    def __init__(self, team_controller, stadium_controller):
        self.matches = []
        self.team_controller = team_controller
        self.stadium_controller = stadium_controller

    def add_match(self, local_team_name, visitor_team_name, datetime_str, stadium_name):
        local_team = self.team_controller.get_team_by_name(local_team_name)
        visitor_team = self.team_controller.get_team_by_name(visitor_team_name)
        stadium = self.stadium_controller.get_stadium_by_name(stadium_name)
        match_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

        if local_team and visitor_team and stadium:
            match = Match(local_team, visitor_team, match_datetime, stadium)
            self.matches.append(match)
            return match
        return None

    def get_matches_by_country(self, country_name):
        return [match for match in self.matches if match.local_team.country_name == country_name or match.visitor_team.country_name == country_name]

    def get_matches_by_stadium(self, stadium_name):
        return [match for match in self.matches if match.stadium.name == stadium_name]

    def get_matches_by_date(self, date):
        return [match for match in self.matches if match.datetime.date() == date]

    def get_all_matches(self):
        return self.matches


