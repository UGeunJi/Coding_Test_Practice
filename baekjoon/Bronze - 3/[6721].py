for _ in range(int(input())):
    a, b = input().split()
    res = int(str(int(a[::-1]) + int(b[::-1]))[::-1])
    print(res)
