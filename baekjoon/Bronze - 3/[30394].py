N = int(input())

maxY = -99999999999999999999999999999999999999999
minY = 99999999999999999999999999999999999999999
for i in range(N) : 
    x, y = map(int, input().split())
    
    maxY = max(y, maxY)
    minY = min(y, minY)
    
print(maxY - minY)
