# Задание 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = ['ехал', 'грека', 'через', 'реку']
my_tuple = (4, 8, 15, 16, 23, 42)
my_set = set('император')
my_frozenset = frozenset('императрица')
my_dict = {'name': 'Шоё', 'last_name': 'Хината', 'age': 15}
my_bytes = b'word'
my_bytearray = bytearray(my_bytes)

final_list = [394, 9.75, complex(5, 4), 'крокодил', my_list, my_tuple, my_set, my_frozenset, my_dict, True, my_bytes,
              my_bytearray, None]

print(f'Типы элементов списка:')
for i, el in enumerate(final_list, 1):
    print(f'{i}. {el} - {type(el)}')
