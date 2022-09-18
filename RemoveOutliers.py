#  Copyright (c) Vladimir Modenov.
#  Created: 18.09.2022, 16:44
#  Project: StepikPythonProjects
#  File: RemoveOutliers.py

# На вход программе подается натуральное число n, а затем nn различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит
# ставшиеся числа каждое на отдельной строке, не меняя их порядок.

n = int(input())
myList = []

for i in range(n):
    x = int(input())
    myList.append(x)

myList.remove(min(myList))
myList.remove(max(myList))

print(*myList, sep='\n')
