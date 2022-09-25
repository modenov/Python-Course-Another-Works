#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 20:11
#  Project: StepikPythonProjects
#  File: InOneLine3.py

# На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное
# выражение, которая выведет квадраты четных чисел, которые не оканчиваются на цифру 4.

print(*[int(i) ** 2 for i in input().split() if i[-1] in "046"])
