from src import item

test = item.Item('nokia', 150, 3)
def test_item():
    assert test.name == 'nokia'
    assert test.price == 150
    assert test.quantity == 3

def test_calculate_total_price():
    assert item.Item.calculate_total_price(test) == 450

def test_apply_discount():
    assert item.Item.apply_discount(test) == 150