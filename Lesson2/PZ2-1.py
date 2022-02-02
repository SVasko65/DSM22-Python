"""
Практическое задание 2-1

Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.

Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
i = 0  # Инициализация счетчика
sch_int = 0
sch_str = 0
sch_com = 0
sch_bool = 0
sch_none = 0
sch_float = 0
my_list = [123, 50.2, False, 'Список', None, 'F', complex(17, 5)]
# print(len(my_list), i)
while i < len(my_list):
    print("%d элемент списка - " % i, type(my_list[i]))
    # Подсчет типов данных в списке
    if str(type(my_list[i])) == "<class 'int'>":
        sch_int = sch_int + 1
    elif str(type(my_list[i])) == "<class 'str'>":
        sch_str = sch_str + 1
    elif str(type(my_list[i])) == "<class 'float'>":
        sch_float = sch_float + 1
    elif str(type(my_list[i])) == "<class 'bool'>":
        sch_bool = sch_bool + 1
    elif str(type(my_list[i])) == "<class 'NoneType'>":
        sch_none = sch_none + 1
    elif str(type(my_list[i])) == "<class 'complex'>":
        sch_com = sch_com + 1
    i = i + 1
print("В представленном списке: int - %d; str - %d; float - %d; bool - %d; None - %d; complex - %d \n"
      % (sch_int, sch_str, sch_float, sch_bool, sch_none, sch_com))
