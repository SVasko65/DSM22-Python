"""
Практическое задание 4-3

Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.

Решите задание в одну строку.

Подсказка: использовать функцию range() и генератор
"""

print(f"В пределах от 20 до 240 имеются следующие числа кратные 20 или 21:\n"
      f"{[elm for elm in range(20, 240) if (elm % 20 ==0 or elm % 21 ==0)]}")