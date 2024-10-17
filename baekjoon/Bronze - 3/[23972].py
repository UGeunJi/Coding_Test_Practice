K, N = map(int, input().split())
 
if N == 1:
    print(-1)
else:
    a = (K * N) // (N - 1)
    if(K * N) % (N - 1):
        a += 1 
    print(a)
