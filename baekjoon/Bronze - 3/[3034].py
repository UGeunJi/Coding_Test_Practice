n, h, w = map(int, input().split())
diag = ((h ** 2) + (w ** 2)) ** (1 / 2)

for i in range(n):
    length = int(input())
    if length <= diag:
        print('DA')
    else:
        print('NE')
