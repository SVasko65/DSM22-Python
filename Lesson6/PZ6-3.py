"""
Практическое задание 6-3

Реализовать базовый класс Worker (работник).

Определить атрибуты: name, surname, position (должность), income (доход);
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
Создать класс Position (должность) на базе класса Worker;
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income);
Проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    _income = {}

    def __init__(self, name, surname, position, income1, income2):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["Оклад"] = income1
        self._income["Премия"] = income2


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["Оклад"] + self._income["Премия"]


worker1 = Position('Иван', 'Иванов', 'экономист', 20000, 5000)
print("Проверяем значения атрибутов 1-го экземпляра класса Position")
print(f"Полное имя - {worker1.get_full_name()}")
print(F"Доход рабочего - {worker1.get_total_income()}\n")

print('*' * 50)
print("Проверяем значения атрибутов 2-го экземпляра класса Position")
worker2 = Position('Петр', 'Петров', 'инженер', 15000, 7000)
print(f"Полное имя - {worker2.get_full_name()}")
print(F"Доход рабочего - {worker2.get_total_income()}")