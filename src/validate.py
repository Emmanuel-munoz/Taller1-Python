def validate_customer(customers: list, id: str, email: str) -> None:
    """
    Valida que el ID y el email no estén duplicados.
    Lanza ValueError si hay conflicto.
    """
    for c in customers:
        if str(c.id) == str(id):
            raise ValueError("El ID ya existe")

        if c.email == email:
            raise ValueError("El email ya existe")