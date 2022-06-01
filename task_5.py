# Задание 5.
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее
# сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

company_name = input('Как называется ваша фирма? ')
revenue = float(input('Введите выручку вашей фирмы: '))
costs = float(input('Введите издержки вашей фирмы: '))
result = ''
result_sum = 0
result_sum_for_ans = ''
profit = False
if revenue > costs:
    profit = True
    result = 'с прибылью'
    result_sum = revenue - costs
elif revenue < costs:
    result = 'с убытком'
    result_sum = costs - revenue
else:
    result = 'в ноль'
if result_sum:
    result_sum_for_ans = ' ' + str(f'{result_sum:.2f}') + ' руб'
print(f'Фирма «{company_name}» отработала {result}{result_sum_for_ans if result_sum_for_ans else ""}.')
if profit:
    profitability = int(float(f'{result_sum / revenue:.2f}') * 100)
    print(f'Рентабельность фирмы «{company_name}» — {profitability}%.')
    staff_number = int(input('Сколько сотрудников у вас работает? '))
    result_sum_per_staff = f'{result_sum / staff_number:.2f}'
    print(f'Прибыль в расчёте на одного сотрудника — {result_sum_per_staff} руб.')
