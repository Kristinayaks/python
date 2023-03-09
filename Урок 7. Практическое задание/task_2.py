"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def total_consumption(self):
        return f"Общий расход ткани: {(self.param / 6.5 + 0.5) + (2 * self.param + 0.3) :.2f}"

    @abstractmethod
    def abstract_met(self):
        return "Метод абстрактный"


class Coat(Clothes):
    def coat_consumption(self):
        return f"Расход ткани для пошива пальто: {self.param / 6.5 + 0.5 :.2f} м.кв."

    def abstract_met(self):
        return "Метод абстрактный2"


class Costume(Clothes):
    def costume_consumption(self):
        return f"Расход ткани для пошива костюма: {2 * self.param + 0.3 :.2f} м.кв."

    def abstract_met(self):
        pass


coat = Coat(25)
costume = Costume(1.60)
print(coat.coat_consumption())
print(costume.costume_consumption())
# Не могу вывести на экран общий расход ткани. Прошу подсказать в чем причина.
# Пробовала так: clothes = Clothes(25, 1.60)
# print(clothes.total_consumption)
