
class Ticket:
    def __init__(self, cliente, partido, tipo, asiento, codigo_unico):
        self.cliente = cliente
        self.partido = partido
        self.tipo = tipo
        self.asiento = asiento
        self.codigo_unico = codigo_unico
        self.utilizado = False

    def marcar_utilizado(self):
        self.utilizado = True
