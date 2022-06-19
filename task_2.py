# Задание 2.
# Реализовать класс Road (дорога).
# - определить атрибуты: length (длина), width (ширина);
# - значения атрибутов должны передаваться при создании экземпляра класса;
# - атрибуты сделать защищёнными;
# - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# - использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
#   в 1 см*число см толщины полотна;
# - проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_road_mass(self, layer_mass=25, layer_q=5):
        road_mass = self._length * self._width * layer_mass * layer_q
        return f'{road_mass / 1000:.2f} т.'


try:
    road_length = float(input('Введите длину дороги в метрах: '))
    road_width = float(input('Введите ширину дороги в метрах: '))
    road = Road(road_length, road_width)
    print(f'Необходимая масса асфальта: {road.count_road_mass()}')
except ValueError:
    print('Неверно введены данные.')
