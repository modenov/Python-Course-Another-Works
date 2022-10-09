#  Copyright (c) Vladimir Modenov.
#  Created: 09.10.2022, 20:55
#  Project: StepikPythonProjects
#  File: ListsExam.py

numbers = list(range(3))
print(numbers)


numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:3]
print(my_list)


numbers = [1, 2, 3, 4, 5]
my_list = numbers[:-1]
print(my_list)


numbers = [1, 2, 3, 4, 5]
my_list = numbers[:]
print(my_list)


s = int(input())
b = []
for i in range(1, s + 1):
    if i % 2 == 0:
        b.append(i)
print(b)


a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

my_list = [a[i] + b[i] for i in range(len(a))]

print(*my_list)


n = [int(i) for i in input().split()]
print(*n, sep='+', end='=')

print(sum(n))


n = input().split("-")
c = [len(i) for i in n]
if c == [3, 3, 4] and ''.join(n).isdigit():
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
    print("YES")
else:
    print("NO")


