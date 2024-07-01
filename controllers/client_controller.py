
from models.client import Client

class ClientController:
    def __init__(self):
        self.clients = []

    def add_client(self, name, id_number, age):
        client = Client(name, id_number, age)
        self.clients.append(client)
        return client

    def get_client_by_id(self, id_number):
        for client in self.clients:
            if client.id_number == id_number:
                return client
        return None
