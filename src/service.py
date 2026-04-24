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
        return {"id": self.id, "name": self.name, "email": self.email, "phone": self.phone}

# Cargar datos al iniciar el módulo
raw_data = load_data()
customers = [Customer(**c) for c in raw_data]

def register_customer(id, name, email, phone):
    if validate_customer(customers, id, email):
        new_customer = Customer(id, name, email, phone)
        customers.append(new_customer)
        
        # Persistencia: Convertir lista de objetos a lista de diccionarios y guardar
        data_to_save = [c.to_dict() for c in customers]
        if save_data(data_to_save):
            return True
    return False

def view_customer(id):
    for customer in customers:
        if str(customer.id) == str(id):
            return customer
    return None

def view_all_customers():
    # Retornamos la lista cargada (que ya incluye lo del JSON)
    return customers