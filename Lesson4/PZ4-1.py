"""
Практическое задание 4-1

Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
Используйте в нем формулу: (выработка в часах * ставка в час) + премия.

Во время выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def raschet(r_hour: int, r_rate: int, r_prize: int):
    """ Расчет заработной платы сотрудника

    r_hour - выработка в часах
    r_rate - ставка в час
    r_prize - премия

    """
    return (r_hour * r_rate) + r_prize

print(f'Для расчета заработной платы работника введите следующие данные:/n')
hour = input("Сотрудник отработал (час): ")
rate = input("Почасовая ставка составляет (руб): ")
prize = input("Cотруднику предусмотрена премия (руб): ")

print('*' * 30)
print(f"Заработная плата сотрудника составляет (руб): {raschet(int(hour), int(rate), int(prize))}")