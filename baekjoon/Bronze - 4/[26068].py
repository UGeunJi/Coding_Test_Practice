n = int(input())
answer = 0

for i in range(n):
    s1, s2 = input().split('-')
    if int(s2) <= 90:
        answer += 1
    
print(answer)    
