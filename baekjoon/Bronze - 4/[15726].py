a, b, c = map(int,input().split())

d = a * b / c
e = a / b * c

if(d > e):
    print(int(d))
else:
    print(int(e))
