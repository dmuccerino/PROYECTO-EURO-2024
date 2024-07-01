import random
import string
from models.client import Cliente
from models.tickets import Ticket
from utils.api_utils import cargar_partidos

class VentaTicketsController:
    def __init__(self):
        self.clientes = []
        self.ticket = []
        self.partidos = []  # Esta lista debería ser cargada desde los datos iniciales

    def registrar_cliente(self, nombre, cedula, edad):
        cliente = Cliente(nombre, cedula, edad)
        self.clientes.append(cliente)
        return cliente

    def mostrar_partidos(partidos):
        print("Partidos Disponibles:")
        for i, partido in enumerate(partidos, start=1):
         print(f"{i}. {partido.equipo_local} vs {partido.equipo_visitante} - {partido.fecha_hora} - Estadio: {partido.estadio}")
    
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
    
def mostrar_partidos(partidos):
    print("Partidos Disponibles:")
    for i, partido in enumerate(partidos, start=1):
        print(f"{i}. {partido.equipo_local} vs {partido.equipo_visitante} - {partido.fecha_hora} - Estadio: {partido.estadio}")

def seleccionar_asiento():
    # Simulación de un mapa de estadio con asientos disponibles
    mapa_estadio = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "X", "O", "O"],
        ["O", "X", "X", "X", "O"],
        ["O", "O", "O", "O", "O"]
    ]

    print("Mapa del Estadio:")
    for fila in mapa_estadio:
        print(" ".join(fila))

    # Selección de asiento
    fila = int(input("Seleccione la fila (1-5): ")) - 1
    columna = int(input("Seleccione la columna (1-5): ")) - 1

    # Validación de asiento ocupado
    if mapa_estadio[fila][columna] == "X":
        print("Este asiento ya está ocupado. Por favor, seleccione otro.")
        seleccionar_asiento()

    # Marcar asiento como ocupado
    mapa_estadio[fila][columna] = "X"

    return fila, columna

def calcular_costo_entrada(tipo_entrada, descuento_cedula=False):
    if tipo_entrada == "General":
        precio_base = 35
    elif tipo_entrada == "VIP":
        precio_base = 75
    else:
        raise ValueError("Tipo de entrada no válido")

    if descuento_cedula:
        precio_base *= 0.5

    subtotal = precio_base
    iva = subtotal * 0.16
    total = subtotal + iva

    return subtotal, iva, total

# Función principal para la gestión de venta de entradas
def gestion_venta_entradas():
    # Cargar partidos desde la API
    partidos = cargar_partidos()
    
    # Capturar datos del cliente
    nombre = input("Ingrese su nombre: ")
    cedula = input("Ingrese su cédula: ")
    edad = int(input("Ingrese su edad: "))

    Cliente = Cliente(nombre, cedula, edad)

    # Mostrar partidos disponibles
    mostrar_partidos(partidos)

    # Selección de partido
    opcion = int(input("Seleccione el número del partido al que desea asistir: "))
    partido_seleccionado = partidos[opcion - 1]

    # Mostrar información del partido seleccionado
    print("\nDetalles del partido seleccionado:")
    print(f"Equipo Local: {partido_seleccionado.equipo_local}")
    print(f"Equipo Visitante: {partido_seleccionado.equipo_visitante}")
    print(f"Fecha y Hora: {partido_seleccionado.fecha_hora}")
    print(f"Estadio: {partido_seleccionado.estadio}")

# Generación de mapa del estadio y selección de asiento
    print("\nSeleccione su asiento:")
    fila, columna = seleccionar_asiento()
    print(f"Ha seleccionado el asiento {fila + 1}-{columna + 1}.")

    # Selección de tipo de entrada
    tipo_entrada = input("Seleccione el tipo de entrada (General/VIP): ")

    # Cálculo del costo de la entrada
    subtotal, iva, total = calcular_costo_entrada(tipo_entrada, cedula == "666")

    # Mostrar resumen de la entrada
    print("\nResumen de la compra:")
    print(f"Tipo de Entrada: {tipo_entrada}")
    print(f"Asiento: Fila {fila + 1}, Columna {columna + 1}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento (si aplica): {50 if cedula == '666' else 0}%")
    print(f"IVA: ${iva:.2f}")
    print(f"Total a Pagar: ${total:.2f}")

    # Confirmación de pago
    confirmacion_pago = input("¿Desea proceder con el pago? (s/n): ")
    if confirmacion_pago.lower() == "s":
        print("Pago exitoso. ¡Disfrute del partido!")

# Llamar a la función principal para comenzar la gestión de venta de entradas
if __name__ == "__main__":
    gestion_venta_entradas()

