
from models.stadium import Stadium

class StadiumController:
    def __init__(self):
        self.stadiums = []

    def add_stadium(self, name, location):
        stadium = Stadium(name, location)
        self.stadiums.append(stadium)
        return stadium

    def get_stadium_by_name(self, name):
        for stadium in self.stadiums:
            if stadium.name == name:
                return stadium
        return None

    def get_all_stadiums(self):
        return self.stadiums

