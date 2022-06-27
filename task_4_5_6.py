# Задание 4.
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# Задание 5.
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру (например, словарь).
# Задание 6.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod


# Классы исключений
class NoPlaceEx(Exception):
    txt = 'Недостаточно места!'


class NoSuchEquipEx(Exception):
    txt = 'Такую технику не храним.'


class NotEnoughUnitsEx(Exception):
    txt = 'На складе недостаточно единиц техники.'


# Класс хранилища техники
class Storage:
    def __init__(self, name, max_count=0):
        self.name = name
        self.max_count = max_count
        self.curr_rest = self.max_count
        self.equipment = []
        self.equip_names = ['принтер', 'сканер', 'ксерокс']
        self.equip_dict = {el: 0 for el in self.equip_names}

    def __str__(self):
        return f'{self.name.capitalize()}. Свободные места: {self.curr_rest}.'


# Класс склада
class OfficeEquipmentStorage(Storage):

    def receive_equip(self):
        try:
            equip_type = input('Какую технику вы хотите положить на склад? ').lower()
            if equip_type not in self.equip_names:
                raise NoSuchEquipEx
            equip_num = int(input('Сколько единиц техники будет размещено? '))
            if equip_num > self.curr_rest:
                raise NoPlaceEx
            if equip_type == 'принтер':
                param_list = Printer.ask_parameters().split(',')
                for i in range(equip_num):
                    self.equipment.append(Printer(param_list[0], param_list[1], self.name))
            elif equip_type == 'ксерокс':
                param_list = Xerox.ask_parameters().split(',')
                for i in range(equip_num):
                    self.equipment.append(Xerox(param_list[0], param_list[1], self.name))
            else:
                param = Scaner.ask_parameters()
                for i in range(equip_num):
                    self.equipment.append(Scaner(param, self.name))
            self.equip_dict[equip_type] += equip_num
            self.curr_rest -= equip_num
        except NoSuchEquipEx as err:
            print(err.txt)
        except ValueError:
            print('Некорректное значение количества.')
        except NoPlaceEx as err:
            print(err.txt)
        except IndexError:
            print('Некорректно введены данные.')

    def send_equip(self, place_obj):
        try:
            equip_type = input('Какую технику вы хотите перенести? ').lower()
            if equip_type not in self.equip_names:
                raise NoSuchEquipEx
            equip_num = int(input('Сколько единиц техники будет перенесено? '))
            if self.equip_dict[equip_type] < equip_num:
                raise NotEnoughUnitsEx
            if place_obj.curr_rest < equip_num:
                raise NoPlaceEx
            obj_type = Printer if equip_type == 'принтер' else Xerox if equip_type == 'ксерокс' else Scaner
            i = 0  # счетчик перенесенных объектов
            j = 0  # индекс элемента в массиве
            while i < equip_num:
                while j < len(self.equipment):
                    if isinstance(self.equipment[j], obj_type):  # если по индексу лежит объект нужного класса
                        place_obj.equipment.append(self.equipment[j])  # переносим этот объект в нужный отдел
                        self.equipment.pop(j)  # и удаляем со склада
                        # увеличиваем счетчик перенесенных объектов i; индекс j оставляем прежним, т.к. под этим
                        # индексом теперь лежит следующий элемент
                        i += 1
                        if i == equip_num:  # как только перенесли нужное количество объектов, прерываемся
                            break
                    else:
                        j += 1  # если по индексу лежит элемент не того класса, ищем по следующему
            place_obj.equip_dict[equip_type] += equip_num
            self.equip_dict[equip_type] -= equip_num
            place_obj.curr_rest -= equip_num
            self.curr_rest += equip_num
        except NoSuchEquipEx as err:
            print(err.txt)
        except ValueError:
            print('Некорректное значение количества.')
        except NotEnoughUnitsEx as err:
            print(err.txt)
        except NoPlaceEx as err:
            print(err.txt)


# Классы оргтехники
class OfficeEquipment(ABC):
    name = ''

    def __init__(self, model, place=''):
        self.model = model
        self.place = place

    @property
    @abstractmethod
    def function(self):
        pass

    def function_with_docs(self, num):
        return f'{self.function.capitalize()} документы в количестве {num}.'

    def __str__(self):
        return f'Техника: {self.name}\nМодель: {self.model}'

    @staticmethod
    @abstractmethod
    def ask_parameters():
        pass


class Printer(OfficeEquipment):
    name = 'принтер'

    def __init__(self, model, print_type, place='', paint_q=100):
        super().__init__(model, place)
        self.print_type = print_type
        self.paint_q = paint_q

    @property
    def function(self):
        return 'печатаю'

    def function_with_docs(self, num):
        if self.paint_q < num:
            return f'Печать невозможна, не хватает {abs(self.paint_q - num)} eд. краски.'
        else:
            self.paint_q -= num
            ans = super().function_with_docs(num)
            ans += f'\nОсталось краски: {self.paint_q}'
            if self.paint_q < 5:
                ans += '\nКраска на исходе, заправьте картридж.'
            return ans

    def __str__(self):
        return f'Техника: {self.name}\nМодель: {self.model}\nТип печати: {self.print_type}'

    @staticmethod
    def ask_parameters():
        return input('Введите модель и тип печати через запятую: ')


class Xerox(OfficeEquipment):
    name = 'ксерокс'

    def __init__(self, model, copy_type, place=''):
        super().__init__(model, place)
        self.copy_type = copy_type

    @property
    def function(self):
        return 'копирую'

    def __str__(self):
        return f'Техника: {self.name}\nМодель: {self.model}\nТип копии: {self.copy_type}'

    @staticmethod
    def ask_parameters():
        return input('Введите модель и тип копии через запятую: ')


class Scaner(OfficeEquipment):
    name = 'сканер'

    @property
    def function(self):
        return 'сканирую'

    @staticmethod
    def ask_parameters():
        return input('Введите модель: ')


# Начинаем тестирование

print('Тестируем оргтехнику:')

print()

printer = Printer('HP P2035', 'чёрно-белая', '', 10)
print(printer)
print(printer.function_with_docs(6))
print(printer.function_with_docs(9))

print()

xerox = Xerox('Xerox DC 440', 'цветная')
print(xerox)
print(xerox.function_with_docs(5))

print()

scaner = Scaner('Kodak Alaris S2060w')
print(scaner)
print(scaner.function_with_docs(8))

print()

# Создадим склад на 50 мест

equip_storage = OfficeEquipmentStorage('склад', 50)
print(equip_storage)

# Попробуем положить туда технику

# Положим 5 ксероксов
equip_storage.receive_equip()
print(equip_storage)
print()

# Положим 17 сканеров
equip_storage.receive_equip()
print(equip_storage)
print()

# Положим еще 6 ксероксов
equip_storage.receive_equip()
print(equip_storage)
print()

# И 28 принтеров - но столько места не будет
equip_storage.receive_equip()
print(equip_storage)
print()

# Попробуем положить компьютер - но склад не хранит такую технику
equip_storage.receive_equip()
print(equip_storage)
print()

# Посмотрим состояние склада

print(equip_storage.equipment)
print()
print(equip_storage.equip_dict)
print()

# Создадим отделы, в рамках задачи рассматриваем их как хранилища техники

accounting = Storage('бухгалтерия', 15)
hr = Storage('отдел кадров', 12)
marketing = Storage('отдел маркетинга', 7)

# Попробуем перенести технику

# Перенесем 6 ксероксов в бухгалтерию
equip_storage.send_equip(accounting)
print(equip_storage)
print()
print(accounting)
print()

# Посмотрим состояние склада

print(equip_storage.equipment)
print()
print(equip_storage.equip_dict)
print()

# И состояние бухгалтерии

print(accounting.equipment)
print()
print(accounting.equip_dict)
print()

# Перенесем 15 сканеров в бухгалтерию - не хватит места
equip_storage.send_equip(accounting)
print(equip_storage)
print()
print(accounting)
print()

# Перенесем 19 сканеров в бухгалтерию - не хватит сканеров
equip_storage.send_equip(accounting)
print(equip_storage)
print()
print(accounting)
print()

# Попробуем перенести 4 сканера в бухгалтерию
equip_storage.send_equip(accounting)
print(equip_storage)
print()
print(accounting)
print()

# И еще 4 сканера отправим в отдел кадров
equip_storage.send_equip(hr)
print(equip_storage)
print()
print(hr)
print()

# Посмотрим состояние склада

print(equip_storage.equipment)
print()
print(equip_storage.equip_dict)
print()

# Состояние бухгалтерии

print(accounting.equipment)
print()
print(accounting.equip_dict)
print()

# И состояние отдела кадров

print(hr.equipment)
print()
print(hr.equip_dict)
print()

# Добавим на склад 15 принтеров
equip_storage.receive_equip()
print(equip_storage)
print()

# И перенесем 5 принтеров в отдел маркетинга
equip_storage.send_equip(marketing)
print(equip_storage)
print()
print(marketing)
print()

# И еще 4 в бухгалтерию
equip_storage.send_equip(accounting)
print(equip_storage)
print()
print(accounting)
print()

# Посмотрим состояние склада

print(equip_storage.equipment)
print()
print(equip_storage.equip_dict)
print()

# Состояние бухгалтерии

print(accounting.equipment)
print()
print(accounting.equip_dict)
print()

# И состояние отдела маркетинга

print(marketing.equipment)
print()
print(marketing.equip_dict)
print()
