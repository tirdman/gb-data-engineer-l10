class NotAvailableDepartmentError(Exception):
    pass


class NotEnoughEquipmentError(Exception):
    pass


departments = ['Отдел 1', 'Отдел 2', 'Отдел 3']


class Storage:

    def __init__(self, name):
        # Название склада
        self.name = name
        # Словарь хранения устройств
        self.__storage_list = {}
        # Словарь текущей информации об устройствах, которые были переданы в отделы
        self.__department = {
            'Отдел 1': [],
            'Отдел 2': [],
            'Отдел 3': [],
        }

    @property
    def storage_list(self):
        return self.__storage_list

    def __str__(self):
        storage_status = f'Текущее состояние склада.\n'
        storage_status += f'Количество устройств на хранении:\n'
        for next_type_eq in self.__storage_list.keys():
            storage_status += f'- {next_type_eq}: {len(self.__storage_list.get(next_type_eq))}\n'

        storage_status += f'---\n'
        storage_status += f'Устройства переданные в отделы:\n'
        for next_department in self.__department.keys():
            current_eqs = {}
            for next_eq in self.__department.get(next_department):
                if next_eq.type_eq() not in current_eqs:
                    current_eqs[next_eq.type_eq()] = 0
                current_eqs[next_eq.type_eq()] += 1

            eq_info = f'{current_eqs}'.strip("{}")
            storage_status += f'{next_department}: {eq_info}\n'

        return storage_status

    # Передача оборудования на хранение
    def transfer_to_department(self, department, type_eq, quantity):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError

            if department not in departments:
                raise NotAvailableDepartmentError(f'Ошибка. Отдела "{department}" не существует в списке доступных')

            if type_eq not in self.__storage_list or len(self.__storage_list.get(type_eq)) < quantity:
                raise NotEnoughEquipmentError(f'Ошибка. На складе недостаточно устройств типа {type_eq}')

            # Единицы снимаются с хранения и передаются в отдел
            eqs = self.__storage_list.get(type_eq)[:quantity]
            del self.__storage_list.get(type_eq)[:quantity]
            self.__department[department] += eqs

        except ValueError as e:
            print('Количество должно быть положительным числом')
        except NotAvailableDepartmentError as e:
            print(e)
        except NotEnoughEquipmentError as e:
            print(e)

    # Проверка дублей сирийный номеров
    def check_sn_duplicate(self, eq):
        return not any(eq.serial_number == next_eq.serial_number for next_eq in self.__storage_list[eq.type_eq()])

    # Прием оборудования на склад
    def receive_equipment(self, eq_list):
        for next_eq in eq_list:

            if next_eq.type_eq() not in self.__storage_list:
                self.__storage_list[next_eq.type_eq()] = []

            if self.check_sn_duplicate(next_eq):
                self.__storage_list[next_eq.type_eq()].append(next_eq)

        return self.__storage_list


class OfficeEquipment:

    def __init__(self, color, brand, model, serial_number):
        self.brand = brand
        self.model = model
        self.color = color
        self.serial_number = serial_number

    def __str__(self):
        return f"Брэнд: {self.brand}, Модель: {self.model}, Цвет: {self.color}, SN: {self.serial_number}"


class Printer(OfficeEquipment):
    __TYPE_EQUIPMENT = 'Принтер'

    @classmethod
    def type_eq(cls):
        return cls.__TYPE_EQUIPMENT

    def __init__(self, color, brand, model, serial_number, is_color_print):
        self.is_color_print = is_color_print
        super().__init__(color, brand, model, serial_number)

    def __str__(self):
        general = super().__str__()
        specific = f"Цветная печать: {'Да' if self.is_color_print else 'Нет'}"
        return f"Тип устройства: {__class__.__TYPE_EQUIPMENT}, {general}, {specific}"


class Scanner(OfficeEquipment):
    __TYPE_EQUIPMENT = 'Сканер'

    @classmethod
    def type_eq(cls):
        return cls.__TYPE_EQUIPMENT

    def __init__(self, color, brand, model, serial_number, is_many_list_scan):
        self.is_many_list_scan = is_many_list_scan
        super().__init__(color, brand, model, serial_number)

    def __str__(self):
        general = super().__str__()
        specific = f"Многостраничное сканирование: {'Да' if self.is_many_list_scan else 'Нет'}"
        return f"Тип устройства: {__class__.__TYPE_EQUIPMENT}, {general}, {specific}"


class Copier(OfficeEquipment, ):
    __TYPE_EQUIPMENT = 'Ксерокс'

    @classmethod
    def type_eq(cls):
        return cls.__TYPE_EQUIPMENT

    def __init__(self, color, brand, model, serial_number, format_paper_support):
        self.format_paper_support = format_paper_support
        super().__init__(color, brand, model, serial_number)

    def __str__(self):
        general = super().__str__()
        specific = f"Поддерживаемые форматы: {', '.join(self.format_paper_support)}"
        return f"Тип устройства: {__class__.__TYPE_EQUIPMENT}, {general}, {specific}"
