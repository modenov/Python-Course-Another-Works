#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 20:52
#  Project: StepikPythonProjects
#  File: Table3.py

# Дано натуральное число n (n ≤ 9). Напишите программу, которая печатает таблицу умножения для всех чисел
# от 1 до n в соответствии с примером. На вход программе подается одно натуральное число.

n = int(input())

for i in range(2, n + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()
