# Задание 6.
# Реализовать два небольших скрипта:
# - итератор, генерирующий целые числа, начиная с указанного;
# - итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл. Вторым пунктом
# необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

user_num = int(input('Введи целое число: '))
user_quantity = int(input('Сколько элементов ты хочешь вывести? '))
my_count = count(user_num)
my_cycle = cycle("ABC")
user_list = []
for el in range(user_quantity):
    user_list.append({next(my_count): next(my_cycle)})
print(f'Твой список: {user_list}')
