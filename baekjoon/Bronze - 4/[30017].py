a, b = map(int, input().split())

cnt = 3

a -= 2
b -= 1

c = min(a, b)

cnt += (2 * c)

print(cnt)
