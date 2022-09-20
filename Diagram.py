#  Copyright (c) Vladimir Modenov.
#  Created: 20.09.2022, 21:03
#  Project: StepikPythonProjects
#  File: Diagram.py

# На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам
# строит столбчатую диаграмму.

nums = input().split()

for i in range(len(nums)):
    nums[i] = int(nums[i])
    print('+' * nums[i], end='\n')
