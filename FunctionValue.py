#  Copyright (c) Vladimir Modenov.
#  Created: 18.09.2022, 15:43
#  Project: StepikPythonProjects
#  File: FunctionValue.py

# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого
# введенного числа x выводит значение функции f(x) = x^2 + 2x + 1, каждое на отдельной строке.

n = int(input())
myList = []
myList2 = []

for i in range(1, n + 1):
    x = int(input())
    myList.append(x)
    bigX = (x + 1) ** 2
    myList2.append(bigX)

print(*myList, sep='\n')
print()
print(*myList2, sep='\n')
