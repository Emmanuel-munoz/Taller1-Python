import json
import os
from colorama import Fore, Style

# Ruta relativa desde la raíz del proyecto hacia la carpeta data
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')

def load_data():
    """Carga los datos desde el archivo JSON. Maneja errores de archivo no encontrado o dañado."""
    if not os.path.exists(DATA_PATH):
        # Si el archivo no existe, retorna una lista vacía de forma segura
        return []
    
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(Fore.RED + Style.BRIGHT + f"Error al leer el archivo de datos: {e}")
        print(Fore.YELLOW + "Se iniciará con una lista vacía para evitar fallos en el sistema.")
        return []

def save_data(data):
    """Guarda la lista de diccionarios en el archivo JSON."""
    try:
        # Asegurarse de que el directorio exista
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        
        with open(DATA_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(Fore.RED + Style.BRIGHT + f"Error crítico al guardar los datos: {e}")
        return False