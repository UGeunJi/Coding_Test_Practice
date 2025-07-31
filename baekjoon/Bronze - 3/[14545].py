for _ in range(int(input())):
    n = int(input())
    res = sum([i ** 2 for i in range(1, n + 1)])
    print(res)
