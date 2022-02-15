"""
Практическое задание 5-4

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_list = list()

sl_numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
             'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Zero': 'Нуль'}


my_file = open("my_fileZ4.txt", "r", encoding='cp1251')

# Чтение строк из файла и их преобразование
print(f"Начато преобразование строк из файла {my_file.name}:")
while True:
    f_str = my_file.readline()
    if len(f_str) != 0:
        str_obr = f_str.split(' ')
        #  print(f"{f_str}", end='')
        str_obr[0] = sl_numbers.get(str_obr[0])
        #  print(f"Преобразована в\n{str_obr[0] + ' ' + str_obr[1] + ' ' + str_obr[2]}")
        my_list.append(str_obr[0] + ' ' + str_obr[1] + ' ' + str_obr[2])
    else:
        break

my_file.close()

# Запись нового блока строк в файл
with open("my_fileZ4P.txt", "w", encoding='cp1251') as my_file2:
    my_file2.writelines(my_list)

print(f"Преобразование строк из файла - {my_file.name} - завершено.\n"
      f"Обработанные данные записаны в новый файл - {my_file2.name}")