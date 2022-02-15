"""
Практическое задание 5-3

Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""
calculation_str = 0
my_list = list()
s_profit = 0
a = 0
my_file = open("my_fileZ3.txt", "r")

while True:
    f_str = my_file.readline()
    if len(f_str) != 0:
        str_obr = f_str.split(' ')
        calculation_str += 1
        str_obr[1] = str_obr[1].replace('\n','')
        s_profit = s_profit + float(str_obr[1])
        if float(str_obr[1]) < 20000.00:
            my_list.append(str_obr)
    else:
        break
my_file.close()

print("Список сотрудников, имеющих оклад меньше 20 000.")
i = 0
while i < len(my_list):
    print(f"{i + 1}. {my_list[i][0]:<10s} - {my_list[i][1]:>10s}")
    i += 1

print(f"Средняя величина дохода {calculation_str} сотрудников = {(s_profit/calculation_str):.2f}")