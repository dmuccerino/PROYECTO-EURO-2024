
from models.tickets import Ticket
import random
import string

class TicketController:
    def __init__(self):
        self.tickets = []

    def generate_ticket_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def add_ticket(self, client, match, seat, ticket_type):
        # Precios y descuento
        base_price = 35 if ticket_type == 'General' else 75
        discount = 0.5 if self.is_vampire_number(client.id_number) else 0
        price = base_price * (1 - discount) * 1.16  # Añadir IVA del 16%

        code = self.generate_ticket_code()
        ticket = Ticket(client, match, seat, ticket_type, price, code)
        self.tickets.append(ticket)
        return ticket

    def is_vampire_number(self, number):
        # Implementar la lógica para determinar si un número es vampiro
        pass

    def get_ticket_by_code(self, code):
        for ticket in self.tickets:
            if ticket.code == code:
                return ticket
        return None
