"""
Практическое задание 7.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат
    спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
    и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""

# Запрашиваем данные
start = int(input('Введите число километров, которые спортсмен пробежал в первый день: '))
predel = int(input('Введите число километров, которые спортсмен должен максимально пробежать в день: '))
print('-' * 15)
# Определяем количество дней
i = 1  # Счетчик дней
a = 0.1  # Процент увеличения
while start >0:
    print('%d-день: %.2f' % (i, start))
    i = i + 1
    start = start + start * a
    if start > predel:
        print('%d-день: %.2f' % (i, start))
        break
print('На %d-день спортсмен достиг результата - не менее %d км' % (i, predel))
