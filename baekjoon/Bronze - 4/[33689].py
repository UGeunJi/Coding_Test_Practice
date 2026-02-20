n = int(input())
cnt = 0

for i in range(n):
    s = list(input())
    if s[0] == 'C':
        cnt += 1

print(cnt)
