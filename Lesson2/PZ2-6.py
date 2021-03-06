"""
Практическое задание 2-6

Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами,то есть
характеристиками товара: название, цена, количество, единица измерения).

Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название.
Тогда значение — список значений-характеристик, например список названий товаров.

Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

input_string = None
product = None
l_property, l_product = list(), list()
d = dict()
l_kort = tuple()
i = 1

while input_string != '':
    input_string = input("Введите данные по товару в следующей последовательности через пробел:\nнаименование цена "
                     "количество единица измерения\nДля завершения ввода при очередном запросе ввода нажмите Enter: ")
    l_property = input_string.split(" ")
    if input_string != '':

        d.update({"Название": l_property[0], "Цена": l_property[1],
                  "Количество": l_property[2], "Ед.измерения": l_property[3]})
        product = (i, d)
        l_product.append(tovar)
        i += 1
    else:
        break

i = 0
print("[")
while i < len(l_product):
    print(l_product[i])
    i += 1
print("]")