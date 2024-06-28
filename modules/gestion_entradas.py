
import json
import os

class GestionEntradas:
    def __init__(self):
        self.partidos = self.cargar_datos('partidos.txt')
        self.entradas = []

    def cargar_datos(self, filename):
        with open(os.path.join('data', filename), 'r') as f:
            return [json.loads(line.strip()) for line in f]

    def vender_entrada(self, cliente, partido_id, asiento, descuento=0):
        partido = next((p for p in self.partidos if p['id'] == partido_id), None)
        if not partido:
            print(f'Partido con ID {partido_id} no encontrado.')
            return

        precio_base = 50  # Precio base por entrada, por ejemplo
        precio_final = precio_base * (1 - descuento / 100)
        entrada = {
            'cliente': cliente,
            'partido_id': partido_id,
            'asiento': asiento,
            'precio': precio_final
        }
        self.entradas.append(entrada)
        print(f'Entrada vendida a {cliente} para el partido {partido_id} en asiento {asiento} por {precio_final}€.')

if __name__ == "__main__":
    gestion_entradas = GestionEntradas()
    gestion_entradas.vender_entrada('Juan Perez', 1, 'A1', 10)  # Ejemplo de venta de entrada

