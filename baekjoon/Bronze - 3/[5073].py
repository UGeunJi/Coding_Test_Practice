while True:
    li = list(map(int, input().split()))
    temp = 0
    if li.count(0) == 3:
        break
    li_sorted = li.sort()
    if li[2] >= li[0] + li[1]:
        print('Invalid')
        continue
    
    for i in range(3):
        if li.count(li[i]) > temp:
            temp = li.count(li[i])
        else:
            pass
    
    if temp == 1:
        print('Scalene')
    elif temp == 2:
        print('Isosceles')
    else:
        print('Equilateral')
