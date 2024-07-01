
import json

# Función para cargar la asistencia a los partidos desde el archivo JSON
def load_attendance():
    with open('data/tickets.txt', 'r', encoding='utf-8') as file:
        attendance = file.readlines()
    return attendance

# Función para obtener el promedio de gasto de un cliente VIP en un partido
def average_vip_expenditure():
    # Lógica para calcular el promedio
    pass

# Función para obtener la asistencia a los partidos de mejor a peor
def sort_attendance():
    attendance = load_attendance()
    # Lógica para ordenar la asistencia y calcular relación asistencia/venta
    pass

# Función para encontrar el partido con la mayor asistencia
def max_attendance_match():
    attendance = load_attendance()
    # Lógica para encontrar el partido con mayor asistencia
    pass

# Función para encontrar el partido con más boletos vendidos
def max_tickets_sold_match():
    attendance = load_attendance()
    # Lógica para encontrar el partido con más boletos vendidos
    pass

# Función para encontrar los top 3 productos más vendidos en el restaurante
def top_three_sold_products():
    products = load_products()
    # Lógica para encontrar los top 3 productos más vendidos
    pass

# Función para encontrar los top 3 clientes que más compraron boletos
def top_three_customers():
    attendance = load_attendance()
    # Lógica para encontrar los top 3 clientes que más compraron boletos
    pass

# Función auxiliar para cargar productos desde el archivo JSON
def load_products():
    with open('data/products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    return products
