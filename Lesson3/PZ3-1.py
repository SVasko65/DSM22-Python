"""
Практическое задание 3-1

Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_del(divider, divisible):
    """ Функция деления действительных чисел.

    divider - делитель
    divisible - делимое

    """
    if divider == 0:
        print("Деление на нуль запрещено")
        return
    else:
        return divisible / divider


xd_divisible = float(input("Введите число, которое хотите разделить: "))
yd_divider = float(input("Введите число-делитель: "))

if my_del(yd_divider, xd_divisible) is not None:
    print("*" * 30, "\nРезультат деления двух чисел: %0.2f" % my_del(yd_divider, xd_divisible))
