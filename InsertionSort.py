#  Copyright (c) Vladimir Modenov.
#  Created: 26.09.2022, 21:17
#  Project: StepikPythonProjects
#  File: InsertionSort.py

# Алгоритм сортировки простыми вставками

a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(1, n):
    elem = a[i]  # первый элемент из неотсортированной части списка
    j = i
    while j >= 1 and a[j - 1] > elem:
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem

print('Отсортированный список:', a)
