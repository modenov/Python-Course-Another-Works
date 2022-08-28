#  Copyright (c) Vladimir Modenov.
#  Created: 28.08.2022, 17:16
#  Project: StepikPythonProjects
#  File: Vowels&Consonants.py

# На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет
# количество гласных и согласных букв.

s = input().lower()
vowels = 0
consonants = 0

glas = "ауоыиэяюёе"
soglas = "бвгджзйклмнпрстфхцчшщ"

for i in range(len(s) - 1):
    if s[i] in glas:
        vowels += 1
    if s[i] in soglas:
        consonants += 1

print("Количество гласных букв равно", vowels)
print("Количество согласных  букв равно", consonants)
