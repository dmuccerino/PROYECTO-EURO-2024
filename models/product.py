
class Product:
    def __init__(self, name, category, is_alcoholic=False, is_packaged=False, price=0.0):
        self.name = name
        self.category = category
        self.is_alcoholic = is_alcoholic
        self.is_packaged = is_packaged
        self.price = price
