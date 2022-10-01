#  Copyright (c) Vladimir Modenov.
#  Created: 01.10.2022, 15:26
#  Project: StepikPythonProjects
#  File: MergeLists2.py

# На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один
# отсортированный список с помощью функции quick_merge(), а затем выводит его.

n = int(input())


def quick_merge(num):
    return sorted([int(i) for i in range(num) for i in input().split()])


print(*quick_merge(n))
