
class AsistenciaController:
    @staticmethod
    def validar_ticket(ticket, partidos):
        for partido in partidos:
            if partido == ticket.partido and not ticket.usado:
                ticket.usado = True
                partido.incrementar_asistencia()
                return True
        return False
    

class PersistenciaController:
    @staticmethod
    def guardar_datos(filename, data):
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')

    @staticmethod
    def cargar_datos(filename):
        data = []
        with open(filename, 'r') as file:
            for line in file:
                data.append(eval(line))
        return data


