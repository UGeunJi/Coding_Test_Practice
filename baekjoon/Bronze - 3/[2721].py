for _ in range(int(input())):
    n = int(input())
    temp = sum(k * sum(range(k + 2)) for k in range(1, n + 1))
    print(temp)
