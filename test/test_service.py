from src.service import new_register, list_records, customers
from src.file import save_data


def setup_function():
    """
    Limpia datos antes de cada test
    """
    customers.clear()
    save_data([])


def test_create_customer():
    result = new_register("1000", "Test User", "test@mail.com", "123")
    assert result is True



def test_duplicate_id():
    new_register("2000", "User1", "user1@mail.com", "123")

    result = new_register("2000", "User2", "user2@mail.com", "456")
    assert result is False


def test_list_records():
    new_register("3000", "User3", "user3@mail.com", "123")

    records = list_records()

    assert isinstance(records, list)
    assert len(records) == 1