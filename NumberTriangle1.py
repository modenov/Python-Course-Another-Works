#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 21:08
#  Project: StepikPythonProjects
#  File: NumberTriangle1.py

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()
