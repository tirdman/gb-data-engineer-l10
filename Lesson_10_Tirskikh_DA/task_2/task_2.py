class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight_square_meter = None
        self.thickness = None

    def calc_weight(self):
        if not self.weight_square_meter or not self.thickness:
            print("Перед расчетом массы асфальта укажите массу асфальта на 0,01 метр и толщину дороги")
            return
        return self._length * self._width * self.weight_square_meter * self.thickness
