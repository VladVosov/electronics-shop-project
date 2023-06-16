from src.item import Item

test = Item('nokia', 150, 3)


def test_item():
    """Тестируем присвоение значений"""
    assert test.name == 'nokia'
    assert test.price == 150
    assert test.quantity == 3


def test_calculate_total_price():
    """Тест суммы стоимости всех товаров одного типа"""
    assert Item.calculate_total_price(test) == 450


def test_apply_discount():
    """Тест применения скидки"""
    assert Item.apply_discount(test) == 150

def test_name_setter():
    """Тест изменения названия товара"""
    test.name = "motorolla"
    assert test.name == "motorolla"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_strind_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr_and_str():
    """Тест для магических методов __repr__ and __str__"""
    item2: Item = Item("Микроволновка", 5000, 15)
    assert repr(item2) == "Item('Микроволновка', 5000, 15)"
    assert str(item2) == 'Микроволновка'