# Задание 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.

user_sec_number = int(input('Введите время в секундах: '))
hour_number = user_sec_number // 3600
min_number = user_sec_number % 3600 // 60
sec_number = user_sec_number % 60
print(f'Ваше время: {hour_number:02}:{min_number:02}:{sec_number:02}')
