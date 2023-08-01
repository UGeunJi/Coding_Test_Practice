a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0

for i in range(3):
    temp = b[i] - a[i]
    if temp < 0:
        pass
    else:
        answer += temp
        
print(answer)
