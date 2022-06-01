# Задание 3.
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = input('Введите число: ')
try:
    temp_user_number = int(user_number)
except ValueError:
    print('Эй, это не число!')
else:
    double_number = user_number + user_number
    triple_number = double_number + user_number
    final_number = int(user_number) + int(double_number) + int(triple_number)
    print(f'Сумма чисел n + nn + nnn: {final_number}')
