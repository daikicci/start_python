# Задание 1.
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.date = str(date)
        try:
            self.day, self.month, self.year = Date.get_int_date(self.date)
        except TypeError:
            print('Передана некорректная дата.')

    def __str__(self):
        try:
            return '-'.join(list(map(lambda x: str(x), [self.day, self.month, self.year])))
        except AttributeError:
            return 'Печатать нечего.'

    @classmethod
    def get_int_date(cls, date):
        try:
            date_int_list = list(map(lambda x: int(x), date.split('-')))
            if len(date_int_list) != 3:
                raise IndexError
            date_int_list = cls.validate_int_date(date_int_list)
            return date_int_list
        except (ValueError, IndexError):
            return

    @staticmethod
    def validate_int_date(date_list):
        if 0 in date_list:
            return
        day, month, year = date_list
        leap_year = year % 4 == 0
        long_month = [1, 3, 5, 7, 8, 10, 12]
        if month > 12:
            return
        if month in long_month:
            if day > 31:
                return
        elif month == 2:
            day_count = 29 if leap_year else 28
            if day > day_count:
                return
        else:
            if day > 30:
                return
        return date_list


print('Передаем слова вместо чисел')
date_1 = Date('пять-десять-двадцать пять')
print(date_1)
print()

print('Передаем недостаточно чисел')
date_2 = Date('05-12')
print(date_2)
print()

print('Одно из чисел - 0')
date_3 = Date('05-12-0000')
print(date_3)
print()

print('Число больше диапазона')
date_4 = Date('45-6-2019')
print(date_4)
print()

print('Месяц больше диапазона')
date_5 = Date('12-29-2019')
print(date_5)
print()

print('31 число в апреле')
date_6 = Date('31-04-2019')
print(date_6)
print()

print('29 число в феврале невисокосного года')
date_6 = Date('29-02-2019')
print(date_6)
print()

print('Просто хорошая дата')
date_7 = Date('15-05-2020')
print(date_7)
print()

print('31 число в марте')
date_8 = Date('31-03-2019')
print(date_8)
print()

print('29 число в феврале високосного года')
date_9 = Date('29-02-2000')
print(date_9)
print()
