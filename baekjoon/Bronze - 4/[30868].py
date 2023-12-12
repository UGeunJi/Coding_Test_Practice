t = int(input())

for i in range(t):
    n = int(input())
    
    mok = n // 5
    nam = n % 5
    
    for _ in range(mok):
        print('++++', end=' ')
    
    for _ in range(nam):
        print('|', end='')
    print('')
