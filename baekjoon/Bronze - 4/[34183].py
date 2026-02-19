n, m, a, b = map(int, input().split())

if n * 3 > m:
    print((n * 3 - m) * a + b)
else:
    print(0)
