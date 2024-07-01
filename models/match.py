
class Match:
    def __init__(self, equipo_local, equipo_visitante, fecha_hora, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha_hora = fecha_hora
        self.estadio = estadio
        self.asientos_disponibles = list(range(1, 101))  # Asientos del 1 al 100

    def asignar_asiento(self):
        if self.asientos_disponibles:
            return self.asientos_disponibles.pop(0)  # Asigna el primer asiento disponible
        else:
            raise ValueError("No hay asientos disponibles")