"""
1.	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


my_f = open("test.txt", 'w')
lines = []
while True:
    my_f.writelines(lines)
    line = input("Введите текст (для окончания ввода оставьте пустую строку):\n")
    if not line:
        break

with open("text.txt", 'r') as my_f:
    content = my_f.readlines()
    print(content)
