r, ar = map(int, input().split())
n = int(input())

for _ in range(n):
    t = int(input())
    if t <= 1000:
        print(t, r*t)
    else:
        print(t, r*1000 + (t-1000)*ar)
