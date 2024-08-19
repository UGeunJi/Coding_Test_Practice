n = int(input())
r = 0

for _ in range(n):
    s = list(map(int, input().split()))

    if sum(s) == -3:
        continue

    for i in range(3):
        if s[i] == -1:
            s[i] = 121

    if s[0] <= s[1] <= s[2]:
        r += 1

print(r)
