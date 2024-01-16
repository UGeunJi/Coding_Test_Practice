n = 0
max_list = []

for i in range(4):
    a, b = map(int, input().split())

    n += b
    n -= a
    max_list.append(n)

print(max(max_list))
