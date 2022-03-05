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
    
    def extract(self, out_data, fname, count):
        """
        Выдача оргтехники со склада

        дальше можно расширить поиск по серии, марки или еще чему либо
        """
        ikey=0
        outkey = []
        out_equipment = []
        #aaa = self._cls_dict{:}
        flist = []
        outkey = [(y, (x)) for y, x in self._cls_dict.items() if fname in x]
        print(outkey)
        if len(outkey) == 0:
            print(f"{fname} на складе отсутствует")
        else:   
            ikey = outkey[0][0] # Выделяем ключ найденной оргтехники
            print('Ключ', ikey)
            flist = outkey[0][1] # Выделяем найденную информацию об оргтехнике
            print('Найденная информация ', flist)
            print('До', self._cls_dict[ikey])
            flist[(len(flist)-1)] -= count  # Уменьшаем количество оргтехники на складе
            
            #self._cls_dict[ikey] = flist       # Сохраняем информацию об остатке на складе 
            
            #out_equipment = outkey
            outkey[0][1][0] = out_data
            outkey[0][1][-1] = count
            print('выходные данные ', outkey[0])
            #out_equipment[0][1][0] = out_data
            #out_equipment[0][1][-1] = count
            print('После', self._cls_dict)
            print(f'{fname} списан со склада')
            return out_equipment
            
class Division:
    """
    Учет полученной оргтехники в подразделении
    """
    __i = 1
    _cls_dict = {__i: list()}

    def __init__(self, data_input, cls_equipment, count):
        self.cls_list = list()
        self.cls_list.append(data_input)                            # Дата поступления в подразделение
        self.cls_list.extend(cls_equipment.__str__().split(','))    # Поступившая оргтехника
        self.cls_list.append(count)                                 # Количество поступившей данной оргтехники
 
    def add_to(self):
        """
        Добавляем оргтехнику в подразделение
        """
        self._cls_dict[self.__i] = self.cls_list
        Division.__i += 1
    
    def extract(self, name):
        """
        Выбытие оргтехники из подразделения

        дальше можно расширить поиск по серии, марки или еще чему либо
        """

 
class OfficeEquipment(ABC):

    def __init__(self, name, price):
        self.name = name    # Наименование оргтехники
        self.price = price  # Цена данной оргтехники

    def __str__(self):
        #obj = f"{self.name},{self.price}"
        #return obj
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
outsklada = my2.extract('08.03.2022','Сканер', 1)
print(outsklada)
print(WareHouse._cls_dict)



#i = 0  # Инициализация счетчика
input_string = None
my_list = []

# Заполнение списка
#while  True: #input_string != 'stop':
#    input_string = input("Введите число элемент списка.\n(Чтобы остановить ввод введите 'stop'): ")
#    if input_string == 'stop':
#        break
#    try:
#        my_list.append(int(input_string))
#    except ValueError:  # перехват стандартного исключения
#       print(ErrorNumber(f"!!! Ошибка ввода. Введено ни число - {input_string}. Повторите ввод!!!"))
#        continue
    
# Вывод на экран введенный список
# print(f"{'*' * 50}\nВведен список чисел: {my_list}")

