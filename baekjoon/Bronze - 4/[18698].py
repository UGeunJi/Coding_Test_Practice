for _ in range(int(input())) :
    cnt = 0
    for char in input() :
        if char == 'D' : break
        cnt += 1
    print(cnt)
