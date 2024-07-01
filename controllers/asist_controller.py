
class AsistenciaController:
    def __init__(self):
        self.tickets = []  # Lista de todos los tickets

    def registrar_ticket(self, ticket):
        self.tickets.append(ticket)

    def validar_ticket(self, codigo_unico):
        for ticket in self.tickets:
            if ticket.codigo_unico == codigo_unico:
                if ticket.utilizado:
                    print("El ticket ya ha sido utilizado.")
                    return False
                else:
                    ticket.marcar_utilizado()
                    print("ticket válido. Se ha registrado la asistencia.")
                    return True
        print("ticket no válido.")
        return False
