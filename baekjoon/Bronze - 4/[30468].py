temp = list(map(int, input().split()))
f = temp[0] + temp[1] + temp[2] + temp[3]
t = temp[4] * 4

if t > f:
    print(t - f)
else:print(0)
