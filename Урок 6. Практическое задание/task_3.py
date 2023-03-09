"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


class Worker:
    """Реализация базового класса Worker (работник)."""
    def __init__(self, name="Иван", surname="Иванов", position="Аналитик", wage=50000, bonus=35000):
        """Публичные атрибуты name, surname, position (должность),
        защищенный атрибут income (доход)."""
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def income(self):
        """Функция, возвращающая данные защищенного атрибута."""
        return self._income


class Position(Worker):
    """Создание класса Position (должность) на базе класса Worker."""

    def get_full_salary(self):
        """Функция, возвращающая общую заработную плату."""
        return self._income["wage"] + self._income["bonus"]


new_worker = Position("Ирина", "Плюсова", "бухгалтер", 30000, 15000)
print(f"Общая заработная плата сотрудника {new_worker.name} {new_worker.surname}"
      f" на должности {new_worker.position}"
      f" составляет {new_worker.get_full_salary()}")
