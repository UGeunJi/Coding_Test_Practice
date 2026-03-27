n = int(input())
snt = 0
for i in range(n):
    a, b, c, d = map(int, input().split())
    if a >= 1000 or b >= 1600 or c >= 1500 or d <= 30 and d != -1:
        snt += 1
        
print(snt)
