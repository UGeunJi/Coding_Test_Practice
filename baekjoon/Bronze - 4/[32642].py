n = int(input())
w = list(map(int, input().split()))
a = [0] * n
s = 0

for i in range(n):
    if w[i] == 1:
        s += 1
    elif w[i] == 0:
        s -= 1

    a[i] = s

print(sum(a))
