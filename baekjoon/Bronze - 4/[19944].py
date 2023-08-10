n, m = map(int, input().split())

if n >= m and (m == 1 or m == 2):
    print('NEWBIE!')
elif n >= m and m != 1 and m != 2:
    print('OLDBIE!')
else:
    print('TLE!')
