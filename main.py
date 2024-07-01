
import sys
import os

# Agregar la ruta del directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(''))

# Importar la función para cargar datos iniciales
from utils.api_utils import cargar_datos_iniciales

def main():
    equipos, estadios, partidos = cargar_datos_iniciales()
    # Aquí puedes continuar con la lógica principal de tu aplicación
    print("Datos iniciales cargados correctamente.")

if __name__ == "__main__":
    main()
