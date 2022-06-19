# Задание 4.
# Реализуйте базовый класс Car.
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
#   turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
#   (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

from random import randint


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоп машина!')

    def turn(self, direction=None):
        print(f'Едем {"направо" if direction == "right" else "налево" if direction == "left" else "прямо"}!')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость превышена! Сбавьте скорость до 60 км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость превышена! Сбавьте скорость до 40 км/ч.')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police or True


town_car = TownCar(randint(0, 200), 'синий', 'Ford Fiesta')
print(f'Название автомобиля: {town_car.name}\n'
      f'Цвет: {town_car.color}\n'
      f'Полицейский: {"да" if town_car.is_police else "нет"}')
town_car.go()
town_car.turn('right')
town_car.show_speed()
town_car.stop()

print()

sport_car = SportCar(randint(0, 300), 'красный', 'Aston Martin Vanquish', False)
print(f'Название автомобиля: {sport_car.name}\n'
      f'Цвет: {sport_car.color}\n'
      f'Полицейский: {"да" if sport_car.is_police else "нет"}')
sport_car.go()
sport_car.turn('left')
sport_car.show_speed()
sport_car.stop()

print()

work_car = WorkCar(randint(0, 200), 'серый', 'Volkswagen Crafter', True)
print(f'Название автомобиля: {work_car.name}\n'
      f'Цвет: {work_car.color}\n'
      f'Полицейский: {"да" if work_car.is_police else "нет"}')
work_car.go()
work_car.turn()
work_car.show_speed()
work_car.stop()

print()

police_car = PoliceCar(randint(0, 200), 'черный', 'Dodge Charger Pursuit')
print(f'Название автомобиля: {police_car.name}\n'
      f'Цвет: {police_car.color}\n'
      f'Полицейский: {"да" if police_car.is_police else "нет"}')
police_car.go()
police_car.turn('right')
police_car.show_speed()
police_car.stop()
