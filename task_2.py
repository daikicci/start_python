# Задание 2.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class OwnZeroDivisionEx(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    temp_dividend, temp_divisor = input('Введите делимое и делитель через запятую: ').split(',')
    dividend, divisor = float(temp_dividend), float(temp_divisor)
    if divisor == 0:
        raise OwnZeroDivisionEx('На ноль делить нельзя!')
    print(round(dividend / divisor, 4))
except OwnZeroDivisionEx as err:
    print(err)
except ValueError:
    print('Вы ввели не числа.')
