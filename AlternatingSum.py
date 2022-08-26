#  Copyright (c) Vladimir Modenov.
#  Created: 14.08.2022, 23:35
#  Project: StepikPythonProjects
#  File: AlternatingSum.py

# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы 1-2+3-4-5-6+...+(-1) в степени (n+1)*n

n = int(input())
counter = 0
for i in range(n):
    if i % 2 == 0:
        counter += i + 1
    else:
        counter -= i + 1
print(counter)
