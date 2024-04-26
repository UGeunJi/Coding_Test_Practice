C, K, P = map(int, input().split())
answer = 0

for i in range(1, C + 1):    
    answer += K * i + P * (i ** 2)
    
print(answer)
