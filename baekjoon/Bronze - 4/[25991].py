n = int(input())
c = [*map(float, input().split())]

for i in range(n) :
    c[i] = c[i] ** 3

print(pow(sum(c), 1 / 3))
