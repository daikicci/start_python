# Задание 1.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__ () для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_for_print = ''
        for el in self.matrix:
            i = 0
            while i < len(el):
                matrix_for_print += f'{el[i]:<5}'
                i += 1
            else:
                matrix_for_print += '\n'
        return matrix_for_print

    def __add__(self, other):
        try:
            # проверяем, что элементов одинаковое количество
            if len(self.matrix) != len(other.matrix):
                raise IndexError
            # проверяем, что в каждом вложенном списке одинаковое количество элементов
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    raise IndexError

            sum_matrix = [
                [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                for i in range(len(self.matrix))
            ]

        except IndexError:
            return 'Складываем только равноразмерные матрицы.'
        else:
            return Matrix(sum_matrix)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_1 + matrix_2)


matrix_3 = Matrix([[7, 8], [9, 10]])  # матрица, в которой меньше строк
print(matrix_1 + matrix_3)

print()

matrix_4 = Matrix([[7, 8], [9, 10], [11, 12, 13]])  # матрица, в одной из строк которой больше чисел
print(matrix_1 + matrix_4)

print()

matrix_5 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # просто побольше элементов
matrix_6 = Matrix([[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]])
matrix_7 = Matrix([[25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36]])
print(matrix_5 + matrix_6 + matrix_7)
