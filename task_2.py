# Задание 2.
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    total_fabric = 0

    def __init__(self, name, quantity, color, param):
        self.name = name
        self.quantity = quantity
        self.color = color
        self.param = param
        Clothes.total_fabric += self.fabric_consumption

    @property
    @abstractmethod
    def fabric_consumption_per_unit(self):
        pass

    @property
    def fabric_consumption(self):
        return self.quantity * self.fabric_consumption_per_unit


class Coat(Clothes):

    @property
    def fabric_consumption_per_unit(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def fabric_consumption_per_unit(self):
        return 2 * self.param / 100 + 0.3


coats_1 = Coat('пальто двубортное мужское', 15, 'черный', 48)
coats_2 = Coat('пальто приталенное женское', 28, 'белый', 40)
suits_1 = Suit('костюм классический мужской', 80, 'серый', 175)
suits_2 = Suit('костюм-тройка женский', 35, 'серый', 160)
print(f'Общий расход ткани: {Clothes.total_fabric:.2f}')
