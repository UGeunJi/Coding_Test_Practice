n, m = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = 0

for i in a:
    l += i

    if l < 0:
        l = 0

    if l >= m:
        r += 1

print(r)
