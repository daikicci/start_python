# Задание 2.
# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
# и т.д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно
# использовать функцию input().

my_list = []
print('Заполните список по одному элементу строками или числами. Когда элементы закончатся, введите "конец".')
user_input = input('Введите элемент списка: ')
pos_types = [int, float, complex, str]
while user_input != 'конец':
    # т.к. строкой может быть все что угодно, этот тип проверяем последним; все, что не число, останется строкой
    for i in range(len(pos_types)):
        try:
            pos_types[i](user_input)
        except ValueError:
            continue
        else:
            my_list.append(pos_types[i](user_input))
            break
    user_input = input('Введите элемент списка: ')
print(f'Ваш список: {my_list}')

length = len(my_list)
for i in range(0, length, 2):
    if i == length - 1:
        break
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(f'Поменяем местами четные с нечетными: {my_list}')
