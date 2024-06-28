
import json
import os

class GestionAsistencia:
    def __init__(self):
        self.partidos = self.cargar_datos('partidos.txt')
        self.asistencias = []

    def cargar_datos(self, filename):
        with open(os.path.join('data', filename), 'r') as f:
            return [json.loads(line.strip()) for line in f]

    def registrar_asistencia(self, cliente, partido_id):
        partido = next((p for p in self.partidos if p['id'] == partido_id), None)
        if not partido:
            print(f'Partido con ID {partido_id} no encontrado.')
            return

        asistencia = {
            'cliente': cliente,
            'partido_id': partido_id,
            'asistio': True
        }
        self.asistencias.append(asistencia)
        print(f'Asistencia registrada para {cliente} al partido {partido_id}.')

if __name__ == "__main__":
    gestion_asistencia = GestionAsistencia()
    gestion_asistencia.registrar_asistencia('Juan Perez', 1)  # Ejemplo de registro de asistencia
