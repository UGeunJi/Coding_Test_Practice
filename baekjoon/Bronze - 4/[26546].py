for i in range(int(input())):
    sen, a, b = input().split()
    
    t1 = sen[:int(a)]
    t2 = sen[int(b):]
    ans = t1 + t2
    
    print(ans)
