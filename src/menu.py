"""
menu.py
Este archivo contiene la lógica de la interfaz de usuario por consola.
"""

# ---------------------------------- IMPORTACIONES ----------------------------------
from colorama import Fore, Style, init
from service import register_customer, view_all_customers, view_customer

init(autoreset=True)

# ---------------------------------- CÓDIGO PRINCIPAL ----------------------------------

def show_menu():
    """Imprime las opciones disponibles en pantalla."""
    print(Fore.CYAN + Style.BRIGHT + "\n--- MENÚ DE GESTIÓN ---")
    print("1. Registrar nuevo cliente")
    print("2. Buscar cliente por ID")
    print("3. Listar todos los clientes")
    print("4. Salir")
    print(Fore.CYAN + "-----------------------")

def handle_option(option):
    """Ejecuta la acción correspondiente a la opción seleccionada."""
    
    if option == '1':
        print(Fore.YELLOW + "\n>> FORMULARIO DE REGISTRO")
        try:
            id = input("ID: ").strip()
            name = input("Nombre: ").strip()
            email = input("Email: ").strip()
            phone = input("Teléfono: ").strip()

            if not id or not name or not email:
                print(Fore.RED + "Error: ID, Nombre y Email son campos obligatorios.")
                return

            if register_customer(id, name, email, phone):
                print(Fore.GREEN + Style.BRIGHT + "✔ Cliente registrado y guardado exitosamente.")
            else:
                print(Fore.RED + "✘ No se pudo completar el registro (ID o Email duplicados).")
        except Exception as e:
            print(Fore.RED + f"Error al procesar el registro: {e}")

    elif option == '2':
        print(Fore.YELLOW + "\n>> BUSCAR CLIENTE")
        search_id = input("Ingrese el ID del cliente: ").strip()
        customer = view_customer(search_id)
        
        if customer:
            print(Fore.GREEN + "\n--- Datos del Cliente ---")
            print(f"ID: {customer.id}")
            print(f"Nombre: {customer.name}")
            print(f"Email: {customer.email}")
            print(f"Teléfono: {customer.phone}")
        else:
            print(Fore.RED + f"No se encontró ningún cliente con el ID: {search_id}")

    elif option == '3':
        print(Fore.YELLOW + "\n>> LISTADO GENERAL DE CLIENTES")
        customers = view_all_customers()
        
        if not customers:
            print(Fore.WHITE + "No hay clientes registrados en la base de datos.")
        else:
            # Encabezado de tabla simple
            print(Fore.BLUE + f"{'ID':<10} {'NOMBRE':<20} {'EMAIL':<25} {'TELÉFONO':<15}")
            print("-" * 70)
            for c in customers:
                print(f"{c.id:<10} {c.name:<20} {c.email:<25} {c.phone:<15}")

    elif option == '4':
        # La lógica de salida se maneja en el break del main.py,
        # así que aquí no necesitamos hacer nada extra.
        pass

    else:
        print(Fore.RED + "Opción no válida. Por favor, intente de nuevo.")