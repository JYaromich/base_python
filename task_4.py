from abc import ABC, abstractmethod


class OfficeException(Exception):
    def __init__(self, txt="Неверно введены данные для заполнения"):
        self.txt = txt

    def __str__(self):
        return self.txt


class OfficeEquipment(ABC):
    def __init__(self, mass: int, width: int, height: int, name_company: str, id: int):
        self.mass = mass
        self.width = width
        self.height = height
        self.name_company = name_company
        self.id = id

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, get_mass):
        if get_mass < 0:
            raise OfficeException('Ошибка! Неверно введена масса оборудования. '
                                  'Масса оборудования не может быть меньше 0')
        self.__mass = get_mass

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, get_width):
        if get_width < 0:
            raise OfficeException('Ошибка! Неверно указана ширина оборудования. '
                                  'Ширина оборудования не может быть меньше 0')
        self.__width = get_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, get_height):
        if get_height < 0:
            raise OfficeException('Ошибка! Неверно указана высота оборудования. '
                                  'Высота оборудования не может быть меньше 0')
        self.__height = get_height

    @abstractmethod
    def get_print(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, mass: int, width: int, height: int, name_company: str, id: int, print_way_num: int):
        OfficeEquipment.__init__(self, mass, width, height, name_company, id)
        self.print_way_num = print_way_num

    @property
    def print_way_num(self):
        return self.__print_way_num

    @print_way_num.setter
    def print_way_num(self, get_print_way_num):
        if get_print_way_num < 0:
            raise OfficeException('Ошибка! Неверно указано количество бумагоприемников. Количество '
                                  'бумагоприемников принтера не может быть меньше 0')
        self.__print_way_num = get_print_way_num

    def get_print(self):
        return f'Принтер {self.name_company} со скоростью печати {self.print_way_num} листов/мин.'


class Scanner(OfficeEquipment):
    def __init__(self, mass: int, width: int, height: int, name_company: str, reg_number: int, max_format_scanner: str):
        OfficeEquipment.__init__(self, mass, width, height, name_company, reg_number)
        self.max_format_scanner = max_format_scanner

    @property
    def max_format_scanner(self):
        return self.__max_format_scanner

    @max_format_scanner.setter
    def max_format_scanner(self, get_max_format_scanner):
        if get_max_format_scanner not in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']:
            raise OfficeException('Ошибка! Неверно указан максимальный формат сканирования')
        self.__max_format_scanner = get_max_format_scanner

    def get_print(self):
        return f' Сканер {self.name_company} с максимальным размером для сканирования {self.max_format_scanner}'


class Copier(OfficeEquipment):
    def __init__(self, mass: int, width: int, height: int, name_company: str, id: int, copy_speed: int) -> None:
        OfficeEquipment.__init__(self, mass, width, height, name_company, id)
        self.copy_speed = copy_speed

    @property
    def copy_speed(self):
        return self.__copy_speed

    @copy_speed.setter
    def copy_speed(self, get_copy_speed):
        if get_copy_speed < 0:
            raise OfficeException('Ошибка! Скорость печать не может быть отрицательной')
        self.__copy_speed = get_copy_speed

    def get_print(self):
        return f' Копир {self.name_company} со сокростью копирования {self.copy_speed} листов/мин'


class ConsignmentNote:
    def __init__(self, department: str, equipment: OfficeEquipment):
        self.department = department
        self.equipment = equipment

    def __str__(self):
        return f'{self.equipment.get_print()} получил {self.department} '


class Stock:
    def __init__(self, free_place: int):
        self.product_dict = {}
        for i in range(free_place):
            self.product_dict[i] = None
        self.__consignment_note = []

    @property
    def consignment_note(self):
        return self.__consignment_note

    def add(self, product: OfficeEquipment, place: int):
        self.product_dict[place] = product

    def go_to_department(self, place: int, name_department: str):
        self.__consignment_note.append(ConsignmentNote(name_department, self.product_dict.pop(place)))

    def get_free_place(self):
        return [key for key in self.product_dict.keys() if not self.product_dict[key]]

    def get_product_count(self):
        return len(self.product_dict.values())

    def __str__(self):
        result_str = ''
        for key in self.product_dict.keys():
            if self.product_dict[key]:
                result_str += 'Позиция {} : товар - {} \n'.format(key, self.product_dict[key].get_print())
        return result_str if result_str else 'Склад пустой'


class TerminalInterface:
    def __init__(self):
        print('-' * 100)
        print('Программы СКЛАД 2000')
        print('Давайте создадим слкад')
        print('-' * 100)
        self.__stock = Stock(self.__input_('Введите количество свободного места на складе > '))
        print('Склад создан!\n')

    def __input_(self, str_to_ask):
        while True:
            try:
                return int(input(str_to_ask))
            except ValueError:
                print('Ошибка неверно введены данные. Необходимо вводить цифры!\n')

    def __get_equipment_object(self, type_object: int):
        mass = self.__input_('Введите массу продукта, кг > ')
        width = self.__input_('Введите ширину продукта, см > ')
        height = self.__input_('Введите высоту продукта, см > ')
        corp_name = input('Введите имя производителя > ')
        reg_number = self.__input_('Введите регистрационный номер > '),

        if type_object == 1:
            while True:
                try:
                    num_prin = self.__input_('Введите количество лотков для печати > ')
                    return Printer(mass, width, height, corp_name, reg_number, num_prin)
                except OfficeException as oe:
                    print(oe)

        if type_object == 2:
            while True:
                try:
                    scan_format = input('Введите максимально доступный формат сканирования > ')
                    return Scanner(mass, width, height, corp_name, reg_number, scan_format)
                except OfficeException as oe:
                    print(oe)

        if type_object == 3:
            while True:
                try:
                    return Copier(mass, width, height, corp_name, reg_number, self.__input_('Введите скорость '
                                                                                            'печати > '))
                except OfficeException as oe:
                    print(oe)

    def add_product(self):
        equipment_choice = self.__input_('Для добавления принтера введите 1, '
                                         'для добавления сканера введите 2, '
                                         'для добавления копира введите 3\n> ')
        free_place = self.__input_(f'Свободные места на складе {self.__stock.get_free_place()}. '
                                   f'Введиет куда положить товар\n >')

        self.__stock.add(self.__get_equipment_object(equipment_choice), free_place)

    def view_product(self):
        print(self.__stock)

    def delete_product(self):
        print(f'Сейчас в складе находятся \n {self.__stock}')
        self.__stock.go_to_department(
            self.__input_('Введите номер позиции продукта на складе, дле передачи в предприятие '),
            input('Введиет назавание подразделения куда необходимо передать оборудование ')
        )
        print('Оборудование передано!')

    def do(self):
        try:
            print('-' * 100)
            while action := self.__input_('Для добавления товара на склад, нажмите 1, \n'
                                          'Для передачи оборудования из склада в подразделение компании, нажмите 2, \n'
                                          'Для просмотра содержимого склада, нажмите 3, \n'
                                          'Для просмотра накладных нажмите 4\n'
                                          'Для выхода из программы нажите 5 '
                                          ' \n > '):

                if int(action) == 1:
                    termital.add_product()
                elif int(action) == 2:
                    termital.delete_product()
                elif int(action) == 3:
                    termital.view_product()
                elif int(action) == 4:
                    termital.view_consignment_note()
                elif int(action) == 5:
                    break
                else:
                    print('Ошибка! Для выбора конкретного действия используйте цифры от 1 до 5')
        except ValueError as ve:
            print(ve)

    def view_consignment_note(self):
        for note in self.__stock.consignment_note:
            print(f'{str(note)}\n')


termital = TerminalInterface()
termital.do()
