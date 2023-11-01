a, p = map(int, input().split())

if a * 7 == p * 13:
    print('lika')
else:
    print('Petra' if a * 7 < p * 13 else 'Axel')
