# Задание 3.
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
# подсчёт средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

from functools import reduce

with open('task_3.txt', 'r', encoding='utf-8') as my_f:
    content = my_f.readlines()
    try:
        staff_salary_dict = {content[i].split()[0]: float(content[i].split()[1].strip()) for i in range(len(content))}
    except (ValueError, IndexError):
        print('В файле указаны некорректные данные.')
    else:
        staff_with_less_salary = []
        for key in staff_salary_dict:
            if staff_salary_dict[key] < 20000:
                staff_with_less_salary.append(key)
        if len(staff_with_less_salary) != 0:
            print('Оклад менее 20000 руб.:')
            for last_name in staff_with_less_salary:
                print(last_name)


        def accumulator(prev_el, el):
            return prev_el + el


        average_salary = reduce(accumulator, staff_salary_dict.values()) / len(content)
        print(f'\nСредний оклад: {average_salary:.2f} руб.')
