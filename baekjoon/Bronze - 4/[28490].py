n = int(input())
temp = []

for i in range(n):
    a, b = map(int, input().split())
    temp.append(a * b)
    
print(max(temp))
