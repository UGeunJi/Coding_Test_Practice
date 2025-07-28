while True :
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0 : break
    if a == 0 : print(d // c // b, b, c, d)
    elif b == 0 : print(a, d // c // a, c, d)
    elif c == 0 : print(a, b, d // a // b, d)
    else : print(a, b, c, a * b * c)
