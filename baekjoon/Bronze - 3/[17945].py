a, b = map(int, input().split())

c = -a + (a ** 2  -b) ** (0.5)
d = -a - (a ** 2  -b) ** (0.5)

if c > d:
    print(int(d), int(c))
elif c == d:
    print(int(c))
elif c < d:
    print(int(c), int(d))
