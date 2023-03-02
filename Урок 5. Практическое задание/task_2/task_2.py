"""
2.	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_lines: int = 0
my_words: int = 0

with open("text(task_2).txt", 'r') as my_file:
    for line in my_file:
        my_lines += 1
        my_words += len(line.split())

print("Lines:", my_lines)
print("Words:", my_words)
