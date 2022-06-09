# Задача 2.
# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить
# вывод данных о пользователе одной строкой.

def get_user_data(name, last_name, birth_year, city, email, phone_number):
    """
    Выводит информацию о пользователе.

    Именованные параметры:
    name -- имя пользователя
    last_name -- фамилия пользователя
    birth_year -- год рождения
    city -- город проживания
    email -- email
    phone_number -- номер телефона
    """
    return f'Тебя зовут {name.capitalize()} {last_name.capitalize()}, {birth_year} г.р., из города ' \
           f'{city.capitalize()}. Email: {email}, телефон: {phone_number}.'


def get_user_data_v2(**kwargs):
    return kwargs


user_last_name = input('Какая у тебя фамилия? ')
user_name = input('Как тебя зовут? ')
user_birth_year = input('В каком году ты родился? ')
user_city = input('В каком городе живешь? ')
user_email = input('Укажи свой email: ')
user_phone_number = input('Укажи свой телефон: ')

print(get_user_data(last_name=user_last_name, name=user_name, birth_year=user_birth_year, city=user_city,
                    email=user_email, phone_number=user_phone_number))

print(get_user_data_v2(name=user_name, last_name=user_last_name, birth_year=user_birth_year, city=user_city,
                       email=user_email, phone_number=user_phone_number))
