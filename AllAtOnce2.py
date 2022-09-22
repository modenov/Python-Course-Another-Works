#  Copyright (c) Vladimir Modenov.
#  Created: 22.09.2022, 21:48
#  Project: StepikPythonProjects
#  File: AllAtOnce2.py

# Дополните приведенный код, чтобы он:

numbers = [8, 9, 10, 11]

numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)

print(numbers)
