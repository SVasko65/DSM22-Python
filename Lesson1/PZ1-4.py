"""
Практическое задание 4.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

# Первая часть задания
chislo = int(input('Введите целое положительное число: '))
a = 1 # Счетчик разрядов числа
b = 10
max_ch = 0
# Вторая часть задания
# Определим разрядность введенного числа и проводим сравнение цифр разрядов
print("Введено число - ", chislo)
max_ch = chislo % b
if chislo < 10:
    print('Вы ввели одноразрядное целое число, которое и представляет собой максимальную цифру - %d !!!' % max_ch)
else:
    while chislo > 10:
        chislo = chislo // b
        a = a + 1
        if chislo > 10:
            if max_ch < (chislo % b):
                max_ch = chislo % b
        else:
            if max_ch < chislo:
                max_ch = chislo
    print('Вы ввели %d-разрядное целое число, в котором максимальным является цифра - %d' % (a, max_ch))