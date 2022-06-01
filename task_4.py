# Задание 4.
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

user_number = int(input('Введите целое положительное число: '))
max_digit = user_number % 10
while user_number // 10 > 0:
    user_number = user_number // 10
    next_digit = user_number % 10
    if next_digit > max_digit:
        max_digit = next_digit
print(f'Самая большая цифра: {max_digit}')

