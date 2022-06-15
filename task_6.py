# Задание 6.
# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce

with open('task_6.txt', 'r', encoding='utf-8') as my_f:
    str_num = len(my_f.readlines())
    my_f.seek(0)
    class_dict = {}
    for i in range(str_num):
        string = my_f.readline()
        temp_class_list = string.split(':')
        dict_key = temp_class_list[0]
        temp_hours_str = ''
        # грустно без регулярок :(
        for symb in list(temp_class_list[1]):
            try:
                int(symb)
            except ValueError:
                temp_hours_str += ' '
            else:
                temp_hours_str += symb

        hours_list = temp_hours_str.split()
        hours_num_list = [int(el) for el in hours_list]


        def int_accumulator(prev_el, el):
            return prev_el + el


        hours = reduce(int_accumulator, hours_num_list)

        class_dict[dict_key] = hours
    print(class_dict)
