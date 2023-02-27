"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, production_in_hours, rate_per_hour, premium = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", production_in_hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", premium)
print("Заработная плата сотрудника: ",
      (float(production_in_hours) * float(rate_per_hour)) + float(premium))
