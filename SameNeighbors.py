#  Copyright (c) Vladimir Modenov.
#  Created: 28.08.2022, 17:07
#  Project: StepikPythonProjects
#  File: SameNeighbors.py

# На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней
# одинаковых соседних символов.

s = input()
counter = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        counter += 1

print(counter)
