# Задание 7.
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создайте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class Complex:
    def __init__(self, real=0, imj=0):
        self.real_part = real
        self.imj_part = imj
        # я не очень поняла, как можно сделать комплексное число так, чтобы оно было именно числом, без complex(),
        # решила пусть будет строкой
        self.num = f'({self.real_part}+{self.imj_part}j)'

    def __str__(self):
        return self.num

    def __add__(self, other):
        real_part = self.real_part + other.real_part
        imj_part = self.imj_part + other.imj_part
        return Complex(real_part, imj_part)

    def __mul__(self, other):
        real_part = self.real_part * other.real_part - self.imj_part * other.imj_part
        imj_part = self.real_part * other.imj_part + other.real_part * self.imj_part
        return Complex(real_part, imj_part)


complex_1 = Complex(6, 8)
complex_2 = Complex(5, 3)
print(complex_1 + complex_2)
print(complex_1 * complex_2)

print()

complex_3 = Complex(3, -5)
complex_4 = Complex(0, 6)
print(complex_3 + complex_4)
print(complex_3 * complex_4)

print()

print(complex_1 + complex_2 + complex_3)
print(complex_1 * complex_2 * complex_3)

