"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZero:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.dividend = dividend

    @staticmethod
    def divide_by_zero(divider, dividend):
        try:
            return divider / dividend
        except:
            return "Делить на ноль нельзя"


div = DivisionByZero(500, 270)
print(DivisionByZero.divide_by_zero(500, 2))
print(DivisionByZero.divide_by_zero(0, 270))
print(DivisionByZero.divide_by_zero(55, 0))
print(div.divide_by_zero(270, 0))
