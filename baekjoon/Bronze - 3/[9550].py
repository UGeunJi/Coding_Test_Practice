for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    
    for i in c:
        ans += i // k
    print(ans)
