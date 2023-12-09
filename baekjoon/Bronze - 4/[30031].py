n = int(input())
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    if a == 136:
        sum += 1000
    elif a == 142:
        sum += 5000
    elif a == 148:
        sum += 10000
    else:
        sum += 50000
        
print(sum)
