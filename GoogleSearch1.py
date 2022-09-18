#  Copyright (c) Vladimir Modenov.
#  Created: 18.09.2022, 16:57
#  Project: StepikPythonProjects
#  File: GoogleSearch1.py

# На вход программе подается натуральное число nn, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.

n = [input() for x in range(int(input()))]
x = input().lower()

for i in n:
    if x in i.lower():
        print(i)
