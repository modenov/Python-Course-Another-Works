#  Copyright (c) Vladimir Modenov.
#  Created: 07.10.2022, 23:47
#  Project: StepikPythonProjects
#  File: CodeReview8.py

n = 8 # n = 7, по условию чисел 8
count = 0
maximum = -10**6 - 1 # maximum = 1000, все случаи, когда все числа меньше 1000, обрабатываются неверно
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0: # x // 4 == 0, по условию нужно найти числа, дел. на 4 без остатка
        count += 1
        if x > maximum: # if x < maximum, если число больше максимума, оно его заменяет, не если меньше максимума
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
