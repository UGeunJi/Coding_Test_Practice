a, t = map(int, input().split())

if a - t >= 30:
    print(0)
else:
    print(10 + 2 * (25 - a + t))
