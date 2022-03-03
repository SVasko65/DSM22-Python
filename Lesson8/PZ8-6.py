"""
Практическое задание 8-6

Продолжить работу над заданием 8-5.
Реализуйте механизм валидации вводимых пользователем данных.

Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

class WareHouse:
    i = 0
    cls_list = []
    cls_dict = {i: cls_list}
    
    def __init__(self, data_input, OfficeEquipment, count):
        self.i += 1
        self.cls_list.clear()
        self.cls_list.append(data_input)       # Дата поступления на склад
        self.cls_list.append(OfficeEquipment)  # Поступившая техника
        self.cls_list.append(count)            # Количество поступившей данной техники
        #self.cls_list[0] = data_input       # Дата поступления на склад
        #self.cls_list[1] = OfficeEquipment  # Поступившая техника
        #self.cls_list[2] = count            # Количество поступившей данной техники


    #def __setitem__(self):
    #   self._dict = {[]}
 
    @property
    def add_to(self):
        """
        Добавляем оргтехнику на склад
        """
        print(self.cls_list)
        
        self.cls_dict[self.i] = self.cls_list
    
    
 
    #def extract(self, name):
    #    ''' извлекаем из значения обьект по названию группы.
    #    дальше можно расширить поиск по серии, марки или еще чему либо'''
    #    if self._dict[name]:
    #        self._dict.setdefault(name).pop(0)
 
class OfficeEquipment:

    def __init__(self, name, price):
        self.name = name    # Наименование оргтехники
        self.price = price  # Цена данной оргтехники

    def __str__(self):
        obj = "{self.name},{self.price}"
        return obj

class Printer(OfficeEquipment):

    def __init__(self, ptypes, price):
        super().__init__('Принтер', price)
        self.ptypes = ptypes  # Модель принтера(лазерный, струйный)
        
class Scanner(OfficeEquipment):
    def __init__(self, stypes, price):
        super().__init__('Сканер', price)
        self.stypes = stypes    # Модель сканера (цветной, черно-белый)
        
class Xerox(OfficeEquipment):
    def __init__(self, producer, price):
        super().__init__('Ксерокс', price)
        self.producer = producer  # Производитель ксерокса
        
class ErrorNumber(Exception):
    
    def __init__(self, text_error):
        self.text = text_error

# Блок проверка программы

my_printer = Printer('Лазерный', 5000)
my_scanner = Scanner('Цветной', 3000)
my_xerox = Xerox('Kyosera',7000)

my1 = WareHouse("03.03.2022", my_printer, '5')
print(WareHouse.i)
my1.add_to()

my2 = WareHouse("04.03.2022", my_scanner, '2')
print(WareHouse.i)
my2.add_to()

my3 = WareHouse("05.03.2022", my_xerox, '1')
print(WareHouse.i)
my3.add_to()

print(WareHouse.cls_dict)




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
