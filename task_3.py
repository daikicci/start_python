# Задача 3.
# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def my_func(num1, num2, num3):
    args = [num1, num2, num3]
    try:
        args = [int(el) for el in args]
    except ValueError:
        return 'Просил целые числа, получил бог весть что.'
    else:
        min_num = min(args)
        args.remove(min_num)
        if min_num in args:
            return 'Хотел сложить два наибольших, да не нашел таких.'
        return f'Сумма двух наибольших: {sum(args)}.'


enter_num = 'Введи три целых числа через пробел: '
user_num_list = input(enter_num).split()
while len(user_num_list) != 3:
    user_num_list = input('Попробуем еще раз. ' + enter_num).split()
sum_two_max = my_func(user_num_list[0], user_num_list[1], user_num_list[2])
print(sum_two_max)

