n = int(input())
num = 0
triple = 0

for i in range(n):
    num += i + 1
    triple += (i + 1) ** 3

square = num ** 2

print(num)
print(square)
print(triple)
