a, b, c = map(int, input().split())

for i in range(a):
    n = int(input())
    if n ** 2 <= b ** 2 + c ** 2:
        print('YES')
    else:
        print('NO')
