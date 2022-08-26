#  Copyright (c) Vladimir Modenov.
#  Created: 20.08.2022, 23:48
#  Project: StepikPythonProjects
#  File: FollowTheRules.py

# На вход программе подается натуральное число n.
# Напишите программу, которая выводит числа от 1 до nnn включительно за исключением:

n = int(input())

for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(i)
