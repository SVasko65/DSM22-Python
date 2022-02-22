"""
Практическое задание 7-1

Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
   
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __getitem__(self, idx):
        return self.mat[idx]

    def __str__(self):
        """
        Вывод матрицы в привычном виде
        """
        return '\n'.join('\t'.join(map(str, row)) for row in self.mat)

    def __add__(self, other):
        """
        Cложения двух объектов класса Matrix

        self - первая слагаемая матрица
        other - вторая слагаемая матрица
        """
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


matrix1 = [[31, 32, 33], [37, 43, 57], [51, 86, 91]]
matrix2 = [[1, 2, 0], [3, 4,  -1], [5, 6, 1]]
matrix3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


my_matrix1 = Matrix(matrix1)
print(my_matrix1, "\n")
my_matrix2 = Matrix(matrix2)
print(my_matrix2, "\n")
my_matrix3 =Matrix(matrix3)
my_matrix3 = my_matrix1 + my_matrix2
print(f"Сумма двах матриц:\n{my_matrix3}")