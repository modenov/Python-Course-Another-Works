#  Copyright (c) Vladimir Modenov.
#  Created: 14.09.2022, 22:35
#  Project: StepikPythonProjects
#  File: ListOfStrings.py

# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных
# строк список и выводит его.

n = int(input())
myList = []

for i in range(n):
    myList.append(input())

print(myList)
