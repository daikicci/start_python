# Задание 1.
# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.

my_last_name = 'Хината'
my_name = 'Шоё'
my_age = 15
print('Меня зовут %s %s, мне %d лет.' % (my_last_name, my_name, my_age))

sister_name = 'Нацу'
sister_age = 6
print('А мою сестру зовут {1} {0}, ей {2} лет.'.format(sister_name, my_last_name, sister_age))

user_name = input("Введи своё имя: ")
apple_number = int(input("Сколько яблок ты сегодня съел? "))
banana_number = int(input("А бананов? "))
orange_number = None
ate_orange = input("Ел ли ты апельсины? ")
if ate_orange.lower() != 'да' and ate_orange.lower() != 'нет':
    print(f'Мам, а {user_name} не хочет со мной разговаривать!')
else:
    if ate_orange.lower() == 'да':
        orange_number = int(input("А сколько? "))
    print(f'{user_name} сегодня кушал много фруктов, вот они слева направо:\n'
          f'Яблоки: {apple_number:<10}'
          f'Бананы: {banana_number:<10}'
          f'Апельсины: {orange_number if orange_number is not None else "не ел"}')

