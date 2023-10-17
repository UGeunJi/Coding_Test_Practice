t = 'N'

for i in range(10):
    n = int(input())
    
    if t == 'N':
        if n == 1:
            t = 'E'
        elif n == 3:
            t = 'W'
        else:
            t = 'S'
    elif t == 'W':
        if n == 1:
            t = 'N'
        elif n == 3:
            t = 'S'
        else:
            t = 'E'
    elif t == 'E':
        if n == 1:
            t = 'S'
        elif n == 3:
            t = 'N'
        else:
            t = 'W'
    elif t == 'S':
        if n == 1:
            t = 'W'
        elif n == 3:
            t = 'E'
        else:
            t = 'N'

print(t)
