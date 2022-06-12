from sys import argv


def count_salary(hours, rate, bonus):
    try:
        user_salary = (float(hours) * float(rate)) + float(bonus)
    except ValueError:
        print('Нужно ввести числа!')
    else:
        print(f'Заработная плата: {user_salary:.2f} руб.')


try:
    script_name, first_param, second_param, third_param = argv
except ValueError:
    print('Неверное число параметров!')
else:
    count_salary(first_param, second_param, third_param)
