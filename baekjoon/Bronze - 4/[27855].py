H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())

P1 = (H1 * 3) + B1
P2 = (H2 * 3) + B2

if P1 == P2:
    print('NO SCORE')
elif P2 < P1:
    print(f'{1} {P1 - P2}')
elif P1 < P2:
    print(f'{2} {P2 - P1}')
