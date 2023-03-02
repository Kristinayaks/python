"""
4.	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

line_en = []
with open("text(task_3).txt", 'r') as my_file:
    line_en = my_file.read()

line_ru = line_en
for en, ru in dictionary.items():
    line_ru = line_ru.replace(en, ru)

with open("text_new(task_3).txt", 'w') as new_file:
    new_file.write(line_ru)
