"""
Практическое задание 2-4

Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
i = 0
# Ввод данных
v_str = input("Введите несколько слов, разделив их пробелом: ")

words = v_str.split(" ")
# Проверка введенных слов
print("Вами введены следующие слова: ", words, "\n", '*' * 30)
while i < len(words):
    if len(words[i]) > 10:
        print("%d - %s" % ((i + 1), (words[i][0:10:1])))
    else:
        print("%d - %s" % ((i + 1), words[i]))
    i += 1
