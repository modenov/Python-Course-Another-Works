#  Copyright (c) Vladimir Modenov.
#  Created: 06.09.2022, 22:31
#  Project: StepikPythonProjects
#  File: ListOfNumbers.py

# На вход программе подается одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].

n = int(input())

mylist = list(range(1, n + 1))

print(mylist)
