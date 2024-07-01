
class Ticket:
    def __init__(self, codigo, partido):
        self.codigo = codigo
        self.usado = False  # Atributo para controlar si el ticket ha sido usado
        self.partido = partido  # Referencia al partido asociado

    def validar_ticket(self):
        # Implementación para validar si el ticket es auténtico
        # Aquí verificarías si el código coincide con los registros y si no ha sido usado antes
        return not self.usado

    def marcar_como_usado(self):
        self.usado = True

