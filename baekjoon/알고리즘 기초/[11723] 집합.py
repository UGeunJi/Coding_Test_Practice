import sys

s = []

n = int(sys.stdin.readline())

for i in range(n):
    st = sys.stdin.readline().split()
    if st[0] == 'add':
        if int(st[1]) in s:
            continue
        else:
            s.append(int(st[1]))

    elif st[0] == 'remove':
        if int(st[1]) not in s:
            continue
        else:
            s.remove(int(st[1]))

    elif st[0] == 'check':
        if int(st[1]) in s:
            print(1)
        else:
            print(0)

    elif st[0] == 'toggle':
        if int(st[1]) in s:
            s.remove(int(st[1]))
        else:
            s.append(int(st[1]))

    elif st[0] == 'all':
        s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    elif st[0] == 'empty':
        s = []
