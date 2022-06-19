# Задание 3.
# Реализовать базовый класс Worker (работник).
# - определить атрибуты: name, surname, position (должность), income (доход);
# - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
#   {"wage": wage, "bonus": bonus};
# - создать класс Position (должность) на базе класса Worker;
# - в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
#   (get_total_income);
# - проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
#   значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position.lower()
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker = Position('василий', 'иванов', 'сантехник', 20000, 2000)
print(f'Имя работника: {worker.name}\n'
      f'Фамилия работника: {worker.surname}\n'
      f'Работает на должности: {worker.position}\n'
      f'Полное имя: {worker.get_full_name()}\n'
      f'Доход с учетом премии: {worker.get_total_income()}'
      )
