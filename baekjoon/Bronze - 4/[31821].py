n = int(input())
l = [int(input()) for _ in range(n)]
r = 0

a = int(input())
for _ in range(a):
    m = int(input())
    r += l[m - 1]

print(r)
