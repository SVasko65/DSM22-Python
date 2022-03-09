"""
Практическое задание 8-5

Продолжить работу над заданием 8-4.
Разработайте методы, которые отвечают за приём оргтехники на склад
и передачу в определённое подразделение компании.

Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь)
"""

from abc import ABC, abstractmethod

class WareHouse:
    """
    Склад оргтехники
    """
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
        self.cls_list[-2] = int(self.cls_list[-2])  # Преобразовываем цены в число
        self.cls_list[-1] = int(self.cls_list[-1])  # Преобразовываем количество в число
        self._cls_dict[self.__i] = self.cls_list
        WareHouse.__i += 1
    
    @staticmethod
    def extract(out_data, fname, count):
        """
        Выдача оргтехники со склада

        out_data - дата списания оргтехники
        fname    - наименование оргтехники
        count    - количество списываемой оргтехники
        """
        outdata = {}           # Возвращаемая информация о списанной оргтехники
        ikey=0                 # Рабочий ключ по словарю склада
        out_equipment = []     # Рабочая информация для списания оргтехники 
        flist = []             # Рабочая информация об оргтехнике из словаря склада
        outdt = [[y, x] for y, x in WareHouse._cls_dict.items() if fname in x]
        if len(outdt) == 0:    # Проверка наличия оргтехники на складе
            print(f"{fname} на складе отсутствует")
        else:   
            ikey = outdt[0][0]              # Выделяем ключ найденной оргтехники
            flist = outdt[0][1]             # Выделяем найденную информацию об оргтехнике
            flist[(len(flist)-1)] -= count  # Уменьшаем количество оргтехники на складе
            print(f'{fname} списан со склада')
            out_equipment = flist[:]        # Получаем рабочую копию информации для списания в подразделение
            out_equipment[0] = out_data     # Фиксируем в рабочей информации дату списания
            out_equipment[-1] = count       # Фиксируем в рабочей информации количество списываемой оргтехники
            outdata.update({ikey: out_equipment}) #
            return outdata
            
class Division:
    """
    Учет полученной оргтехники в подразделении
    """
    _cls_dict = {}

    def __init__(self, divis, inp_data):
        self.divis = divis
        self.inp_data = inp_data
        self._cls_dict.update({divis: inp_data})  # Включение оргтехники в учет подразделения
        
    def __str__(self):
        return f'{self._cls_dict}'
 
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
        
class ErrorNumber(Exception):
    
    def __init__(self, text_error):
        self.text = text_error

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

# Выводим поступившую на склад оргтехнику
print(f"На склад поступила следующая техника:\n{WareHouse._cls_dict}")

# Передача в подразделение оргтехники
outsklada = WareHouse.extract('08.03.2022','Сканер', 1)
div1 = Division('Основное', outsklada)
print(f"В подразделение '{div1.divis}' поступила следующая оргтехника {div1.inp_data}")
