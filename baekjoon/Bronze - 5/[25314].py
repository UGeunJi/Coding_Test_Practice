n = int(input())
arr = []


for i in range(n // 4):
    arr.append('long')
    
arr.append('int')

print(*arr)
