"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

from datetime import datetime


class StockOfficeEquipment:
    StockOfficeEquipment_address = "600000 г. Владимир, ул. Центральная, д.7"
    StockOfficeEquipment_schedule = "Пн-Пт: 07:00-22:00 Сб-Вс: 07:00-17:00"

    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def stock_get(self, equipment):
        tm = datetime.now()
        self.lists.update({equipment.serial_number: [equipment.title, self, tm]})
        print("На склад "+self.title+" получено оборудование: "+ "" +equipment.title+", "
             "серийный номер: "+ str(equipment.serial_number)+", Дата: "
              + str(tm.day)+'.'+str(tm.month)+'.'+str(tm.year))

    def stock_give(self, equipment, other):
        tm = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title, other, tm]})
        print("Передано оборудование: " + "" + equipment.title + ", серийный номер: " + str(
            equipment.serial_number) + ", Дата: "
              + str(tm.day) + '.' + str(tm.month) + '.' + str(tm.year))
        other.stock_get(equipment)

    def list_equipments(self):
        print("На склад " + self.title + " получено оборудование: ")
        print(self.lists)
        print("Общее количество: ", len(self.lists))
        print("Со склада " + self.title + " выдано оборудование: ")
        print(self.give_lists)
        print("Общее количество: ", len(self.give_lists))


class OfficeEquipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)


class Printer(OfficeEquipment):
    def __init__(self, title, serial_number, print_velocity):
        OfficeEquipment.__init__(self, title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return "Название модели: " + OfficeEquipment.__str__(self) + " ," \
                " Параметры: " + str(self.print_velocity)


class Scanner(OfficeEquipment):
    def __init__(self, title, serial_number, resolution):
        OfficeEquipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return "Название модели: " + OfficeEquipment.__str__(self) + "," \
                "Параметры: " + str(self.resolution)


class Copier(OfficeEquipment):
    def __init__(self, title, serial_number, addit):
        OfficeEquipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return "Название модели: " + OfficeEquipment.__str__(self) + "," \
                "Параметры: " + str(self.addit)


stock1 = StockOfficeEquipment("М7")
stock2 = StockOfficeEquipment("М12")
p = Printer("Pantum", 426799, 200)
s = Scanner("HP", 654321, 3500)
c = Copier("Kyocera", 653829, 75)
p1 = Printer("Epson", 836920, 300)

print(p)
print(s)
print(c)
print(p1)

stock1.stock_get(p)
stock1.stock_get(s)
stock1.stock_get(c)
stock1.stock_get(p1)

stock1.stock_give(p, stock2)

stock1.list_equipments()
stock2.list_equipments()
