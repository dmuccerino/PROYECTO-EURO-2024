import requests
from models.team import load_teams_from_api
from models.stadium import load_stadiums_from_api

class Ticket:
    def __init__(self, cliente, partido, tipo_entrada, asiento, precio):
        self.cliente = cliente
        self.partido = partido
        self.tipo_entrada = tipo_entrada
        self.asiento = asiento
        self.precio = precio


    def calculate_ticket_price(self):
        base_price = 35 if self.ticket_type == 'General' else 75
        total_price = base_price
        
        if self.is_vampire_number(self.cedula):
            total_price *= 0.5
        
        total_price *= 1.16
        
        return total_price

    def is_vampire_number(self, cedula):
        cedula_str = str(cedula)
        n = len(cedula_str)
        
        if n % 2 != 0 or n < 2:
            return False
        
        half_n = n // 2
        part1 = int(cedula_str[:half_n])
        part2 = int(cedula_str[half_n:])
        
        product = part1 * part2
        
        product_str = str(product)
        
        if sorted(cedula_str) == sorted(product_str):
            return True
        else:
            return False

def select_seat(match):
    # Implementar lógica para seleccionar asiento según disponibilidad
    pass

def sell_ticket(client_name, cedula, age, match, ticket_type):
    seat_number = select_seat(match)
    ticket = Ticket(client_name, cedula, age, match, ticket_type, seat_number, Ticket.calculate_ticket_price())
    return ticket

def save_ticket_to_file(ticket):
    with open('tickets.txt', 'a') as file:
        file.write(f"Client Name: {ticket.client_name}, Cedula: {ticket.cedula}, Match: {ticket.match}, Seat: {ticket.seat_number}, Price: {ticket.price}\n")
