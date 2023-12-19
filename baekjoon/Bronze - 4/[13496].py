n = int(input())

for i in range(n):
    ns, ss, nd = map(int, input().split())
    
    cnt = 0
    for j in range(ns):
        sd, ncnt = map(int, input().split())
        
        if nd * ss >= sd:
            cnt += ncnt

    print(f'Data Set {i + 1}:')
    print(cnt)
    print()
