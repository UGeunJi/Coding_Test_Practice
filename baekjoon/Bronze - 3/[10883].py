N = int(input())
answer = 0
for _ in range(N):
    A, B = map(int, input().split())
    answer += B % A
    
print(answer)
