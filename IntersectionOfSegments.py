# На числовой прямой даны два отрезка: a1, b1; a2, b2.
# Напишите программу, которая находит их пересечение.

# my code
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (b1 == a2):
    print(b1)
elif (b2 == a1):
    print(b2)
elif (b1 < a2 or b2 < a1):
    print("пустое множество")
else:
    print(max(a1, a2), min(b1, b2))

# not my code
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print("пустое множество")
else:
    if a1 > a2:
        a2 = a1
    if b1 > b2:
        b1 = b2
    if a2 == b1:
        print(a2)
    else:
        print(a2, b1)
