#  Copyright (c) Vladimir Modenov.
#  Created: 18.09.2022, 16:50
#  Project: StepikPythonProjects
#  File: NoDuplicates.py

# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только
# уникальные строки, в том же порядке, в котором они были введены.

n = int(input())
myList = []

for i in range(n):
    s = input()
    if s not in myList:
        myList.append(s)

print(*myList, sep='\n')
