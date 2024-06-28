import json
import os

class GestionPartidos:
    def __init__(self):
        self.equipos = self.cargar_datos('equipos.txt')
        self.estadios = self.cargar_datos('estadios.txt')
        self.partidos = self.cargar_datos('partidos.txt')

    def cargar_datos(self, filename):
        filepath = os.path.join('data', filename)
        if not os.path.exists(filepath):
            print(f"Error: El archivo {filepath} no existe.")
            return []

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = [json.loads(line) for line in f]
            return data
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON en el archivo {filename}: {e}")
            return []
        except Exception as e:
            print(f"Otro error ocurrió al leer el archivo {filename}: {e}")
            return []

    def mostrar_partidos(self):
        for partido in self.partidos:
            print(partido)
