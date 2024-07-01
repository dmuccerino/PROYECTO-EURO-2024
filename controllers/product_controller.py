
from models.product import Product

class ProductController:
    def __init__(self):
        self.products = []

    def add_product(self, name, category, price, is_alcoholic=False, is_packaged=False):
        product = Product(name, category, price, is_alcoholic, is_packaged)
        self.products.append(product)
        return product

    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def get_products_by_category(self, category):
        return [product for product in self.products if product.category == category]

    def get_products_by_price_range(self, min_price, max_price):
        return [product for product in self.products if min_price <= product.price <= max_price]

    def get_all_products(self):
        return self.products
