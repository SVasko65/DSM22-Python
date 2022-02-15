"""
Практическое задание 5-2

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

calculation_str = 0
calculation_slov = list()
sum_slov = 0

my_file = open("my_fileZ2.txt", "r", encoding='cp1251')

while True:
    f_str = my_file.readline()
    if len(f_str) != 0:
        calculation_str += 1
        str_obr = f_str.split(' ')
        if str_obr[0] == '\n': # исключаем из подсчета пустую строку
          calculation_slov.append(0)
        else:
          calculation_slov.append(len(str_obr))
    else:
        break
my_file.close()

print(f"В фале {my_file.name} содержится {calculation_str} строк(и)")

i = 0
while i < len(calculation_slov):
    print(f"В {i + 1} строке - {calculation_slov[i]} слов(а)")
    sum_slov = sum_slov + calculation_slov[i]
    i += 1
print(f"В файле {my_file.name} всего {sum_slov} слов(а)")