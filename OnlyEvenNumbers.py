#  Copyright (c) Vladimir Modenov.
#  Created: 15.08.2022, 19:35
#  Project: StepikPythonProjects
#  File: OnlyEvenNumbers.py

# Напишите программу, которая считывает последовательность из 10 целых чисел
# и определяет является ли каждое из них четным или нет.

counter = 0

for i in range(10):
    n = int(input())
    if n % 2 == 0:
        counter = counter + 1

if counter == 10:
    print("YES")
else:
    print("NO")
