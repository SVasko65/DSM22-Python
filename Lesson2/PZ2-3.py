"""
Практическое задание 2-3

Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень)

Напишите решения через list и через dict.
"""
# Инициализируем словаря времен года
l_zima = list([12, 1, 2])
l_vesn = list([3, 4, 5])
l_leto = list([6, 7, 8])
l_osen = list([9, 10, 11])

vr_goda = dict(key_z='Зима', key_v='Весна', key_l='Лето', key_o='Осень')

# Ввод данных
mes = int(input("Введите номер месяца: "))
print('*' * 30)
if mes in l_zima:
    print("Вами введен месяц с номером %d, который соответствует времени года - %s " % (mes, vr_goda.get('key_z')))
elif mes in l_vesn:
    print("Вами введен месяц с номером %d, который соответствует времени года - %s " % (mes, vr_goda.get('key_v')))
elif mes in l_leto:
    print("Вами введен месяц с номером %d, который соответствует времени года - %s " % (mes, vr_goda.get('key_l')))
elif mes in l_osen:
    print("Вами введен месяц с номером %d, который соответствует времени года - %s " % (mes, vr_goda.get('key_o')))
else:
    print('Введено не допустимое число')
