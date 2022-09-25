#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 18:49
#  Project: StepikPythonProjects
#  File: ListExpressions6.py

# На вход программе подается строка текста, содержащая целые числа. Напишите программу, использующую списочное
# выражение, которая выведет кубы указанных чисел также на одной строке.

print(*[int(i) ** 3 for i in input().split()])
