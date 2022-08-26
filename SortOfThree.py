# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a = int(input())
b = int(input())
c = int(input())

minimum = min(a, b, c)
maximum = max(a, b, c)

second = (a + b + c) - minimum - maximum

print(maximum)
print(second)
print(minimum)
