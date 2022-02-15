"""
Практическое задание 5-1

Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.

Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open("my_fileZ1.txt", "w")

print("Вводите строки текста.\n"
      "(Для завершения ввода введите пустую строку.):")
while True:
    input_str = input()
    if len(input_str) > 0:
        my_file.write(input_str + '\n')
    else:
        break
my_file.close()

print('*' * 50) #  Разделительная линия
# Проверка введенных строк
my_file = open("my_fileZ1.txt", "r")
for my_row in my_file:
    print(my_row, end="")

my_file.close()