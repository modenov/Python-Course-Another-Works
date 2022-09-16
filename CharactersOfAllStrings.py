#  Copyright (c) Vladimir Modenov.
#  Created: 16.09.2022, 21:35
#  Project: StepikPythonProjects
#  File: CharactersOfAllStrings.py

# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает список
# из символов всех строк, а затем выводит его.

n = int(input())
myList = []

for i in range(n):
    number = input()
    myList.extend(number)

print(myList)
