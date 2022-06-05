# Задание 3.
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.

month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']

season_list = [
    {'name': 'зима', 'adj': 'зимний', 'months': ['декабрь', 'январь', 'февраль']},
    {'name': 'весна', 'adj': 'весенний', 'months': ['март', 'апрель', 'май']},
    {'name': 'лето', 'adj': 'летний', 'months': ['июнь', 'июль', 'август']},
    {'name': 'осень', 'adj': 'осенний', 'months': ['сентябрь', 'октябрь', 'ноябрь']}
]

month_num = input('Введи порядковый номер месяца: ')
try_again = 'Давай попробуем еще раз. Введи число от 1 до 12: '
while month_num:
    try:
        int(month_num)
    except ValueError:
        month_num = input(f'{try_again}')
        continue
    else:
        month_num = int(month_num)
        if 1 <= month_num <= 12:
            break
        else:
            month_num = input(f'{try_again}')
            continue

month_name = month_list[month_num - 1]
for i in range(len(season_list)):
    if month_name in season_list[i]['months']:
        print(f'{month_num}-й месяц года - {month_name}. Это {season_list[i]["adj"]} месяц.')
        break
