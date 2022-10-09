#  Copyright (c) Vladimir Modenov.
#  Created: 09.10.2022, 21:19
#  Project: StepikPythonProjects
#  File: FuncExam.py

# объявление функции
def draw_triangle():
    m = 15
    for i in range(1, m + 1, 2):
        print(' ' * ((m - i) // 2) + '*' * i)

# основная программа
draw_triangle()

from math import factorial as f

# объявление функции
def compute_binom(n, k):
    return f(n)//(f(k)*f(n-k))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
