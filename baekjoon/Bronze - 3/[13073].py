for _ in range(int(input())):
    n = int(input())
    s1 = n * (n + 1) // 2
    s2 = int((n * 2) * (n / 2))
    s3 = int((n * 2 + 2) * (n / 2))
    print(s1, s2, s3)
