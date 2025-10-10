t = int(input())
for i in range(t):
    x1, y1, f1, x2, y2, f2 = map(int, input().split())
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    f = f1 + f2
    print(x + y + f)
