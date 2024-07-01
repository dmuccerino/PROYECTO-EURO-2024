
class Ticket:
    def __init__(self, client, match, seat, ticket_type, price, code):
        self.client = client
        self.match = match
        self.seat = seat
        self.ticket_type = ticket_type
        self.price = price
        self.code = code
        self.is_valid = True

    def invalidate(self):
        self.is_valid = False
