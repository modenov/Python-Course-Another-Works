#  Copyright (c) Vladimir Modenov.
#  Created: 27.08.2022, 23:34
#  Project: StepikPythonProjects
#  File: Number2.py

# На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек),
# если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).

s = input()
counter = 0

for i in range(0, len(s)):
    if s[i] in '0123456789':
        counter += 1

if counter > 0:
    print("Цифра")
else:
    print("Цифр нет")
