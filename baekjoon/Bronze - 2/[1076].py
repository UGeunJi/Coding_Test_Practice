tt = 0

for i in range(3):
    s = input()
    temp = 0
    if s == 'black':
        if i == 0 or i == 1:
            temp = 0
        else:
            temp = 1
    elif s == 'brown':
        if i == 0 or i == 1:
            temp = 1
        else:
            temp = 10
    elif s == 'red':
        if i == 0 or i == 1:
            temp = 2
        else:
            temp = 100
    elif s == 'orange':
        if i == 0 or i == 1:
            temp = 3
        else:
            temp = 1000
    elif s == 'yellow':
        if i == 0 or i == 1:
            temp = 4
        else:
            temp = 10000
    elif s == 'green':
        if i == 0 or i == 1:
            temp = 5
        else:
            temp = 100000
    elif s == 'blue':
        if i == 0 or i == 1:
            temp = 6
        else:
            temp = 1000000
    elif s == 'violet':
        if i == 0 or i == 1:
            temp = 7
        else:
            temp = 10000000
    elif s == 'grey':
        if i == 0 or i == 1:
            temp = 8
        else:
            temp = 100000000
    elif s == 'white':
        if i == 0 or i == 1:
            temp = 9
        else:
            temp = 1000000000
    if i == 0:
        tt += temp
    elif i == 1:
        tt = str(tt)
        tt += str(temp)
    else:
        tt = int(tt)
        tt *= temp
        
print(tt)
