k, d, a = map(int, input().split('/'))

if k + a < d:
    print('hasu')
elif d == 0:
    print('hasu')
else:
    print('gosu')
