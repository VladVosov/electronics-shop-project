import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
            return self.__name
        else:
            return 'Product name more than 10 characters'

    @staticmethod
    def string_to_number(number):
        number = int(number[0])
        return number

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        all_price = self.price * self.quantity
        return all_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        sale_price = self.pay_rate * self.price
        return sale_price

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Инициализирует экземпляры класса Item данными из файла src/items.csv"""
        cls.all = []
        with open('../src/items.csv', 'r', encoding="utf-8") as file:
            csv_data = csv.DictReader(file)
            for data in csv_data:
                name = data['name']
                price = float(data['price'])
                quantity = int(data['quantity'])
                cls(name, price, quantity)
