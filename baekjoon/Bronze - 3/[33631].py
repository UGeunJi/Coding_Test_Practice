Fs, Cs, Es, Bs = map(int, input().split())
Fn, Cn, En, Bn = map(int, input().split())
Q = int(input())
cookie = 0
 
for _ in range(Q):
    q, i = map(int, input().split())
    if q == 1:
        max_cookie = min(Fs // Fn, Cs // Cn, Es // En, Bs // Bn)
        if max_cookie >= i:
            Fs, Cs, Es, Bs = Fs - Fn * i, Cs - Cn * i, Es - En * i, Bs - Bn * i
            cookie += i
            print(cookie)
        else:
            print("Hello, siumii")
    elif q == 2:
        Fs += i
        print(Fs)
    elif q == 3:
        Cs += i
        print(Cs)
    elif q == 4:
        Es += i
        print(Es)
    elif q == 5:
        Bs += i
        print(Bs)
