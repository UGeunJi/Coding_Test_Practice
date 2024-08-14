from sys import stdin

n, k = map(int, stdin.readline().split(' '))
fk = k % 10
f2k = (2 * k) % 10
li = []

for i in range(1, n + 1):
    fx = i % 10
    if fx != fk and fx != f2k:
        li.append(str(i))

print(len(li))
print(*li)
