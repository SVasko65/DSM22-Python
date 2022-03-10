"""
Практическое задание 8-4

Начните работу над проектом «Склад оргтехники».

Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""

from abc import ABC, abstractmethod

class WareHouse:
    __i = 1
    _cls_dict = {__i: list()}
    
    def __init__(self, data_input, cls_equipment, count):
        self.cls_list = list()
        self.cls_list.append(data_input)                            # Дата поступления на склад
        self.cls_list.extend(cls_equipment.__str__().split(','))    # Поступившая техника
        self.cls_list.append(count)                                 # Количество поступившей данной техники
 
    def add_to(self):
        """
        Добавляем оргтехнику на склад
        """
        self._cls_dict[self.__i] = self.cls_list
        WareHouse.__i += 1
    
 
class OfficeEquipment(ABC):

    def __init__(self, name, price):
        self.name = name    # Наименование оргтехники
        self.price = price  # Цена данной оргтехники

    def __str__(self):
        pass

class mPrinter(OfficeEquipment):

    def __init__(self, ptypes, price):
        super().__init__('Принтер', price)
        self.ptypes = ptypes  # Модель принтера(лазерный, струйный)
    
    def __str__(self):
        return f"{self.name},{self.ptypes},{self.price}"
        
class mScanner(OfficeEquipment):
    def __init__(self, stypes, price):
        super().__init__('Сканер', price)
        self.stypes = stypes    # Модель сканера (цветной, черно-белый)

    def __str__(self):
        return f"{self.name},{self.stypes},{self.price}"
        
class Xerox(OfficeEquipment):
    def __init__(self, producer, price):
        super().__init__('Ксерокс', price)
        self.producer = producer  # Производитель ксерокса

    def __str__(self):
        return f"{self.name},{self.producer},{self.price}"

# Блок проверки программы

my_printer = mPrinter('Лазерный', 5000)
my_scanner = mScanner('Цветной', 3000)
my_xerox = Xerox('Kyosera',7000)

# Оформляем поступление оргтехники на склад
my1 = WareHouse("03.03.2022", my_printer, '5')
my1.add_to()

my2 = WareHouse("04.03.2022", my_scanner, '2')
my2.add_to()

my3 = WareHouse("05.03.2022", my_xerox, '1')
my3.add_to()

# выводим поступившую на склад оргтехнику
print(f"На склад поступила следующая техника:\n{WareHouse._cls_dict}")

