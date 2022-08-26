# Separate big number
n = int(input())
print(n // 10000)
print(n % 10000 // 1000)
print(n % 1000 // 100)
print(n % 100 // 10)
print(n % 10)
