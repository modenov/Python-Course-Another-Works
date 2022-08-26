#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 18:39
#  Project: StepikPythonProjects
#  File: WhileInWhile.py

# first tack
for i in range(1, 4):
    for j in range(3, 5):
        print(i, j)

# second tack
counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)