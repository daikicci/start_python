# Задание 1.
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func(divident, divider):
    """Возвращает частное от деления."""

    try:
        result = float(divident) / float(divider)
    except (ValueError, ZeroDivisionError):
        return 0.0
    else:
        return result


first_num = input('Введи первое число: ')
second_num = input('Введи второе число: ')
quotient = div_func(first_num, second_num)
if quotient == 0.0:
    print('Что-то не то ты пытаешься делить.')
else:
    print(f'Разделили одно на другое, получили {round(quotient, 3)}.')
