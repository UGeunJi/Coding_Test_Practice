n = int(input())

for i in range(n):
    li = sorted(list(map(int, input().split())))
    ma = li[2] ** 2
    el = li[0] ** 2 + li[1] ** 2

    if ma == el:
        print(f'Scenario #{i + 1}:')
        print('yes')
        print()
    else:
        print(f'Scenario #{i + 1}:')
        print('no')
        print()
