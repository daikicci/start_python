# Задание 5.
# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
# чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

user_num_list = input('Введи строку чисел, разделенных пробелами: ').split()
user_sum = 0  # сюда будем писать сумму чисел
end_mark = False  # маркер, что встретили специальный символ


def accumulator(num_list, curr_sum):
    found_err = False  # маркер, что в этой итерации уже говорили юзеру о том, что он неправ
    global end_mark
    for el in num_list:
        try:
            curr_sum += float(el)
        except ValueError:
            if el == 'q':
                end_mark = True
                break
            elif found_err:
                continue
            else:
                print('Ну пожалуйста, давай только числа!')
                found_err = True
                continue
    return curr_sum


while not end_mark:
    user_sum = accumulator(user_num_list, user_sum)
    print(user_sum)
    if end_mark:
        break
    user_num_list = input().split()

print('Конец! Кто сложил, тот молодец!')
