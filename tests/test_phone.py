from src.phone import Phone
from src.item import Item

phone1 = Phone("iPhone 14", 120_000, 5, 2)

def test_init():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_add():
    """Тест сложения количества товаров в магазине. Неввозможности сложения экзкмпляров других классов"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert item1 + 10000 == 'Складывать можно только объекты Item и дочерние от них'
