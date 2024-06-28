
import json
import os

class GestionRestaurantes:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, tipo, precio):
        producto = {
            'nombre': nombre,
            'tipo': tipo,
            'precio': precio
        }
        self.productos.append(producto)
        print(f'Producto {nombre} agregado.')

    def buscar_productos(self, nombre=None, tipo=None, precio_min=None, precio_max=None):
        resultados = self.productos
        if nombre:
            resultados = [p for p in resultados if nombre.lower() in p['nombre'].lower()]
        if tipo:
            resultados = [p for p in resultados if p['tipo'] == tipo]
        if precio_min is not None:
            resultados = [p for p in resultados if p['precio'] >= precio_min]
        if precio_max is not None:
            resultados = [p for p in resultados if p['precio'] <= precio_max]
        
        for producto in resultados:
            print(f"{producto['nombre']} - {producto['tipo']} - {producto['precio']}€")

if __name__ == "__main__":
    gestion_restaurantes = GestionRestaurantes()
    gestion_restaurantes.agregar_producto('Hamburguesa', 'Comida', 5.5)  # Ejemplo de agregar producto
    gestion_restaurantes.buscar_productos(tipo='Comida')  # Ejemplo de búsqueda de productos
