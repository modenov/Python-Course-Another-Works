#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 16:04
#  Project: StepikPythonProjects
#  File: ListExpressions2.py

# Дополните приведенный код, используя списочное выражение, так чтобы получить новый список, содержащий длины строк
# исходного списка.

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(i) for i in keywords]

print(lengths)
