"""
Практическое задание 5-5

Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange

list_numbers = list()
summa = 0
i = 1

count = int(input("Введите количество целых чисел, которое будет составлять набор для подсчета: "))

# Формирование числового списка
while i <= count:
    list_numbers.append(randrange(0, 100))
    i += 1

# Сохраняем список в файл
my_file = open("my_fileZ5.txt", "w", encoding='cp1251')
my_file.writelines(' '.join(map(str,list_numbers)))
my_file.close()
print(f"Сохранена в файле {my_file.name} строка чисел: {' '.join(map(str,list_numbers))}",)

# Подсчет суммы чисел из файла
my_file = open("my_fileZ5.txt", "r", encoding='cp1251')
i = 0
f_str = my_file.readline()
if len(f_str) != 0:
    str_obr = f_str.split(' ')  # Преобразуем считанную строку для подсчета
    while i < len(str_obr):
        str_obr[i] = str_obr[i].replace('\n', '')  # Очищаем от лишних символов
        summa = summa + int(str_obr[i])
        i += 1

my_file.close()
print("*" * 50, f"\nСумма чисел в файле {my_file.name} = {summa}")