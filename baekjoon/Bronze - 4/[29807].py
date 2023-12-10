res = 0

t = int(input())
sub = list(map(int, input().split())) + [0] * (5 - t)

if sub[0] > sub[2]:
    res += (sub[0] - sub[2]) * 508
else:
    res += (sub[2] - sub[0]) * 108

if sub[1] > sub[3]:
    res += (sub[1] - sub[3]) * 212
else:
    res += (sub[3] - sub[1]) * 305

if sub[4] > 0:
    res += sub[4] * 707

res *= 4763

print(res)
