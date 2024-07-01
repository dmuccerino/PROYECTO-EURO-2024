import requests
import json
from controllers.ticket_controller import VentaTicketsController
from controllers.asist_controller import AsistenciaController
from models.team import Team
from models.stadium import Stadium
from models.match import Match


# Funciones para cargar datos desde las APIs y guardarlos en archivos TXT
def load_teams_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        teams = response.json()
        with open('data/teams.txt', 'w') as file:
            json.dump(teams, file)

def load_stadiums_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        stadiums = response.json()
        with open('data/stadiums.txt', 'w') as file:
            json.dump(stadiums, file)

def load_matches_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        matches = response.json()
        with open('data/matches.txt', 'w') as file:
            json.dump(matches, file)

# URLs de las APIs proporcionadas
teams_api_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'
stadiums_api_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'
matches_api_url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'

# Llamadas para cargar los datos iniciales
load_teams_from_api(teams_api_url)
load_stadiums_from_api(stadiums_api_url)
load_matches_from_api(matches_api_url)

# Crear una instancia del controlador de venta de tickets
def cargar_datos_iniciales():
    with open('data/teams.txt') as file:
        equipos_data = json.load(file)
    with open('data/stadiums.txt') as file:
        estadios_data = json.load(file)
    with open('data/matches.txt') as file:
        partidos_data = json.load(file)

    equipos = [Team(e['name'], e['code'], e['group']) for e in equipos_data]
    estadios = [Stadium(s['name'], s['city']) for s in estadios_data]

    for partido in partidos_data:
        equipo_local = next(e for e in equipos if e.codigo_fifa == partido['home'])
        equipo_visitante = next(e for e in equipos if e.codigo_fifa == partido['away'])
        estadio = next(s for s in estadios if s.nombre == partido['stadium'])
        partido_obj = Match(equipo_local, equipo_visitante, partido['datetime'], estadio)
        venta_tickets_controller.partidos.append(partido_obj)

cargar_datos_iniciales()

venta_tickets_controller = VentaTicketsController()
asistencia_controller = AsistenciaController()

def main():
    while True:
        print("\nMenu:")
        print("1. Registrar Cliente")
        print("2. Mostrar Partidos")
        print("3. Vender Ticket")
        print("4. Validar ticket")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            edad = int(input("Edad: "))
            cliente = VentaTicketsController.registrar_cliente(nombre, cedula, edad)
            print(f"Cliente registrado: {cliente.nombre}")
        elif opcion == "2":
            VentaTicketsController.mostrar_partidos()
        elif opcion == "3":
            VentaTicketsController.mostrar_partidos()
            indice = int(input("Seleccione el partido: "))
            partido = VentaTicketsController.seleccionar_partido(indice)
            tipo = input("Tipo de entrada (General/VIP): ")
            cliente_cedula = input("Ingrese la cédula del cliente: ")
            cliente = next((c for c in VentaTicketsController.clientes if c.cedula == cliente_cedula), None)
            if cliente:
                ticket = VentaTicketsController.vender_ticket(cliente, partido, tipo)
                if ticket:
                    asistencia_controller.registrar_ticket(ticket)  # Registrar el ticket vendido
                    print(f"ticket generado: {ticket.codigo_unico}")
            else:
                print("Cliente no encontrado.")
        elif opcion == "4":
            codigo_unico = input("Ingrese el código único del ticket: ")
            asistencia_controller.validar_ticket(codigo_unico)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
