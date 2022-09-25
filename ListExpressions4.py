#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 17:37
#  Project: StepikPythonProjects
#  File: ListExpressions4.py

# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел палиндромов от
# 100 до 1000.

palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]

print(palindromes)
