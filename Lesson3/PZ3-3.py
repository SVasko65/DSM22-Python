"""
Практическое задание 3-3

Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    if arg1 > arg2:
        if arg1 > arg3:
            fmax1 = arg1
            if arg2 > arg3:
                fmax2 = arg2
            else:
                fmax2 = arg3
        else:
            fmax1 = arg3
            fmax2 = arg1
    elif arg2 > arg3:
        fmax1 = arg2
        if arg1 > arg3:
            fmax2 = arg1
        else:
            fmax2 = arg3
    elif arg1 > arg3:
        fmax1 = arg1
        if arg2 > arg3:
            fmax2 = arg2
        else:
            fmax2 = arg3
    else:
        fmax1 = arg3
        fmax2 = arg2

    return fmax1, fmax2, fmax1 + fmax2


max1 = 0
max2 = 0

perv = int(input("Введите первый аргумент: "))
vtor = int(input("Введите второй аргумент: "))
tret = int(input("Введите третий аргумент: "))

max1, max2, itog = my_func(perv, vtor, tret)

print("*" * 30, f"\nСумма двух наибольших аргументов {max1} и {max2} составляет = {itog}")
