n = int(input())

for i in range(n):
    num, base = map(str, input().split())
    if base == 'kg':
        num = float(num) * 2.2046
        base = 'lb'
    elif base == 'lb':
        num = float(num) * 0.4536
        base = 'kg'
    elif base == 'l':
        num = float(num) * 0.2642
        base = 'g'
    elif base == 'g':
        num = float(num) * 3.7854
        base = 'l'

    print(f'{num:.4f} {base}')
