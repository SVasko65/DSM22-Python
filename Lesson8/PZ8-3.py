"""
Практическое задание 8-3

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.

Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""

class ErrorNumber(Exception):
    """ 
    Пользовательский класс-исключение
    """
    def __init__(self, text_error):
        self.text = text_error

input_string = None

# Заполнение списка
while  True: #input_string != 'stop':
    input_string = input("Введите число элемент списка.\n(Чтобы остановить ввод введите 'stop'): ")
    if input_string == 'stop':
        break
    try:
        my_list.append(int(input_string))
    except ValueError:  # перехват стандартного исключения
        print(ErrorNumber(f"!!! Ошибка ввода. Введено ни число - {input_string}. Повторите ввод!!!"))
        continue
    
# Вывод на экран введенный список
print(f"{'*' * 50}\nВведен список чисел: {my_list}")