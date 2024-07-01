
class Ticket:
    def __init__(self, cliente, partido, tipo, asiento, codigo_unico):
        self.cliente = cliente
        self.partido = partido
        self.tipo = tipo
        self.asiento = asiento
        self.codigo_unico = codigo_unico
        self.utilizado = False

tickets_emitidos = [
    Ticket("Juan Pérez", "1234567890", "Equipo A vs Equipo B", "VIP", 100.00),
    Ticket("María Gómez", "0987654321", "Equipo C vs Equipo D", "General", 50.00),
]

# Función para validar la autenticidad del ticket
def validar_ticket(codigo_ticket):
    for ticket in tickets_emitidos:
        if ticket.codigo == codigo_ticket:
            if not ticket.usado:
                ticket.usado = True
                return True
            else:
                return False
    return False

# Función para actualizar la asistencia al partido
def actualizar_asistencia(partido, codigo_ticket):
    if validar_ticket(codigo_ticket):
        print(f"¡ticket válido! Asistencia al partido de {partido.equipo_local} vs {partido.equipo_visitante} registrada.")
    else:
         print("Boleto inválido o ya utilizado.")