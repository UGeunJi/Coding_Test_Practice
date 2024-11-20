n = int(input())

for _ in range(n):
    print('@' * (5 * n))

for _ in range(n * 3):
    print('@' * n + ' ' * (n * 3) + '@' * n)

for _ in range(n):
    print('@' * (5 * n))
