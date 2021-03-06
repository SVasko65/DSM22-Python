"""
Практическое задание 5-6

Сформировать (не программно) текстовый файл.
В нем каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.

Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{"Информатика": 170, "Физика": 40, "Физкультура": 30}
"""


def obrabotka(elm: list):
    """ Выбираем в списке существенные данные """
    j = 0
    while j < len(elm):
        if elm[j].find(':') != -1:
            elm[j] = elm[j].replace(':', '')
        elif elm[j].find('(') != -1:
            elm[j] = elm[j][:(elm[j].find('('))]
        elif elm[j].find('-') != -1:
            elm[j] = 0
        j += 1
    return elm


my_dic = {}

my_file = open("my_fileZ6.txt", "r", encoding='cp1251')

# Чтение строк из файла и их обработка
print(f"Начата обработка файла {my_file.name}:")
while True:
    f_str = my_file.readline()
    if len(f_str) != 0:
        str_obr = obrabotka((f_str.split(' ')))
        my_dic[str_obr[0]] = int(str_obr[1]) + int(str_obr[2]) + int(str_obr[3])
    else:
        break

my_file.close()

# Вывод словаря по форме, указанной в задании
print(('*' * 50 + '\n'), f"Вывод словаря по форме задания\n{my_dic}")

# Форматированный вывод словаря
print(f"\nФорматированный вывод словаря.\nСписок предметов и общее количество часов по ним:")
for key in my_dic.keys():
    print(f"{key:<15s} - {my_dic[key]:>5d}")

print(f"\nОбработка файла {my_file.name} завершена:")