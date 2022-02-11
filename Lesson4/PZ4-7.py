"""
Практическое задание 4-7

Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.

При вызове функции должен создаваться объект-генератор.

Функция должна вызываться следующим образом: for el in fact(n).

Она отвечает за получение факториала числа.
В цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.

Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
"""

def fact(arg):
    """
    Генераторная функция факториала числа

    arg - исходное число
    """
    result = 1
    for x in range(1, arg + 1, 1):
      result *= x
      yield result
         
     
number = int(input("Для расчета факториала введите положительное целое число: "))

mylist = [arg for arg in fact(number)]  # Вызов вычисления факториала

print("*" * 50, f"\n{number}! = ", end="")  # Вывод разделительной полосы и исходных данных

if len(mylist) == 0: print(f" {i} ")  # 0!

for i in range(1, number+1):  # Оформление процесса вычисления факториала
    print(f" {i} ", end="")
    if i > number-1:
        break
    else:
       print(f"*", end="")
    
if number > 1:
  print("=", mylist[number-1]) # Вывод результата вычисления факториала