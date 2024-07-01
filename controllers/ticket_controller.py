import random
import string
from models.client import Cliente
from models.tickets import Ticket

class VentaTicketsController:
    def __init__(self):
        self.clientes = []
        self.ticket = []
        self.partidos = []  # Esta lista debería ser cargada desde los datos iniciales

    def registrar_cliente(self, nombre, cedula, edad):
        cliente = Cliente(nombre, cedula, edad)
        self.clientes.append(cliente)
        return cliente

    def mostrar_partidos(self):
        for i, partido in enumerate(self.partidos, start=1):
            print(f"{i}. {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} en {partido.estadio.nombre} el {partido.fecha_hora}")
    
    def seleccionar_partido(self, indice):
        return self.partidos[indice - 1]

    def seleccionar_asiento(self, partido):
        try:
            asiento = partido.asignar_asiento()
            return asiento
        except ValueError as e:
            print(e)
            return None

    def calcular_costo_ticket(self, tipo, cedula):
        precio_base = 35 if tipo == "General" else 75
        if self.es_numero_vampiro(cedula):
            precio_base *= 0.5
        return precio_base * 1.16  # Agregar IVA del 16%

    def es_numero_vampiro(self, cedula):
        # Implementar la lógica para verificar si la cédula es un número vampiro
        return False

    def generar_codigo_unico(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def vender_ticket(self, cliente, partido, tipo):
        asiento = self.seleccionar_asiento(partido)
        if asiento is None:
            print("No hay asientos disponibles para este partido.")
            return None
        costo = self.calcular_costo_ticket(tipo, cliente.cedula)
        codigo_unico = self.generar_codigo_unico()
        ticket = ticket(cliente, partido, tipo, asiento, codigo_unico)
        self.ticket.append(ticket)
        print(f"Ticket vendido con éxito! Cliente: {cliente.nombre}, Partido: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}, Asiento: {asiento}, Costo: {costo}, Código: {codigo_unico}")
        return ticket
