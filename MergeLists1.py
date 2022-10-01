#  Copyright (c) Vladimir Modenov.
#  Created: 01.10.2022, 14:03
#  Project: StepikPythonProjects
#  File: MergeLists1.py

# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию
# списка, состоящих из целых чисел, и объединяет их в один отсортированный список.

# объявление функции
def merge(list1, list2):
    return sorted(list1 + list2)


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
