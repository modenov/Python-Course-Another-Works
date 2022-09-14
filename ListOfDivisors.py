#  Copyright (c) Vladimir Modenov.
#  Created: 14.09.2022, 23:18
#  Project: StepikPythonProjects
#  File: ListOfDivisors.py

# На вход программе подается натуральное число n. Напишите программу, которая создает список состоящий из делителей
# введенного числа.

n = int(input())
myList = []

for i in range(1, n + 1):
    if n % i == 0:
        myList.append(i)

print(myList)
