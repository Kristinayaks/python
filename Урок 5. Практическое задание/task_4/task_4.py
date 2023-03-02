"""
4. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

employees = {"Приветов": 55550.00, "Любимова": 9999.99, "Гатихинский": 33033.33, "Владимиров": 123123.13,
             "Авдеев": 43300.54, "Морозова": 78567.00, "Краузе": 8100.78, "Солнцев": 25300.65,
             "Мирчук": 12300.54, "Веселов": 71711.00, "Жданова": 12300.54, "Дианов": 33456.87}
try:
    with open("text(task_4).txt", 'r+') as my_file:
        for last_name, salary in employees.items():
            my_file.write(last_name + " " + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")

summa: int = 0
count: int = 0
last_name_employees = []
with open("text(task_4).txt", 'r') as my_f:
    for line in my_f:
        print(line, end="")
        tokens = line.split(" ")
        if float(tokens[1]) < 20000.00:
            last_name_employees.append(tokens[0])
        summa += float(tokens[1])
        count += 1
res = summa / count
print(f"Фамилии сотрудников: {last_name_employees}")
print(f"Средний доход: {res}")
