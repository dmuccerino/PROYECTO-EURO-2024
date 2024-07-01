
from models.stadiums import Stadium

class StadiumController:
    def __init__(self):
        self.stadiums = []

    def add_stadium(self, name, location):
        stadium = Stadium(name, location)
        self.stadiums.append(stadium)

    def get_stadium(self, name):
        for stadium in self.stadiums:
            if stadium.name == name:
                return stadium
        return None
