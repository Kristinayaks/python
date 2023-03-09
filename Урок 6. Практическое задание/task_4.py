"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    """Базовый класс Car."""

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """Публичный метод go, который сообщает, что машина поехала."""
        return f"Автомобиль {self.name} поехал"

    def stop(self):
        """Публичный метод stop, который сообщает, что машина остановилась."""
        return f"Автомобиль {self.name} остановился"

    def turn_right(self):
        """Публичный метод turn_right, который сообщает, что машина повернула направо."""
        return f"Автомобиль {self.name} повернул направо"

    def turn_left(self):
        """Публичный метод turn_left, который сообщает, что машина повернула налево."""
        return f"Автомобиль {self.name} повернул налево"

    def show_speed(self):
        """Публичный метод show_speed, который показывает текущую скорость автомобиля."""
        return f"Текущая скорость автомобиля {self.name} составляет {self.speed} км/ч"


class TownCar(Car):
    """Дочерний класс TownCar."""

    def __init__(self, speed, color, name, is_police):
        """Публичные атрибуты: speed, color, name, is_police (булево)."""
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость городского автомобиля {self.name} "
              f"составляет {self.speed} км/ч")

        if self.speed > 60:
            return f"Скорость {self.name} превышает допустимой отметки"


class SportCar(Car):
    """Дочерний класс SportCar."""

    def __init__(self, speed, color, name, is_police):
        """Публичные атрибуты: speed, color, name, is_police (булево)."""
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    """Дочерний класс WorkCar."""

    def __init__(self, speed, color, name, is_police):
        """Публичные атрибуты: speed, color, name, is_police (булево)."""
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """Переопределение метода show_speed."""
        print(f"Текущая скорость рабочего автомобиля {self.name} "
              f"составляет {self.speed} км/ч")
        if self.speed > 40:
            return f"Скорость {self.name} превышает допустимой отметки"
        else:
            return f"Скорость {self.name} в пределах допустимой отметки"


class PoliceCar(Car):
    """Дочерний класс PoliceCar."""

    def __init__(self, speed, color, name, is_police):
        """Публичные атрибуты: speed, color, name, is_police (булево)."""
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} является полицейским автомобилем"
        else:
            return f"{self.name} не является полицейским автомобилем"


BMW = SportCar(150, "Синяя", "BMW", False)
Hyundai = TownCar(40, "Черная", "Hyundai", False)
Kia = WorkCar(50, "Белая", "Kia", True)
Toyota = PoliceCar(90, "Голубая", "Toyota", True)
print(Kia.turn_left())
print(f"Если {Hyundai.turn_right()}, то {BMW.stop()}")
print(f"{Kia.go} со скоростью {Kia.show_speed()}")
print(f"Автомобиль {Kia.name} в цвете: {Kia.color}")
print(BMW.show_speed())
print(Hyundai.show_speed())
print(Toyota.police())
print(Toyota.show_speed())
