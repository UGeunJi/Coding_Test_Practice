n = int(input())
num = 1

for i in range(0, n):
    num *= i + 1

print(num // (7 * 24 * 60 * 60))
