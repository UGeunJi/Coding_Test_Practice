while 1:
    n = int(input())
    if n == 0:
        break
    print(f"{n} => {n ** 2 - (n - 1)}")
