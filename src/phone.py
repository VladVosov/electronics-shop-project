from src.item import Item
class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = None
        self.number_of_sim = number_of_sim

        @property
        def number_of_sim(self):
            return self._number_of_sim

        @number_of_sim.setter
        def number_of_sim(self, number):
            if number <= 0:
                raise ValueError ('Количество физических SIM-карт должно быть целым числом больше нуля')
            self._number_of_sim = number

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
