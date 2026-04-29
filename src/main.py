"""
main.py
Archivo principal del sistema
"""

from colorama import Fore, Style, init
init(autoreset=True)

from menu import show_menu, handle_option


print(Fore.YELLOW + Style.BRIGHT + '=' * 100)
print(Fore.RED + Style.BRIGHT + '==== Bienvenido al Sistema de Gestión de Clientes ====')
print(Fore.YELLOW + Style.BRIGHT + '=' * 100 + '\n')


while True:
    try:
        show_menu()
        option = input('Seleccione una opción: ').strip()

        if option == '9':  
            print(Fore.BLUE + Style.BRIGHT + 'Gracias por usar el sistema. ¡Hasta luego!')
            break

        handle_option(option)

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f'Error inesperado: {e}')