#  Copyright (c) Vladimir Modenov.
#  Created: 07.10.2022, 23:40
#  Project: StepikPythonProjects
#  File: CodeReview9.py

n = 4
count = 0
maximum = -999999

for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
