
from models.stadium import Stadium

class StadiumController:
    def __init__(self):
        self.stadiums = []

    def agregar_estadio(self, nombre, ubicacion):
        estadio = Stadium(nombre, ubicacion)
        self.stadiums.append(estadio)

    def obtener_estadios(self):
        return self.stadiums

    def obtener_estadio_por_nombre(self, nombre):
        for estadio in self.stadiums:
            if estadio.nombre == nombre:
                return estadio
        return None



