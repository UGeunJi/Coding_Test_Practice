for _ in range(int(input())):
    k, N = map(int, input().split())
    s1 = N*(N+1)//2
    s2 = int((N*2)*(N/2))
    s3 = int((N*2+2)*(N/2))
    print(k, s1, s2, s3)
