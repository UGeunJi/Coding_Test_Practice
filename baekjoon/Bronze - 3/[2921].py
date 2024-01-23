n = int(input())
cnt = 0

for i in range(1, n + 1):
    cnt += 1.5 * i * (i + 1)

print(int(cnt))
