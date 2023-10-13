for _ in range(int(input())):
    l = [*input().split()]
    c = 0
    for i in l:
        if len(i) >= 2:
            c += 1
        
    print(*l)
    print(["zilch\n", "double\n", "double-double\n", "triple-double\n"][c])
