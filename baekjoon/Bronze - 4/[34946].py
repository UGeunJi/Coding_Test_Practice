a, b, c, d = map(int, input().split())

if a + b > d and c > d:
    print('T.T')
elif a + b <= d and c > d:
    print('Shuttle')
elif a + b > d and c <= d:
    print('Walk')
else:
    print('~.~')
