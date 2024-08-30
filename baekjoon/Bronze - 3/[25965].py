N = int(input())
for _ in range(N):
    M = int(input())
    cnt = 0
    lst = []
    for _ in range(M):
        lst.append(list(map(int, input().split())))
    KDA = list(map(int, input().split()))
    
    for i in lst:
        tmp = 0
        for j in range(3):
            if j != 1:
                tmp += i[j] * KDA[j]
            else:
                tmp -= i[j] * KDA[j]
        if tmp > 0:
            cnt += tmp
    print(cnt)
