#  Copyright (c) Vladimir Modenov.
#  Created: 14.09.2022, 22:45
#  Project: StepikPythonProjects
#  File: ListOfClubs.py

# На вход программе подается натуральное число n, а затем nn целых чисел. Напишите программу, которая создает
# из указанных чисел список их кубов.

n = int(input())
myList = []

for i in range(n):
    myList.append(int(input()) ** 3)

print(myList)
