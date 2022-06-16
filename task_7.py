# Задание 7.
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open('task_7.txt', 'r', encoding='utf-8') as my_f:
    str_num = len(my_f.readlines())
    my_f.seek(0)
    profit_dict = {}
    profit_sum = 0
    profit_firm_count = 0
    for i in range(str_num):
        firm_data = my_f.readline().split()
        try:
            profit = float(firm_data[2]) - float(firm_data[3])
            profit_dict[firm_data[0]] = profit
            if profit > 0:
                profit_sum += profit
                profit_firm_count += 1
        except (ValueError, IndexError):
            print('В файле указаны некорректные данные.')

    try:
        average_profit = profit_sum / profit_firm_count
    except ZeroDivisionError:
        print('Ни одна фирма не получила прибыль.')
    else:
        with open('task_7.json', 'w', encoding='utf-8') as my_json:
            json.dump([profit_dict, {'average_profit': average_profit}], my_json, indent=4, ensure_ascii=False)
