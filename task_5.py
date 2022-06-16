# Задание 5.
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint
from functools import reduce

start_list_num = [randint(0, 100) for i in range(15)]

with open('task_5.txt', 'w+', encoding='utf-8') as my_f:
    start_list_str = [str(el) for el in start_list_num]
    my_f.write(' '.join(start_list_str))
    my_f.seek(0)
    str_list = my_f.readline().split()
    num_list = [int(el) for el in str_list]


    def accumulator(prev_el, el):
        return prev_el + el


    num_sum = reduce(accumulator, num_list)
    print(f'Сумма чисел: {num_sum}')


