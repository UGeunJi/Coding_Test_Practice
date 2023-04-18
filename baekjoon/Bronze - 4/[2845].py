a, b = map(int, input().split())

l = list(map(int, input().split()))

for i in range(len(l)):
    l[i] = l[i] - a * b

print(*l, sep=' ')
