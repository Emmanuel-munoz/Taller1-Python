from colorama import Fore, Style, init
from validate import validate_customer
from file import load_data, save_data

init(autoreset=True)


class Customer:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }


# ==============================
# CARGA INICIAL
# ==============================
raw_data = load_data()
customers = [Customer(**c) for c in raw_data]


# ==============================
# CREATE
# ==============================
def new_register(id, name, email, phone):
    try:
        if validate_customer(customers, id, email):
            new_customer = Customer(id, name, email, phone)
            customers.append(new_customer)

            save_data([c.to_dict() for c in customers])

            print(Fore.GREEN + "✔ Cliente registrado correctamente")
            return True

    except ValueError as e:
        print(Fore.RED + f"✘ Error: {e}")

    return False


# ==============================
# READ (LIST)
# ==============================
def list_records():
    if not customers:
        print(Fore.YELLOW + "No hay clientes registrados")
        return []

    # Uso de lambda para ordenar por nombre
    ordered = sorted(customers, key=lambda c: c.name.lower())

    return ordered


# ==============================
# READ (SEARCH)
# ==============================
def search_record(term):
    # Uso de list comprehension para filtrar
    results = [
        c for c in customers
        if term.lower() in c.name.lower() or str(c.id) == str(term)
    ]

    if not results:
        print(Fore.YELLOW + "No se encontraron resultados")

    return results


# ==============================
# UPDATE
# ==============================
def update_record(id, name=None, email=None, phone=None):
    for customer in customers:
        if str(customer.id) == str(id):

            if name:
                customer.name = name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone

            save_data([c.to_dict() for c in customers])

            print(Fore.GREEN + "✔ Cliente actualizado correctamente")
            return True

    print(Fore.RED + "✘ Error: ID no existe")
    return False


# ==============================
# DELETE
# ==============================
def delete_record(id):
    global customers

    # List comprehension para eliminar
    new_list = [c for c in customers if str(c.id) != str(id)]

    if len(new_list) == len(customers):
        print(Fore.RED + "✘ Error: ID no existe")
        return False

    customers = new_list

    save_data([c.to_dict() for c in customers])

    print(Fore.GREEN + "✔ Cliente eliminado correctamente")
    return True