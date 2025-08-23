x, y = map(int, input().split())
d = 100000
n = int(input())

for i in range(n):
    x1, y1 = map(int, input().split())
    d1 = abs(x1 - x) + abs(y1 - y)
    if d > d1:
        d = d1
        mx = x1
        my = y1
 
print(mx, my)
