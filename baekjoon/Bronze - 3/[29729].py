import sys
input = sys.stdin.readline

S, N, M = map(int, input().split())

cnt = 0
for i in range(N+M) : 
    num = int(input())
    
    if num == 1 : 
        if S == cnt : 
            S += S
        cnt += 1
    else : 
        cnt -= 1
        
print(S)
