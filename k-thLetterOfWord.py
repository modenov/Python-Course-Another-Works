#  Copyright (c) Vladimir Modenov.
#  Created: 16.09.2022, 21:18
#  Project: StepikPythonProjects
#  File: k-thLetterOfWord.py

# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
myList = []

for i in range(n):
    number = input()
    myList.append(number)

k = int(input())
k1 = ''

for j in myList:
    if len(j) >= k:
        k1 += j[k - 1]

print(k1)
