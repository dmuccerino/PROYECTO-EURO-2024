
import json

# Función para cargar productos desde el archivo JSON
def load_products():
    with open('data/products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    return products

# Función para buscar productos por nombre
def find_product_by_name(name):
    products = load_products()
    found_products = [p for p in products if p['name'].lower() == name.lower()]
    return found_products

# Función para buscar productos por tipo (alimento o bebida)
def find_products_by_type(product_type):
    products = load_products()
    found_products = [p for p in products if p['type'].lower() == product_type.lower()]
    return found_products

# Función para buscar productos por rango de precio
def find_products_by_price_range(min_price, max_price):
    products = load_products()
    found_products = [p for p in products if min_price <= p['price'] <= max_price]
    return found_products

# Función para realizar la venta de productos de restaurante
def sell_product(customer_id, product_name, is_alcoholic, is_underage):
    products = load_products()
    product = next((p for p in products if p['name'].lower() == product_name.lower()), None)
    if product:
        if product['type'].lower() == 'bebida' and is_alcoholic and is_underage:
            return "No se puede vender bebidas alcohólicas a menores de edad."
        
        # Aplicación de descuento si la cédula es un número perfecto
        discount_percentage = 0.15 if is_perfect_number(customer_id) else 0
        discount_amount = product['price'] * discount_percentage
        
        total_price = product['price'] + (product['price'] * 0.16) - discount_amount
        
        # Actualizar inventario (simulado)
        product['stock'] -= 1
        
        return {
            'product_name': product['name'],
            'total_price': total_price,
            'discount_amount': discount_amount,
            'is_discounted': discount_amount > 0
        }
    else:
        return "Producto no encontrado."

# Función auxiliar para verificar si un número es perfecto
def is_perfect_number(number):
    sum_divisors = sum(i for i in range(1, number) if number % i == 0)
    return sum_divisors == number
