n = int(input())
temp = 1

for i in range(n):
    temp *= i + 1

temp = list(str(temp))

print(temp[-1])
