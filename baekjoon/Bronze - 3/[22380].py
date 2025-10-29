while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    money = list(map(int, input().split()))
    pay = m // n
    res = 0
    for i in money:
        if i >= pay:
            res += pay
        else:
            res += i
    print(res)
