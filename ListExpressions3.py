#  Copyright (c) Vladimir Modenov.
#  Created: 25.09.2022, 17:26
#  Project: StepikPythonProjects
#  File: ListExpressions3.py

# Дополните приведенный код списочным выражением, чтобы получить новый список, содержащий только слова длиной
# не менее пяти символов (включительно).

keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [m for m in keywords if len(m) >= 5]

print(new_keywords)
