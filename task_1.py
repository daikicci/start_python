# Задание 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

int = 394
float = 9.75
complex = complex(5, 4)
str = 'крокодил'
list = ['ехал', 'грека', 'через', 'реку']
tuple = (4, 8, 15, 16, 23, 42)
set = set('император')
frozenset = frozenset('императрица')
dict = {'name': 'Шоё', 'last_name': 'Хината', 'age': 15}
bool = True
bytes = b'word'
bytearray = bytearray(bytes)
none = None

my_list = [int, float, complex, str, list, tuple, set, frozenset, dict, bool, bytes, bytearray, none]

print(f'Типы элементов списка:')
for i, el in enumerate(my_list, 1):
    print(f'{i}. {el} - {type(el)}')
