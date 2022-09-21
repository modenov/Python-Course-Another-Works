#  Copyright (c) Vladimir Modenov.
#  Created: 21.09.2022, 22:35
#  Project: StepikPythonProjects
#  File: ListsAppendExtend.py

myList = ['hello', 'my', 'name', 'vova']

myList.append('modenov')
print(myList)

myList.extend('modenov')
print(myList)

# insert
names = ['Gvido', 'Roman' , 'Timur']
print(names)

names.insert(0, 'Anders')
print(names)

names.insert(4, 'Josef')
print(names)

# index
names = ['Gvido', 'Roman' , 'Timur']
position = names.index('Timur')
print(position)

names = ['Gvido', 'Roman' , 'Timur']
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в списке')

# remove
food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')
print(food)

# pop
names = ['Gvido', 'Roman' , 'Timur']
item = names.pop(1)
print(item)
print(names)

# count
names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1)
print(cnt2)
print(cnt3)

# reverse
names = ['Gvido', 'Roman' , 'Timur']
names.reverse()
print(names)

# clear
names = ['Gvido', 'Roman' , 'Timur']
names.clear()
print(names)

# copy
names = ['Gvido', 'Roman' , 'Timur']
names_copy = names.copy() # создаем поверхностную копию списка names

print(names)
print(names_copy)

# аналог copy
names = ['Gvido', 'Roman' , 'Timur']
names_copy1 = list(names)             # создаем поверхностную копию с помощью функции list()
names_copy2 = names[:]                # создаем поверхностную копию с помощью среза от начала до конца


colors = ['Orange']
colors.append('Red')
colors.append('Blue')
colors.append('Green')
colors.insert(0, 'Violet')
colors.insert(2, 'Purple')

print(colors)

colors = ['Red', 'Blue', 'Green', 'Black', 'White']
del colors[-1]
colors.remove('Green')

print(colors)

# sort
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort()
print('Отсортированный список:', a)

a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort(reverse = True)   # сортируем по убыванию
print('Отсортированный список:', a)

a = ['бета', 'альфа', 'дельта', 'гамма']
a.sort()
print ('Отсортированный список:', a)

numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
numbers.sort()
del numbers[0]
del numbers[-1]
numbers.sort(reverse=True)
print(numbers)