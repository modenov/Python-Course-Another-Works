#  Copyright (c) Vladimir Modenov.
#  Created: 16.09.2022, 21:04
#  Project: StepikPythonProjects
#  File: RemoveOddIndexes.py

# На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из
# указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

n = int(input())
myList = []

for i in range(n):
    number = int(input())
    myList.append(number)

print(myList[::2])
