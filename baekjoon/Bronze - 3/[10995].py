n = int(input())

if n == 1:
    print('*')
    
else:
    for i in range(n):
        if i % 2 == 0:
            a = print('* ' * n)
        else:
            b = print(' *' * n)
