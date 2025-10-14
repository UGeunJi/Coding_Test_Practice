n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n - 1):
    if li[i] - li[i + 1] >= k:
        cnt += 1

print(cnt)
