N = int(input())
li = list(map(int, input().split()))
r = 0

for i in range(n - 1):
    r += (i + 1)
    r -= li[i]
print(r + n)
