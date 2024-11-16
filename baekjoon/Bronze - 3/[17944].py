n, t = map(int, input().split())
cnt = 0
x = 1

for i in range(t):
    cnt += x
    if(cnt == 2 * n):
        x = -1
    if(cnt == 1):
        x = 1

print(cnt)
