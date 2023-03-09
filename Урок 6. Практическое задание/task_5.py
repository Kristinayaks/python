"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    """Реализация класса Stationery (канцелярская принадлежность)."""
    title: str

    def draw(self):
        """Публичный метод draw (отрисовка)."""
        print("Запуск отрисовки.")


class Pen(Stationery):
    """Создание дочернего класса Pen (ручка)."""
    title = "Ручка"

    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationery):
    """Создание дочернего класса Pencil (карандаш)."""
    title = "Карандаш"

    def draw(self):
        print(f"{self.title} чертит")


class Handle(Stationery):
    """Создание дочернего класса Handle (маркер)."""
    title = "Маркер"

    def draw(self):
        print(f"{self.title} рисует")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
