#  Copyright (c) Vladimir Modenov.
#  Created: 04.09.2022, 14:09
#  Project: StepikPythonProjects
#  File: Most-Frequent-Symbol.py

# На вход программе подается строка текста. Напишите программу, которая выводит на экран символ,
# который появляется наиболее часто.

s = input()
count = 0
total = 0

for i in s:
    if s.count(i) >= count:
        count = s.count(i)
        total = i

print(total)
