from colorama import Fore, init
from src.validate import validate_customer
from src.file import load_data, save_data

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



raw_data = load_data()
customers = [Customer(**c) for c in raw_data]


def new_register(id, name, email, phone):
    try:
        validate_customer(customers, id, email)

        new_customer = Customer(id, name, email, phone)
        customers.append(new_customer)

        save_data([c.to_dict() for c in customers])

        return True

    except ValueError:
        return False



def list_records():
    if not customers:
        return []

    return sorted(customers, key=lambda c: c.name.lower())



def search_record(term):
    return [
        c for c in customers
        if term.lower() in c.name.lower() or str(c.id) == str(term)
    ]



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
            return True

    return False



def delete_record(id):
    global customers

    new_list = [c for c in customers if str(c.id) != str(id)]

    if len(new_list) == len(customers):
        return False

    customers = new_list
    save_data([c.to_dict() for c in customers])

    return True