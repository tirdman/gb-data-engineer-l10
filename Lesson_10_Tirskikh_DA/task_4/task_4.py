from abc import ABC, abstractmethod

clothe_types = ['coat', 'suite']


class ClothesInterface(ABC):

    @abstractmethod
    def get_clothes_rate(self):
        pass


class Clothes(ClothesInterface):
    clothe_items = []

    def __init__(self, clothes_type, clothes_size):
        self.close_type = clothes_type
        self.clothe_size = clothes_size

        Clothes.clothe_items.append(self)

    @property
    def get_clothes_rate(self):
        if self.close_type == 'coat':
            return self.clothe_size / 6.5 + 0.5
        return 2 * self.clothe_size + 0.3

    @staticmethod
    def get_clothes_rate_all():
        all_rate = 0
        for next_item in Clothes.clothe_items:
            all_rate += next_item.get_clothes_rate
        return all_rate
