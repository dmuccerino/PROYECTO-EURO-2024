import requests
import json
import os

def guardar_como_txt(datos, filepath):
    """Guardar datos como líneas de texto en un archivo."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in datos:
            f.write(f"{json.dumps(item)}\n")


def descargar_equipos_desde_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def descargar_estadios_desde_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def descargar_partidos_desde_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def cargar_datos_iniciales():
    """Cargar datos desde la API y guardarlos en archivos .txt."""
    api_urls = {
        'equipos': 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json',
        'estadios': 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json',
        'partidos': 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json',
    }
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)

    for key, url in api_urls.items():
        response = requests.get(url)  # Realizar solicitud GET a la API
        if response.status_code == 200:
            datos = response.json()  # Convertir respuesta JSON a diccionario/lista de Python
            guardar_como_txt(datos, os.path.join(data_dir, f'{key}.txt'))  # Guardar datos en archivo .txt
        else:
            print(f'Error al cargar {key} desde la API')

if __name__ == "__main__":
    cargar_datos_iniciales()
