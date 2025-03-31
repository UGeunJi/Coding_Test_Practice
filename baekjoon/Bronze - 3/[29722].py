y, m, d = map(int, input().split("-"))
N = int(input())

d += N
m += (d - 1) // 30
d = (d - 1) % 30 + 1
y += (m - 1) // 12
m = (m - 1) % 12 + 1

print("{}-{}-{}".format(y, str(m).zfill(2), str(d).zfill(2)))
