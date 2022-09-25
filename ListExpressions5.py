#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 17:40
#  Project: StepikPythonProjects
#  File: ListExpressions5.py

# На вход программе подается натуральное число n. Напишите программу, использующую списочное выражение, которая
# создает список содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно, то есть каждый на
# отдельной строке.

n = int(input())

myList = [i ** 2 for i in range(1, n + 1)]

print(*myList, sep='\n')
