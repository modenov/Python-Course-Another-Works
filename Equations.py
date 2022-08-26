#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 23:10
#  Project: StepikPythonProjects
#  File: Equations.py

total = 0
for x in range(1, 366):
    for y in range(1, 366):
        for z in range(1, 366):
            if 28 * x + 30 * y + 31 * z == 365:
                total += 1
                print('n =', x, 'k =', y, 'm =', z)

print('Общее количество натуральных решений =', total)


# Стариная задача про быков, коров и телят
for b in range(0, 100):
    for c in range(0, 100):
        for d in range(0, 100):
            if (10*b + 5*c + 0.5*d == 100) and (b + c + d == 100):
                print(b, c, d)
