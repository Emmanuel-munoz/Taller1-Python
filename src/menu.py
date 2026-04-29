"""
menu.py
Interfaz de usuario por consola
"""
from integration import export_to_csv, generate_report
from colorama import Fore, Style, init
from service import (
    new_register,
    list_records,
    search_record,
    update_record,
    delete_record
)

init(autoreset=True)


def show_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n--- MENÚ DE GESTIÓN ---")
    print("1. Registrar nuevo cliente")
    print("2. Buscar cliente")
    print("3. Listar todos los clientes")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("7. Exportar reporte CSV")
    print("8. Filtrar reporte")
    print("9. Salir")
    print(Fore.CYAN + "-----------------------")


def handle_option(option):

    # ==========================
    # CREATE
    # ==========================
    if option == '1':
        print(Fore.YELLOW + "\n FORMULARIO DE REGISTRO")
        try:
            id = input("ID: ").strip()
            name = input("Nombre: ").strip()
            email = input("Email: ").strip()
            phone = input("Teléfono: ").strip()

            if not id or not name or not email:
                print(Fore.RED + "Error: ID, Nombre y Email son obligatorios.")
                return

            new_register(id, name, email, phone)

        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    # ==========================
    # SEARCH
    # ==========================
    elif option == '2':
        print(Fore.YELLOW + "\n BUSCAR CLIENTE")
        term = input("Ingrese ID o nombre: ").strip()

        results = search_record(term)

        if results:
            for c in results:
                print(Fore.GREEN + "\n--- Cliente ---")
                print(f"ID: {c.id}")
                print(f"Nombre: {c.name}")
                print(f"Email: {c.email}")
                print(f"Teléfono: {c.phone}")

    # ==========================
    # LIST
    # ==========================
    elif option == '3':
        print(Fore.YELLOW + "\n LISTADO GENERAL")

        customers = list_records()

        if customers:
            print(Fore.BLUE + f"{'ID':<10} {'NOMBRE':<20} {'EMAIL':<25} {'TELÉFONO':<15}")
            print("-" * 70)
            for c in customers:
                print(f"{c.id:<10} {c.name:<20} {c.email:<25} {c.phone:<15}")

    # ==========================
    # UPDATE
    # ==========================
    elif option == '4':
        print(Fore.YELLOW + "\n ACTUALIZAR CLIENTE")

        id = input("ID del cliente: ").strip()
        name = input("Nuevo nombre (Enter para omitir): ").strip()
        email = input("Nuevo email (Enter para omitir): ").strip()
        phone = input("Nuevo teléfono (Enter para omitir): ").strip()

        update_record(
            id,
            name if name else None,
            email if email else None,
            phone if phone else None
        )

    # ==========================
    # DELETE
    # ==========================
    elif option == '5':
        print(Fore.YELLOW + "\n ELIMINAR CLIENTE")

        id = input("ID del cliente: ").strip()

        confirm = input("¿Seguro que deseas eliminarlo? (s/n): ").lower()

        if confirm == 's':
            delete_record(id)
        else:
            print(Fore.CYAN + "Operación cancelada")

    #==========================
    # EXPORT CSV
    # ==========================
    elif option == '7':
        export_to_csv()

    #==========================
    # FILTRO DINAMICO
    # =========================
    elif option =='8':
        print(Fore.YELLOW + "\n FILTRAR REPORTE")

        campo = input("Campo (id, name, email, phone): ").strip()
        valor = input("Valor a buscar: ").strip()

        generate_report(**{campo: valor})

    

    # ==========================
    # EXIT
    # ==========================
    elif option == '6':
        print(Fore.CYAN + "Saliendo del sistema...")

    else:
        print(Fore.RED + "Opción no válida")
        